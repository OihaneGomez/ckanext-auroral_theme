import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint
import logging

log = logging.getLogger(__name__)

class AuroralThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IBlueprint)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'auroral_theme')

    def get_blueprint(self):
        log.info('AuroralThemePlugin: Registrando Blueprint /wiki')
        blueprint = Blueprint('auroral_theme', __name__,
                              template_folder='templates')

        @blueprint.route('/wiki')
        def wiki():
            return toolkit.render('wiki.html')

        return blueprint





        



