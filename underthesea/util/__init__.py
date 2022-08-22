from os import remove
from urllib.request import urlretrieve
from os.path import dirname, join, exists
from zipfile import ZipFile

components = [
    {
        "name": "classification.vntc.model",
        "url": "https://www.dropbox.com/sh/y3wtsw4v8x0z5ll/AADLpHIdUW9LD7WL5_CzslRKa?dl=1",
        "zip_destination": ["classification/vntc", "tc_svm_vntc_20190607.zip"],
        "model_destination": ["classification/vntc", "tc_svm_vntc_20190607"]
    }
]


def download_component(component_name):
    try:
        component = [component for component in components if
                     component["name"] == component_name][0]
        try:
            folder = dirname(dirname(__file__))
            zip_folder = join(folder, join(*component["zip_destination"]))
            model_folder = join(folder, join(*component["model_destination"]))
            if exists(model_folder):
                print(f"""Component '{component["name"]}' is already existed.""")
            else:
                print(f"""Start download component '{component["name"]}'""")
                print(zip_folder)
                download_file(component["url"], zip_folder)
                ZipFile(zip_folder).extractall(model_folder)
                remove(zip_folder)
                print(f"""Finish download component '{component["name"]}'""")
        except Exception as e:
            print(e)
            print(f"""Cannot download component '{component["name"]}'""")
    except Exception:
        message = f"Error: Component with name '{component_name}' does not exist."
        print(message)


def download_file(url, file_name):
    """ Cross platform file download helper function
    :param url: url of file
    :param file_name: destination file
    """
    urlretrieve(url, file_name)


pass
