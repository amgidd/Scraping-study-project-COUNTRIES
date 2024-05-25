This scraping  python project get data from the site and saves data in txt ot json format.

- config.py - URL of site
- main.py - start this, declaring which type of utput file you want to save(txt, json as str)
- get_response.py - uses requests (python lib) to get info from URL
- parse_response.py - uses BeautifulSoup (python lib) to parse data from get_response.py
- format_response.py - simple sort of results just for some consistency
- save_response.py - uses json(python lib), saves results as txt or json, depending of argument of save() function call in main

Project is divided into modules for study
No documentation and type hinting
