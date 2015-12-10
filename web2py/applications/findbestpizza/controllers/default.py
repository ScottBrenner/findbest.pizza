# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    return dict(message=T('Index'))


def map():
    return dict(message=T('Map'))


def info():
    pizzeria = db.pizzeria(request.args(0))
    review_list = db(db.review.parent==pizzeria).select()
    if auth.user:
        logIn = True
    else:
        logIn = False
    return dict(review_id=review_list, logIn=logIn, user_id=auth.user_id)


def add_review():
    db.review.insert(title=request.vars.title, description=request.vars.description, created_by=request.vars.user_id, parent=request.args(0))
    return "ok"


def update_review():
    row = db(db.review.id == request.vars.loc).select().first()
    row.update_record(title=request.vars.title)
    row.update_record(description=request.vars.description)
    return "ok"


def load_reviews():
    pizzeria = db.pizzeria(request.args(0))
    review_list = db(db.review.parent == pizzeria).select()
    p = {r.id: {'title': r.title, 'description': r.description, 'parent': r.parent, 'fromDB': r.fromDB,
                'created_by': r.pizzeria_creator}
         for r in review_list}
    return response.json(dict(review_dict=p))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


