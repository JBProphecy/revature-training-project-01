from project.ingest import ingest_all

CONFIG_FILE_PATH = "config/wildfire_global.yaml"

def test_ingest_all():
    ingest_all()

if __name__ == "__main__":
    test_ingest_all()
