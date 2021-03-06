# -*- coding: utf-8 -*-
from Products.CMFPlone.utils import safe_unicode
from plone import api


def checkProfile(event):
    """ Check Profile for User Loggedin event """
    portal = api.portal.get()
    currentId = event.principal.getId()
    if portal['members'].has_key(currentId):
        return
    else:
        currentUser = api.user.get(userid=currentId)
        with api.env.adopt_roles(['Manager']):
            api.content.create(
                type='Profile',
                id=currentId,
                title=currentUser.getProperty('fullname'),
                customCategories = api.portal.get_registry_record('hcd.content.browser.siteSetting.ISiteSetting.event'),
                container=portal['members'],
            )

