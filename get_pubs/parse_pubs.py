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
    if len(pub[2].split(',')) > 1:
        journal = pub[2].split(',')[0].strip()
        year = pub[2].split(',')[1].strip()
    doc = {'authors': authors,
           'title': title,
           'journal': journal,
           'year': year}

    pub_docs.append(doc)

out_string = ''
for pub_doc in pub_docs:
    if len(pub_doc["journal"]) < 1:
        pub_doc["journal"] = pub_doc["year"]
        pub_doc["year"] = ''

    pub_string = f'<li>\n' \
                 f'    <a href="#">{pub_doc["title"]}<a/>\n' \
                 f'    <authors>{pub_doc["authors"]}</authors>\n' \
                 f'    <journal>{pub_doc["journal"]}</journal>, ' \
                 f'{pub_doc["year"]}\n' \
                 f'</li>\n'
    out_string += pub_string

with open(out_file, 'w') as fout:
    print(out_string, file=fout)

print('lol')
