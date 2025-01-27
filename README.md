一些工具 & CSL 以符合碩論style

# Workflow

1. Download all Bibtex from Semantic Scholar.
    - Using semantic scholar will make sure necessary fields are filled/present.
2. Run the cleanup python script.
    - Clean up the year, container abbr. (Because CSL can't modify field value)
3. Import into Mendeley/Zotero
    - Merge with some existing items(which is not available on Semantic Scholar) in your library.
4. Use Mendely/Zotero word plugin to insert cite/bib. .
5. Change the citation style.
    - With given custom CSL file/URL.
    - The current [master_essay.csl](https://csl.mendeley.com/styles/755707591/ieee)

# Resources

1. [Mendeley CSL editor](https://csl.mendeley.com/visualEditor/)
2. [Mendeley CSL validator](https://validator.citationstyles.org/)
3. [CSL spec docs](https://docs.citationstyles.org/en/stable/specification.html#toc-entry-89)
4. [bibtexparser docs](https://bibtexparser.readthedocs.io/en/main/bibtexparser.html)