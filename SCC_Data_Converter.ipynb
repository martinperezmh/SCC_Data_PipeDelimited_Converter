{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ac3ebe8-e99d-4644-9944-74a533b71a0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.2.2\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# Purpose: Convert Sober data XLSX to a .TXT file (pipe-delimited), remove trailing zeros, export to local folder\n",
    "# Handles column names in a case-insensitive manner.\n",
    "\n",
    "import pandas as pd\n",
    "from datetime import datetime\n",
    "import os\n",
    "\n",
    "print(pd.__version__)\n",
    "\n",
    "# Prompt for Excel file name with error handling\n",
    "data = input('Enter Excel File Name (.xlsx): ').strip()\n",
    "\n",
    "try:\n",
    "    # Ensure .xlsx extension (case-insensitive)\n",
    "    if not data.lower().endswith('.xlsx'):\n",
    "        data += '.xlsx'\n",
    "    \n",
    "    # Load Excel file into DataFrame\n",
    "    df = pd.read_excel(data)\n",
    "    \n",
    "    # Normalize column names to lowercase for case-insensitive operations\n",
    "    df.columns = df.columns.str.lower()\n",
    "    \n",
    "    # Print shape and preview\n",
    "    print(f'DataFrame Shape: {df.shape}')\n",
    "    print(f'Sample Rows:\\n{df.head(3)}')\n",
    "\n",
    "except FileNotFoundError:\n",
    "    print(f\"Error: File '{data}' not found. Please check the file name and path.\")\n",
    "    exit()\n",
    "except ValueError as e:\n",
    "    print(f\"Error reading Excel file: {e}\")\n",
    "    exit()\n",
    "\n",
    "# Fill NaN values in 'address2' (case-insensitive)\n",
    "if 'address2' in df.columns:\n",
    "    df['address2'] = df['address2'].where(pd.notnull(df['address2']), None)\n",
    "\n",
    "# Remove trailing zeros from 'patientvmcmrn' (case-insensitive)\n",
    "if 'patientvmcmrn' in df.columns:\n",
    "    df['patientvmcmrn'] = df['patientvmcmrn'].fillna('').apply(\n",
    "        lambda x: str(int(x)) if str(x).strip() != '' else ''\n",
    "    )\n",
    "\n",
    "# Show the processed 'patientvmcmrn' if it exists\n",
    "if 'patientvmcmrn' in df.columns:\n",
    "    print(df['patientvmcmrn'].head())\n",
    "\n",
    "# Get the current date in YYYYMMDD format\n",
    "current_date = datetime.now().strftime('%Y%m%d')\n",
    "export_file = f'CalAim_SoberingCenter_{current_date}.TXT'\n",
    "print(f'Exporting: {export_file}')\n",
    "\n",
    "# Export to a pipe-delimited file without quoting\n",
    "df.to_csv(export_file, sep='|', index=False, quoting=3, encoding='utf-8')\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
