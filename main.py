from parse_links import get_all_collections, get_catalog
from parse_items import get_links, get_data


def main():
    get_all_collections()
    get_catalog()
    get_links()
    get_data()


if __name__ == "__main__":
    main()
