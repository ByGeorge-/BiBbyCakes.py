"""generates and appends to a bibtex file"""

def format(extra_string):
	"""
	Generates the file that has format for all entry types 
	Input: extra entries from book, article or in collection and adds to this 
	"""
	author_cite = "author = \"{0}\",\n".format(author)
    title_cite = "title = \"{0}\",\n".format(title)
    year_cite = "year = \"{0}\",\n".format(year)
    entry_type_cites = extra_string
    end_cite_entry = "}\n\n"

def article():
	journal = input("What is journal title? ")

	return "journal = \"{0}\",\n".format(journal)


def book():
	publisher = input("What is publisher title? ")

	return "publisher = \"{}\",\n".format(publisher)


def incollection():
	booktitle = input("what is book title? ")
	editors = input("What is editors?")
	publisher = input("what is publisher")
	pages = input("what is pages names")


	return "\nbooktitle = \"{0}\",\neditors = \"{1}\",\npublisher = \"{2}\",\npages = \"{3}\",\n".format(booktitle, editors, publisher, pages)
    


def make_bib():
	entry_type = "Please choose an entry type: article, book, incollection"

	ref_name = input("What is reference title? ")
	author = input("What is author? ")
	title = input("What is title? ")
	year = input("What is entry year? ")

	if entry_type.lower() == "article":
		add_this = article()
	elif entry_type.lower() == "book":
		add_this = book()
	elif entry_type.lower() == "incollection":
		add_this = incollection()

	your_bib = format(add_this)

	print(your_bib)
