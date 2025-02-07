#!/usr/bin/env python3


class DefaultValues:
    SHODAN_API_KEY: str = "YOUR_DEFAULT_API_KEY"
    CENSYS_API_ID: str = "YOUR_CENSYS_API_ID"
    CENSYS_API_SECRET: str = "YOUR_CENSYS_API_SECRET"

    CENSYS_DEFAULT_RESULTS_QUANTITY: int = 100000
    CENSYS_FREE_PLAN_RESULTS_QUANTITY: int = 1000
    SHODAN_DEFAULT_RESULTS_QUANTITY: int = 100000

    QUERIES_FILE: str = "queries_test.json"
    MARKERS_DIRECTORY: str = "map"

    RESULTS_DIRECTORY: str = "results"
    JSON_RESULTS_DIRECTORY: str = "json"
    JSON_RESULTS_FILE: str = "all_results.json"
    CSV_RESULTS_DIRECTORY: str = "csv"
    CSV_RESULTS_FILE: str = "all_results.csv"
    TXT_RESULTS_DIRECTORY: str = "txt"
    TXT_RESULTS_FILE: str = "all_results.txt"

    CUSTOM_SCRIPTS_DIRECTORY: str = "custom_scripts"
    PY_SCRIPTS_DIRECTORY: str = "py_scripts"
    NSE_SCRIPTS_DIRECTORY: str = "nse_scripts"

    JSON_CONTINENTS_FILE: str = "continents.json"
    CSV_CONTINENTS_FILE: str = "continents.csv"
    TXT_CONTINENTS_FILE: str = "continents.txt"

    PNG_RESULTS_DIRECTORY: str = "png"
    PNG_ALL_RESULTS_DIRECTORY: str = "all_results"
    PNG_LIMITED_RESULTS_DIRECTORY: str = "limited_results"


class DefaultTlsParserValues:
    PARSED_RESULTS_DIR = "tls_processed_data"

    FULL_RESULTS_JSON = "tls_scanner_results.json"
    UNIQUE_ATTACKS_JSON = "tls_scanner_attacks.json"
    UNIQUE_BUGS_JSON = "tls_scanner_bugs.json"
    UNIQUE_VULNERABILITIES_JSON = "tls_scanner_vulnerabilities.json"

    FULL_RESULTS_CSV = "tls_scanner_results.csv"
    UNIQUE_ATTACKS_CSV = "tls_scanner_attacks.csv"
    UNIQUE_BUGS_CSV = "tls_scanner_bugs.csv"
    UNIQUE_VULNERABILITIES_CSV = "tls_scanner_vulnerabilities.csv"

    UNIQUE_GROUPPED_PRODUCTS_RESULTS_CSV = "tls_scanner_groupped.csv"


class DefaultTlsScannerValues:
    PRODUCT_LIMIT = 50
    LENGTH_OF_HOSTS_SUBGROUPS = 100
    NMAP_PING_SCAN_ARGS = "-n -sP"
    TLS_DETECTION_HOST_TIMEOUT = 180
    TLS_NMAP_WORKERS = 10
    TLS_SCANNER_REPORT_DETAIL = "NORMAL"
    TLS_SCANNER_SCAN_DETAIL = "NORMAL"
    TLS_SCANNER_PATH = "./TLS-Scanner/apps/TLS-Scanner.jar"
    TLS_SCANNER_THREADS = 4
    TLS_SCANNER_RESULTS_DIR = "tls"
    TLS_SCANNER_TIMEOUT = 1200


class DefaultVulnersScanValues:
    SUDO = False
    PORTS = None
    TOP_PORTS = None
    WORKERS = 10
    HOST_TIMEOUT = 120
    VULNERS_SCRIPT_PATH = "/plugins/vulners.nse"


class DefaultNmapScanValues:
    PORTS = None
    TOP_PORTS = None
    SUDO = False
    HOST_TIMEOUT = 30
    ARGUMENTS = "-Pn -T4 -A"
    WORKERS = 10


class DefaultProcessManagerValues:
    PORTS = None
    SUDO = False
    ARGUMENTS = "-Pn -A"
    WORKERS = 10


class DefaultPlotValues:
    PLOT_DEFAULT_AUTOPCT = "%1.1f%%"
    PLOT_LABEL_FONT_SIZE = 6
    PLOT_SUPTITLE_FONT_SIZE = 12
    PLOT_DPI = 200


class DefaultDatabaseValues:
    DB_NAME = "database.db"
