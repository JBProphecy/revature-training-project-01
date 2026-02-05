from project.core import convert_to_dataframe

class Config: pass

def test_csv_reader(temporary_path):
    config = Config()
    config.format = "csv"
    config.path = "data/tornado_usa.csv"
    config.field_map = {
    "yr": "year",
    "mo": "month",
    "dy": "day",
    "date": "date",
    "st": "state",
    "mag": "magnitude",
    "inj": "injury_count",
    "fat": "fatality_count",
    "slat": "latitude_start",
    "elat": "latitude_end",
    "slon": "longitude_start",
    "elon": "longitude_end",
    "len": "length_miles",
    "wid": "width_yards",
}

    df = convert_to_dataframe(config)
    print(df.head())

if __name__ == "__main__":
    test_csv_reader(None)