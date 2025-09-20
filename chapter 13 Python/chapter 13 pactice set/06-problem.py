# Windows PowerShell
# Copyright (C) Microsoft Corporation. All rights reserved.

# Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

# PS C:\Users\user\Documents\Python\Python\chapter 13 Python\chapter 13 pactice set> python -m venv env1
# PS C:\Users\user\Documents\Python\Python\chapter 13 Python\chapter 13 pactice set> python -m venv env2
# PS C:\Users\user\Documents\Python\Python\chapter 13 Python\chapter 13 pactice set> .\env1\Script\activate.ps1
# .\env1\Script\activate.ps1 : The term '.\env1\Script\activate.ps1' is not recognized as the name of a cmdlet,
# function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the
# path is correct and try again.
# At line:1 char:1
# + .\env1\Script\activate.ps1
# + ~~~~~~~~~~~~~~~~~~~~~~~~~~
#     + CategoryInfo          : ObjectNotFound: (.\env1\Script\activate.ps1:String) [], CommandNotFoundException
#     + FullyQualifiedErrorId : CommandNotFoundException

# PS C:\Users\user\Documents\Python\Python\chapter 13 Python\chapter 13 pactice set> env1\Scripts\activate
# (env1) PS C:\Users\user\Documents\Python\Python\chapter 13 Python\chapter 13 pactice set> pip install pandas
# Collecting pandas
#   Using cached pandas-2.3.2-cp313-cp313-win_amd64.whl.metadata (19 kB)
# Collecting numpy>=1.26.0 (from pandas)
#   Using cached numpy-2.3.3-cp313-cp313-win_amd64.whl.metadata (60 kB)
# Collecting python-dateutil>=2.8.2 (from pandas)
#   Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
# Collecting pytz>=2020.1 (from pandas)
#   Using cached pytz-2025.2-py2.py3-none-any.whl.metadata (22 kB)
# Collecting tzdata>=2022.7 (from pandas)
#   Using cached tzdata-2025.2-py2.py3-none-any.whl.metadata (1.4 kB)
# Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
#   Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
# Using cached pandas-2.3.2-cp313-cp313-win_amd64.whl (11.0 MB)
# Using cached numpy-2.3.3-cp313-cp313-win_amd64.whl (12.8 MB)
# Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
# Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
# Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
# Using cached tzdata-2025.2-py2.py3-none-any.whl (347 kB)
# Installing collected packages: pytz, tzdata, six, numpy, python-dateutil, pandas
# Successfully installed numpy-2.3.3 pandas-2.3.2 python-dateutil-2.9.0.post0 pytz-2025.2 six-1.17.0 tzdata-2025.2

# [notice] A new release of pip is available: 25.1.1 -> 25.2
# [notice] To update, run: python.exe -m pip install --upgrade pip
# (env1) PS C:\Users\user\Documents\Python\Python\chapter 13 Python\chapter 13 pactice set> pip install pyjokes
# Collecting pyjokes
#   Using cached pyjokes-0.8.3-py3-none-any.whl.metadata (3.4 kB)
# Using cached pyjokes-0.8.3-py3-none-any.whl (47 kB)
# Installing collected packages: pyjokes
# Successfully installed pyjokes-0.8.3

# [notice] A new release of pip is available: 25.1.1 -> 25.2
# [notice] To update, run: python.exe -m pip install --upgrade pip
# (env1) PS C:\Users\user\Documents\Python\Python\chapter 13 Python\chapter 13 pactice set> pip freeze > requirments.txt
# (env1) PS C:\Users\user\Documents\Python\Python\chapter 13 Python\chapter 13 pactice set> deactivate
# PS C:\Users\user\Documents\Python\Python\chapter 13 Python\chapter 13 pactice set> env2/Scripts/activate
# (env2) PS C:\Users\user\Documents\Python\Python\chapter 13 Python\chapter 13 pactice set> pip install pyjokes
# Collecting pyjokes
#   Using cached pyjokes-0.8.3-py3-none-any.whl.metadata (3.4 kB)
# Using cached pyjokes-0.8.3-py3-none-any.whl (47 kB)
# Installing collected packages: pyjokes
# Successfully installed pyjokes-0.8.3

# [notice] A new release of pip is available: 25.1.1 -> 25.2
# [notice] To update, run: python.exe -m pip install --upgrade pip
# (env2) PS C:\Users\user\Documents\Python\Python\chapter 13 Python\chapter 13 pactice set> pip freeze >requirments2.txt
# (env2) PS C:\Users\user\Documents\Python\Python\chapter 13 Python\chapter 13 pactice set> deactivate
# PS C:\Users\user\Documents\Python\Python\chapter 13 Python\chapter 13 pactice set>