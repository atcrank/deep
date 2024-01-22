import os

import requests

"""
Use this URL list instead of manually downloading static files.
To run, you can invoke with `python3 pysrc/static/update_static.py`

I would have liked to find the equivalent of ":latest" for libraries

"""

STATIC_SOURCE = [
    "https://unpkg.com/htmx.org/dist/htmx.min.js",
    "https://unpkg.com/idiomorph@3.0",
    "https://unpkg.com/hyperscript.org@0.9.12",
    "https://code.jquery.com/jquery-3.7.0.min.js",
    "https://code.jquery.com/ui/1.13.2/jquery-ui.min.js",
    "https://code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css",
    "https://jqueryui.com/resources/demos/style.css",
]


def save_files_from_urls(l=STATIC_SOURCE):
    success = []
    fail = []
    for url in l:
        file_type = url.split(".")[-1]
        if file_type not in ["js", "css"]:
            file_type = "js"
        save_dir = f"./deep4/static/{file_type}"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        file_name = url.split("/")[-1]
        file_name.rstrip("@.0123456789")
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
