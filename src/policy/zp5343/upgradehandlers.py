import logging
from persistent.list import PersistentList
from Products.CMFCore.utils import getToolByName
from Products.LinguaPlone.browser.setup import SetupView


def setupLinguaFolders(site, logger):
    sw = SetupView(site, site.REQUEST)

    sw.folders = {}
    pl = getToolByName(site, "portal_languages")
    sw.languages = pl.getSupportedLanguages()
    if len(sw.languages) == 1:
        logger.error('Only one supported language configured.')
    sw.defaultLanguage = pl.getDefaultLanguage()
    available = pl.getAvailableLanguages()
    for language in sw.languages:
        info = available[language]
        sw.setUpLanguage(language, info.get('native', info.get('name')))

    sw.linkTranslations()
    sw.removePortalDefaultPage()
    sw.setupLanguageSwitcher()


def upgradeToPlone4(context):
    logger = logging.getLogger('policy.zp5343')

    site = getToolByName(context, 'portal_url').getPortalObject()

    news = site.news
    news.setExcludeFromNav(True)
    news.reindexObject()
  
    events = site.events
    events.setExcludeFromNav(True)
    events.reindexObject()

    Members = site.Members
    Members.setExcludeFromNav(True)
    Members.reindexObject()

    setupLinguaFolders(site, logger)

def upgradeToPlone4Cleanup(context):
    logger = logging.getLogger('policy.zp5343')

    site = getToolByName(context, 'portal_url').getPortalObject()

    del site.__annotations__['collective.recaptcha.settings.RecaptchaSettingsAnnotations']

    portal_transforms = getToolByName(context, 'portal_transforms')
    
    # no other way to remove transform when it is broken
    # because code was uninstalled.
    html_to_html = portal_transforms._mtmap['text/html']['text/html']
    html_to_html = [transform for transform in html_to_html if 'fck' not in transform.id]
    portal_transforms._mtmap['text/html']['text/html'] = PersistentList(html_to_html)
    
    portal_transforms._delObject('fck_ruid_to_url', suppress_events=True)
