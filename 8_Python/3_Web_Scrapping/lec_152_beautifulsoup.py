"""
BeautifulSoap is used to analyze the HMTL files.

It is used for parsing the data.

"""

from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_title():
    h1_tag = simple_soup.find('h1')
    return h1_tag.string

def find_list_items():
    li_tag = simple_soup.find_all('li')
    list_content = [item.string for item in li_tag]
    return list_content

def find_subtitle():
    sub_title = simple_soup.find('p', {'class':'subtitle'})
    return sub_title.string

def find_other_para():
    paragraphs = simple_soup.find_all('p')
    only_para = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    # The empty list which is added in the attr is just for the paragraphs which does not have any class
    # so it will not give any error when it runs the loop.
    str_para = [sp.string for sp in only_para]
    return str_para

print(find_title())
print(find_list_items())
print(find_subtitle())
print(find_other_para())