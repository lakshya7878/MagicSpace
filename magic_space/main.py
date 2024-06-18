import os
import argparse
import subprocess
import json


# Helper data
CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), "config/workspaces.json")
# ANSI escape code for red color text
red_color_code = "\033[91m"
# ANSI escape code for green color text
green_color_code = "\033[92m"
# ANSI escape code for blue color text
blue_color_code = "\033[94m"
# ANSI escape code to reset text color
reset_color_code = "\033[0m"


# Helper functions below :
def log_green(string):
    print(green_color_code + string + reset_color_code)


def log_red(string):
    print(red_color_code + string + reset_color_code)


def log_blue(string):
    print(blue_color_code + string + reset_color_code, end=" | ")


def load_config():
    if os.path.exists(CONFIG_FILE_PATH):
        try:
            with open(CONFIG_FILE_PATH, "r") as file:
                return json.load(file)
        except:
            with open(CONFIG_FILE_PATH, "w") as file:
                json.dump({}, file, indent=4)
            return {}
    return {}


def write_config(workspace_dict):
    with open(CONFIG_FILE_PATH, "w") as file:
        json.dump(workspace_dict, file, indent=4)


# To find the Application folder on user's device
def find_applications_folder():
    possible_folders = [
        "/Applications",  # Standard location
        os.path.expanduser("~/Applications"),  # User's home Applications folder
    ]

    for folder in possible_folders:
        if os.path.isdir(folder):
            return folder
    return None


def get_all_app_names(folder):
    app_names = set()
    for app_name in os.listdir(folder):
        if app_name.endswith(".app"):
            app_name = app_name[:-4]
            app_names.add(app_name)
    return app_names


# CLI functions here :


# Create a workspace
def create_workspace(args):
    workspaces_dict = load_config()
    if args.workspace.lower() in workspaces_dict:
        log_red(f"Workspace : {args.workspace.lower()} already exists")
        return

    workspaces_dict.update({args.workspace.lower(): {}})
    write_config(workspaces_dict)
    log_green(f"Successfully created workspace : {args.workspace.lower()}")

    # Displaying all apps user can add to workspace
    print("\n")
    folder = find_applications_folder()
    log_blue(
        "Apps on this mac (can be added to this workspace using : magicspace --add <workspace> app-1, app-2 ...) - "
    )
    print("\n")

    app_names = get_all_app_names(folder)
    for app_name in app_names:
        log_blue(app_name)


# Delete a workspace
def delete_workspace(args):
    workspaces_dict = load_config()
    if args.workspace.lower() in workspaces_dict:
        del workspaces_dict[args.workspace.lower()]
        write_config(workspaces_dict)
        log_green(f"Workspace : {args.workspace.lower()} deleted")
        return
    log_red("No such workspace exists")


# Add apps to workspace
def add_apps_to_workspace(args):
    workspaces_dict = load_config()
    workspace_name = args.workspace.lower()
    if workspace_name not in workspaces_dict:
        log_red(f"No workspace named : {workspace_name} found")
        return

    folder = find_applications_folder()
    all_apps_names = get_all_app_names(folder)
    input_app_names = args.apps.split(",")

    for app_name in input_app_names:
        if app_name in all_apps_names:
            workspaces_dict[workspace_name].update({app_name: {}})
            log_green(f"Added app {app_name}")
        else:
            log_red(f"App not found {app_name}")

    write_config(workspaces_dict)


# List all workspaces and the apps that it opens
def list_all_workspaces():
    workspaces_dict = load_config()
    for key, values in workspaces_dict.items():
        log_green("* " + key + " - " + str(list(values.keys())))


# Opens all the apps inside a given workspace
def open_workspace(args):
    workspaces_dict = load_config()
    workspace_name = args.workspace.lower()
    if workspace_name not in workspaces_dict:
        log_red(f"{workspace_name} : No such workspace was found")
        return

    for app in workspaces_dict[workspace_name]:
        subprocess.run(["open", "-a", app])


def main():
    parser = argparse.ArgumentParser(description="CLI app to manage workspaces (apps)")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subparser for 'create' command
    create_parser = subparsers.add_parser("create", help="Create a new workspace")
    create_parser.add_argument(
        "workspace", metavar="<workspace>", type=str, help="Name of the workspace"
    )

    # Subparser for 'delete' command
    delete_parser = subparsers.add_parser("delete", help="Delete a workspace")
    delete_parser.add_argument(
        "workspace", metavar="<workspace>", type=str, help="Name of the workspace"
    )

    # Subparser for 'open' command
    open_parser = subparsers.add_parser("open", help="Open a workspace")
    open_parser.add_argument(
        "workspace", metavar="<workspace>", type=str, help="Name of the workspace"
    )

    # Subparser for 'list' command
    list_parser = subparsers.add_parser("list", help="Lists all workspaces")

    # Subparser for 'add' command
    add_parser = subparsers.add_parser("add", help="Add apps to a workspace")
    add_parser.add_argument(
        "--workspace",
        metavar="<workspace>",
        type=str,
        required=True,
        help="Workspace to add apps to",
    )
    add_parser.add_argument(
        "--apps",
        metavar="<apps>",
        type=str,
        required=True,
        help="Comma separated apps to add to the workspace",
    )

    args = parser.parse_args()

    match args.command:
        case "create":
            create_workspace(args)
        case "delete":
            delete_workspace(args)
        case "open":
            open_workspace(args)
        case "list":
            list_all_workspaces()
        case "add":
            add_apps_to_workspace(args)
        case default:
            print("Please provide a valid command")


if __name__ == "__main__":
    main()
