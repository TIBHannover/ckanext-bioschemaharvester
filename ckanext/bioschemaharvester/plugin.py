import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.bioschemaharvester.harvester.bioschemascrap import BioSchemaMUController

from flask import Blueprint


class BioschemaharvesterPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.ITemplateHelpers)

    """
    Bioschema Sitemap scrapping and harvesting
    
    """

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('public/statics', 'ckanext-bioschemaharvester')

    # plugin Blueprint
    def get_blueprint(self):
        blueprint = Blueprint(self.name, self.__module__)
        blueprint.template_folder = u'templates'
        blueprint.add_url_rule(
            u'/bioschemaharvester/',
            u'_get_dataseturl',
            BioSchemaMUController._get_dataseturl,
            methods=['POST']
        )
        return blueprint

    # ITemplateHelpers

    def get_helpers(self):
       return {'_get_dataseturl': BioSchemaMUController._get_dataseturl}

