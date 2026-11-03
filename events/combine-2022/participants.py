"""Script to create markdown table from participants.

Download the registrants from: https://docs.google.com/spreadsheets/d/1ILZowd1K77Ulf8ITQMgkQOMy2YQgDLQRfdzfwxOVtVA/edit#gid=86280785
"""
from pathlib import Path

import pandas as pd


def read_df(tsv_path: Path) -> pd.DataFrame:
    """Reads dataframe from participant xlsx."""
    df = pd.read_csv(tsv_path, sep="\t")
    df.fillna('-', inplace=True)
    # print(df.columns)
    df.columns = ["timestamp", "email", "last_name", "first_name", "affiliation", "address", "dates", "communities", "projects", "share", "agreement"]
    df.sort_values(by=["last_name", "first_name"], inplace=True)
    print(df.to_string())
    return df


def create_attendee_md(df: pd.DataFrame) -> str:
    """Creates the markdown from attendee list."""

    lines = [
      "| Name | Affiliation | Attendance |",
      "|---|---|---|"
    ]

    for index, row in df.iterrows():
        name = f"{row['first_name'] + ' ' + row['last_name']}"
        affiliation = f"{row['affiliation']}"
        attendance =f"{row['dates']}<br/>{row['communities']}"
        line = f"| {name} | {affiliation} | {attendance} |"
        if row['share'] == "Yes":
            lines.append(line)

    return "\n".join(lines)


def create_attendee_list(df: pd.DataFrame) -> pd.DataFrame:
  """Creates the markdown from attendee list."""

  entries = []
  for index, row in df.iterrows():
    name = f"{row['last_name']}, {row['first_name']}"
    affiliation = f"{row['affiliation']}"
    # attendance = f"{row['dates']}<br/>{row['communities']}"
    entries.append({
      "Name": name,
      "Affiliation": affiliation,
      "Th 6th Oct": None,
      "Fr 7th Oct": None,
      "Sa 8th Oct": None,
      "Signature": None,
    })

  return pd.DataFrame(entries)


if __name__ == "__main__":
    tsv_path: Path = Path("/home/mkoenig/Downloads/Registration_COMBINE2022.tsv")
    xlsx_path: Path = Path("/home/mkoenig/Downloads/Registration_COMBINE2022.xlsx")

    df = read_df(tsv_path)
    md = create_attendee_md(df)
    print("-" * 80)
    print(md)
    print("-" * 80)

    print(f"{len(df)} participants have registered for COMBINE2022 so far.")

    with open("participants.md", "w") as f_md:
        f_md.write(md)

    # list for registration
    df_reg = create_attendee_list(df)
    df_reg.to_excel(xlsx_path, index=False)
