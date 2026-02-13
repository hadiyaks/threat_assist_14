reporting_links = {
    "india": {
        "name": "National Cyber Crime Reporting Portal",
        "url": "https://cybercrime.gov.in/"
    },
    "usa": {
        "name": "FBI Internet Crime Complaint Center",
        "url": "https://www.ic3.gov/"
    }
}


def get_reporting_link(country):
    country = country.lower()
    return reporting_links.get(country, {
        "name": "Local Police Cybercrime Cell",
        "url": "https://www.google.com/search?q=cybercrime+report+portal"
    })
