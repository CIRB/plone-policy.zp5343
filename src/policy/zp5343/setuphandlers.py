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
    # if sw.previousDefaultPageId:
    #     sw.resetDefaultPage()
    sw.setupLanguageSwitcher()


def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.
    logger = context.getLogger('policy.zp5343')

    if context.readDataFile('policy.zp5343_various.txt') is None:
        return

    site = context.getSite()

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
    setup_tool = context.getSetupTool()
