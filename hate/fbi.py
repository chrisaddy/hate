import tabula
import pandas as pd
import locale
from locale import atof

locale.setlocale(locale.LC_NUMERIC, "")

def read_table(path: str, page: int, table_num: int = 0) -> pd.DataFrame:
    return tabula.read_pdf(path, pages=page, stream=True)[table_num]


def thousands_to_int(col: pd.Series) -> pd.Series:
    return col.str.replace(",","").astype(int)


def number_of_agencies_by_population_group_96(fbi_96_path: str) -> dict:
    df = read_table(fbi_96_path, page=8, table_num=0).iloc[1:,:]

    df.columns = ["population_group", "participating_agencies", "population_covered"]
    df["participating_agencies"] = thousands_to_int(df["participating_agencies"])
    df["population_covered"] = thousands_to_int(df["population_covered"])

    return df


def number_of_incidencts_offenses_victims_offenders_by_bias_motivation_96(fbi_96_path: str) -> dict:
    return read_table(fbi_96_path, page=11, table_num=0)


def location_of_incidents_by_bias_motivation_96(fbi_96_path: str) -> dict:
    return read_table(fbi_96_path, page=12, table_num=0)

def number_of_offenses_victims_offenders_by_offense_96(fbi_96_path: str) -> dict:
    return read_table(fbi_96_path, page=13, table_num=0)
