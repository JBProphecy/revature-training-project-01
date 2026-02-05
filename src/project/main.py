import logging
from project.utils._ingest import ingest


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    ingest("config/wildfire_global.yaml")
    ingest("config/tornado_usa.yaml")


if __name__ == "__main__":
    main()