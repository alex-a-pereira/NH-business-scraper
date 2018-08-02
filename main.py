from bs4 import BeautifulSoup
import requests
from pprint import pprint
url = "https://quickstart.sos.nh.gov/online/BusinessInquire/BusinessInformation?businessID=621550"
soup = BeautifulSoup(open("webpages/QuickStart.htm"), "html.parser")


def append_with_purposes(purpose_html, dictionary):
    def purposes_to_string(purposes):
        purposes_enum = list(enumerate(purposes, start=1))
        enum_to_list = ['Purpose ' + str(x[0]) + ': ' + x[1] for x in purposes_enum]
        list_to_string = ' '.join(enum_to_list)
        return list_to_string

    def clean_purpose_list(list_of_purposes):
        for item in list(list_of_purposes):
            if item.isdigit():
                list_of_purposes.remove(item)

    purpose_list = list(map(lambda x: x.attrs['value'], purpose_html))
    clean_purpose_list(purpose_list)
    string_of_purposes = purposes_to_string(purpose_list)

    dictionary['Principal Purpose:'] = string_of_purposes


def append_with_data_panel(data_html, dictionary):
    def get_string(tag):
        try:
            tag_string = tag.string
        except AttributeError:
            tag_string = "N/A"

        if tag_string and '\xa0' in tag_string:
            tag_string = tag_string.replace('\xa0', ' ')
        return tag_string

    def get_row_content(row_label):
        row_content = row_label.find_next_sibling("td")
        potential_span = row_content.find("span")
        if potential_span:
            row_content = row_content.span
        return row_content

    def determine_if_blank(label_string):
        if not label_string or label_string == ' ':
            return 1

    info_labels = data_html.find_all(attrs={"align": "right"})
    for label in info_labels:
        label_str = get_string(label)
        if determine_if_blank(label_str):
            continue
        content = get_row_content(label)
        dictionary[label_str] = get_string(content)


def assemble_business_dict(html):
    bus_dict = {}

    parsed_data_panel = html.find(attrs={"class": "data_pannel"})  # typo of panel is in HTML
    append_with_data_panel(parsed_data_panel, bus_dict)
    parsed_purposes = html.find_all(attrs={"name": "SelectedAgentBAdd"})
    append_with_purposes(parsed_purposes, bus_dict)

    return bus_dict