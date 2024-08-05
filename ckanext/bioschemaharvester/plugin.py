import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class BioschemaharvesterPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    """
    BioSchema Sitemap scrapping and harvesting
    
    """

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('public/statics', 'ckanext-bioschemaharvester')

    # ITemplateHelpers

    def get_helpers(self):
        pass
