import os
import hashlib


root_repo_path = "C:\\Development\\GitHub\\embycon_kodi_repo\\repo"


def read_addon_xml(addon_path):
    addon_string = ""
    with open(addon_path, "r", encoding="utf-8") as f:
        for line in f:
            if "<?xml" not in line:
                addon_string += line
    return addon_string.strip()


def process_repo_dir(path):
    addons_list = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if name == "addon.xml":
                addons_list.append(os.path.join(root, name))
    return addons_list


def process_all_addons():
    addons_paths = []
    for root, dirs, files in os.walk(root_repo_path, topdown=False):
        for name in files:
            if name == "addons.xml":
                addons_paths.append(root)
    print(str(addons_paths))

    for path in addons_paths:
        addon_list = process_repo_dir(path)
        print(addon_list)

        addons_string = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n"
        addons_string +=  "<addons>\n"
        for addon_path in addon_list:
            addons_string += read_addon_xml(addon_path) + "\n"
        addons_string +=  "</addons>\n"
        #print(addons_string)
        with open(os.path.join(path, "addons.xml"), "w", encoding="utf-8") as f:
            f.write(addons_string)

        md5 = hashlib.md5(addons_string.encode("utf-8")).hexdigest()
        print(md5)
        with open(os.path.join(path, "addons.xml.md5"), "w", encoding="utf-8") as f:
            f.write(md5 + "  addons.xml\n")


process_all_addons()
