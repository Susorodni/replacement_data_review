import os
from tkinter import filedialog, messagebox
import pandas as pd
import zipfile
from replacement_data_review.services import asset_manager
from pandas.errors import (
    EmptyDataError,
    ParserError
)

SUPPORTED_FILE_EXTENSIONS = [
    "*.xls",
    "*.xlsx",
    "*.xlsm",
    "*.xlsb",
    "*.odf",
    "*.ods",
    "*.odt",
    "*.csv"
]

file_path: str = filedialog.askopenfilename(
    filetypes=[
        ("All supported filetypes", SUPPORTED_FILE_EXTENSIONS),
        ("Excel Files", SUPPORTED_FILE_EXTENSIONS[0:-1]),
        ("CSV Files", SUPPORTED_FILE_EXTENSIONS[-1])
    ]
)

# grabs the extension of the selected file to later check if it
# is a compatible filetype
ext = os.path.splitext(file_path)[1].lower()

# depending on the filetype, pandas has to read the file
# with different commands. If not compatible, an error is thrown.
try:
    if ext in [".xlsx", ".xls"]:
        df = pd.read_excel(file_path)
    elif ext == ".csv":
        df = pd.read_csv(file_path)
except FileNotFoundError as e:
    messagebox.showerror("File Not Found Error", str(e))
except PermissionError as e:
    messagebox.showerror("Permission Error", str(e))
except IsADirectoryError as e:
    messagebox.showerror("Is a Directory Error", str(e))
except UnicodeDecodeError as e:
    messagebox.showerror("Unicode Decode Error", str(e))
except EmptyDataError as e:
    messagebox.showerror("Empty Data Error Error", str(e))
except ParserError as e:
    messagebox.showerror("Parser Error", str(e))
except ValueError as e:
    messagebox.showerror("Value Error", str(e))
except ImportError as e:
    messagebox.showerror("Import Error", str(e))
except zipfile.BadZipFile as e:
    messagebox.showerror("Excel Corruption Error", str(e))
except OSError as e:
    messagebox.showerror("OS Error", str(e))

assets = asset_manager.build_assets(df)