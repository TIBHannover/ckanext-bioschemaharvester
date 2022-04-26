[![Tests](https://github.com/TIB/ckanext-bioschemaharvester/workflows/Tests/badge.svg?branch=main)](https://github.com/TIB/ckanext-bioschemaharvester/actions)

# ckanext-bioschemaharvester

This plug-in is an extension to CKAN Harvester to harvest (bio)schema  datasets from repositories using (bio)schema. Example: [MassBank Repo](https://massbank.eu/MassBank/)

This harvester is developed using the offical CKAN Harvester https://github.com/ckan/ckanext-harvest 
following the actual Harvest Interface of gather, fetch and import techniques. 

When installed, you can see an option to use as `BioSchema Scrapper/Harvest`

![Screenshot from 2022-04-26 13-55-13](https://user-images.githubusercontent.com/70484813/165295076-874351a5-1086-477c-8b67-997992dafb5d.png)


As name suggests, this harvester is more of a web-scrapper. It is developed using Beautiful scoop to harvest/fetch metadata from HTML page of the dataset (tested only on MassBank Repo)

Note: This plugin uses migrated tables from other plugin to store metadata  to desired metadata tables without overwriting default ckan tables in the database. So, see that you already have these tables in your ckan instance.

- https://github.com/bhavin2897/ckanext-rdkit-visuals
- https://github.com/bhavin2897/ckanext-related_resources


## Requirements

If your extension works across different versions you can add the following table:

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.8 & eariler   | not tested    |
| 2.9             | yes           |


## Installation

To install ckanext-bioschemaharvester:

Activate your CKAN virtual environment, for example:

     . /usr/lib/ckan/default/bin/activate

Clone the source and install it on the virtualenv

    git clone https://github.com/bhavin2897/ckanext-bioschemaharvester.git
    cd ckanext-bioschemaharvester
    pip install -e .
	pip install -r requirements.txt

Add `bioschemaharvester` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload


## Developer installation

To install ckanext-bioschemaharvester for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/TIB/ckanext-bioschemaharvester.git
    cd ckanext-bioschemaharvester
    python setup.py develop
    pip install -r requirements.txt
    
Restart Server if you are using Supervisor and Nginx

	sudo service supervisor reload
	sudo service nginx reload


## Harvesting 

NOTE: Before installing and harvesting, it is assummed that you already have installed 
- [CKAN Harvester](https://github.com/ckan/ckanext-harvest)   
- [RDKit Visuals](https://github.com/bhavin2897/ckanext-rdkit-visuals)
- [Related Resources](https://github.com/bhavin2897/ckanext-related_resources)

The harvest Source CAN be a Sitemap, Sitemaps or single web page, containing bioschema in JSON-LD format and available to scrap.
Source Example: https://massbank.eu/MassBank/sitemapindex.xml

No need to add any information to the configuartion text.

Choose Bioschema Scrapper/Harvester 

Save  

Run Harvester `ckan -c /etc/ckan/default/ckan.ini harvester run`, if you running on development/production server. 

Else if you are running locally, follow regular hravetsing process. 

	ckan -c /etc/ckan/default/ckan.ini harvester gather-consumer
	
	ckan -c /etc/ckan/default/ckan.ini harvester fetch-consumer
	
	ckan -c /etc/ckan/default/ckan.ini harvester run

## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-bioschemaharvester

If ckanext-bioschemaharvester should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
