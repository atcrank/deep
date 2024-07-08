"""
Use this URL list instead of manually downloading static files.
To run, you can invoke with `python3 pysrc/static/update_static.py`

I would like to find the equivalent of dockers ":latest" tag for libraries

"""

import os

import requests

STATIC_SOURCE = [
    "https://unpkg.com/htmx.org/dist/htmx.min.js",
    "https://unpkg.com/htmx.org/dist/ext/ws.js",
    "https://unpkg.com/idiomorph",
    "https://unpkg.com/hyperscript.org",
    "https://code.jquery.com/jquery-3.7.0.min.js",
    "https://code.jquery.com/ui/1.13.2/jquery-ui.min.js",
    "https://code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css",
    "https://jqueryui.com/resources/demos/style.css",
    "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.3/js/bootstrap.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.2.3/css/bootstrap.min.css",
]


def save_files_from_urls(source_list=STATIC_SOURCE):
    success = []
    fail = []
    for url in source_list:
        file_type = url.split(".")[-1]
        if file_type not in ["js", "css"]:
            file_folder = "js"
            add_type = True
        else:
            file_folder = file_type
            add_type = False
        save_dir = f"./deep4/static/{file_folder}"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        file_name = url.split("/")[-1]
        file_name.rstrip("@.0123456789")
        if add_type:
            file_name = file_name + "." + file_folder
        save_path = os.path.join(save_dir, file_name)
        try:
            r = requests.get(url)
            with open(save_path, "wb") as f:
                f.write(r.content)
            success.append((url, save_path))
            print(f"Successfully downloaded {url} to {save_path}")
        except Exception as e:
            fail.append((url, save_path))
            print(f"Failed to download {url}", e)


if __name__ == "__main__":
    save_files_from_urls(STATIC_SOURCE)
