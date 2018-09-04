import os.path as op

raw_file = op.join(op.dirname(__file__), 'raw_pubs.txt')
out_file = op.join(op.dirname(__file__), 'html_pubs.txt')

with open(raw_file) as f:
    pub_list = f.readlines()

pub_list = [x.replace('“', '"').replace('”', '"').split('"')
            for x in pub_list]

pub_docs = []
for pub in pub_list:
    authors = pub[0].split(sep=' ', maxsplit=1)[1]
    title = pub[1]

    # some posts (especially new ones) may not have the same
    # journal and year formatting
    journal = ''
    year = ''
    if len(pub[2].split(',')) > 2:
        journal = pub[2].split(',')[1].strip()
        year = pub[2].split(',')[2].strip()[:4]
    doc = {'authors': authors,
           'title': title,
           'journal': journal,
           'year': year}

    pub_docs.append(doc)

year_dict = {str(year): '<ul  class="pubs">\n'
              for year in range(2018, 2004, -1)}

year_dict['missing_year'] = '<ul  class="pubs">\n'

for pub_doc in pub_docs:
    pub_string = f'    <li>\n' \
                 f'        <a href="#">{pub_doc["title"]}</a>\n' \
                 f'        <authors>{pub_doc["authors"]}</authors>\n' \
                 f'        <journal>{pub_doc["journal"]}</journal>\n' \
                 f'    </li>\n'

    if pub_doc['year'] not in year_dict:
        year_dict['missing_year'] += pub_string
        continue

    year_dict[pub_doc['year']] += pub_string

out_string = ''
for key, value in year_dict.items():
    out_string += key + '\n' + value + '</ul>\n'

with open(out_file, 'w') as fout:
    print(out_string, file=fout)
