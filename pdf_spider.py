import scrapy
from PyPDF2 import PdfReader
from io import BytesIO
import re
import json
from scrapy.crawler import CrawlerProcess

class PDFSpider(scrapy.Spider):
    name = 'pdf_spider'

    # Define the list of URLs
    start_urls = [
        #'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-006-2017.pdf',
        # Add more URLs as needed
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1718-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1885-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1255-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1535-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-006-2017.pdf',


        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1860-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-950-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-951-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-064-2016.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1731-2022.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1867-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-968-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2050-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1973-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-235-2016.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-056-04.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1867-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-968-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2050-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1973-2023.pdf',


        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-235-2016.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1215-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1890-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1631-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2115-2024.pdf',


        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-004-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1840-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1497-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTP-1857-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2094-2024.pdf',


        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2051-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2067-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1202-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1689-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-128-2016.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1456-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1222-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-2172-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-041-13.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TS-020-06.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2144-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1632-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1693-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1346-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2083-2024.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTP-1706-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTP-999-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1438-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTP-1656-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2116-2024.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2156-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2061-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1525-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-829-2018.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1981-2023.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1925-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-006-13.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1510-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1633-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2100-2024.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1717-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2164-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1365-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2055-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TG-025-09.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1483-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1454-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1522-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TS-003-12.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1368-2020.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1842-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-2173-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1634-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2101-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1256-2020.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1449-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TG-002-15.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2117-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1635-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1636-2022.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1526-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1872-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1769-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1637-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1968-2023.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2139-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1091-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1138-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2095-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-002-2017.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1532-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TG-012-10.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1430-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-973-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1473-2021.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2096-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1225-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1455-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1848-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2064-2024.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2114-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1477-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-546-2017.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTP-1657-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2091-2024.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1107-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1466-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-882-2018.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-2174-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1439-2021.pdf',


        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2052-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2048-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-981-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1979-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1306-2020.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTF-2124-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2106-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1136-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1674-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-753-2018.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2149-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1037-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TS-021-06.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1849-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1299-2020.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1366-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-970-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-2175-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1208-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2103-2024.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1685-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1638-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1843-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1959-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1448-2021.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1829-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2065-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-980-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-033-04.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1277-2020.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-977-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2056-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-042-04.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1707-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2090-2024.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1755-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2145-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1249-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1873-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2102-2024.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-003-13.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1543-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1139-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-965-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TG-005-10.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1305-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1475-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1639-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1453-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTF-708-2018.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1715-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1474-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1844-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2053-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1487-2021.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2108-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1205-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTP-1774-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1640-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1967-2023.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-974-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1732-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1527-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1240-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1850-2023.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-068-89.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1135-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTR-1410-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1129-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1268-2020.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1696-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TS-002-08.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1491-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TG-012-09.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2054-2024.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1641-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1267-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-971-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1845-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1969-2023.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1357-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TG-008-13.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1223-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TG-013-10.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/DIR-CPO-5002.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-039-12.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2118-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-975-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1531-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1661-2022.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1482-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-001-2017.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1874-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1642-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1516-2021.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-984-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1276-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TG-004-10.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-106-2016.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TM-001-99.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1691-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1686-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1911-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-982-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1099-2019.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1207-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1275-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2057-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1112-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-590-2017.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-053-09.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1811-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1274-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2107-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1768-2022.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1956-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTF-1217-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1841-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1066-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1509-2021.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-924-2018.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1437-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1790-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2097-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-985-2019.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1467-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-680-2018.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1643-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTP-1655-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1304-2020.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1861-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1270-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-978-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1875-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-2176-2024.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-001-2016.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-459-2017.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2058-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-976-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-994-2019.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2062-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2140-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1347-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2166-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1221-2020.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1862-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2022-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1644-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1547-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-025-11.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1450-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1447-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1134-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1851-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-044-12.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1852-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1876-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1863-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-005-14.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2047-2024.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1345-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1243-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1971-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-913-2018.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1666-2022.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1683-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2060-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1963-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1100-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTR-619-2017.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1864-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1733-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1521-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1476-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-026-11.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TG-004-09.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-938-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/TS-044-10.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2063-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1972-2023.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCPJMU5270.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1773-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2059-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1868-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1520-2021.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1966-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1065-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1452-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1757-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1390-2020.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2066-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1980-2023.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1408-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1108-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1468-2021.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1472-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1620-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1500-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1248-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/UCP-TG-008-10.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1645-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1092-2019.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-001-2018.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1519-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1499-2021.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2141-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1445-2021.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2165-2024.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-188-2016.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-070-2016.pdf',



        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1297-2020.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1646-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTG-1671-2022.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-003-2017.pdf',
        'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1341-2020.pdf',



       # 'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-2096-2024.pdf',
       # 'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1225-2020.pdf',
       # 'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1455-2021.pdf',
       # 'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-1848-2023.pdf',
       # 'https://secure.hosting.vt.edu/www.apps.vpfin.vt.edu/contracts/documents/VTS-006-2017.pdf',
    ]

    def parse(self, response):
        try:
            # Request the PDF content
            pdf_response = response.body
            pdf_content = BytesIO(pdf_response)

            # Extract fields from PDF content
            fields = self.extract_fields_from_pdf(pdf_content, response.url)

            # Output as JSON
            yield fields
        except Exception as e:
            self.logger.error(f"Error parsing PDF: {e}")

    def extract_fields_from_pdf(self, pdf_content, source_url):
        try:
            # Create PDF reader object
            pdf_reader = PdfReader(pdf_content)

            # Extract text from each page
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                text += pdf_reader.pages[page_num].extract_text()

            # Extracting values using regular expressions
            contract_type = self.extract_value(text, "STANDARD CONTRACT")
            title = self.extract_value(text, "SCOPE OF CONTRACT: (.+)")
            contract_number = self.extract_value(text, "Contract Number: (.+)")
            effective = self.extract_value(text, "PERIOD OF CONTRACT: From (.+) through (.+)")
            expiration = effective[1] if effective else ""
            effective = effective[0] if effective else ""
            renewals_allowed = self.extract_value(text, "OPTION FOR RENEWALS: (.+)")
            renewal_term = self.extract_value(text, "Option for four \(\d\) two-year renewals")
            supplier_contacts = self.extract_value(text, "FULL LEGAL NAME \(PRINT\)\s+\((.+)\)")
            buyer_contacts = self.extract_value(text, "FULL LEGAL NAME \(PRINT\)\s+\((.+)\)", index=1)

            return {
                'source_url': source_url,
                'contract_type': contract_type,
                'title': title,
                'contract_number': contract_number,
                'effective': effective,
                'expiration': expiration,
                'renewals_allowed': renewals_allowed,
                'renewal_term': renewal_term,
                'supplier_contacts': supplier_contacts,
                'buyer_contacts': buyer_contacts
            }
        except Exception as e:
            self.logger.error(f"Error extracting fields from PDF: {e}")
            return {}

    def extract_value(self, text, pattern, index=0):
        try:
            matches = re.findall(pattern, text, re.IGNORECASE)  # Ignore case for patterns
            if matches:
                return matches[index].strip()
            else:
                return ""
        except Exception as e:
            self.logger.error(f"Error extracting value from text: {e}")
            return ""

if __name__ == "__main__":
    output_file = "output.json"

    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': output_file
    })

    process.crawl(PDFSpider)
    process.start()

    # Load JSON data from file
    try:
        with open(output_file, 'r') as f:
            data = json.load(f)

        # Print the JSON data
        print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print("Output file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
