#########################################################################
## Define your tables below; for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

from datetime import datetime

db.define_table('pizzeria',
                Field('name', required=True),
                Field('last_active', 'datetime'),
                )

db.define_table('review',
                Field('title', required=True),
                Field('description', 'text', required=True),
                Field('created_on', 'datetime'),
                Field('parent', 'reference pizzeria'),
                Field('created_by'),
                )

db.review.created_on.default = datetime.utcnow()
db.review.created_on.readable = False
db.review.parent.readable = False
db.review.created_on.writable = False
db.review.parent.writable = False
db.review.id.readable = False
db.review.id.writable = False
db.pizzeria.last_active.readable = False
db.pizzeria.last_active.writable = False
db.review.created_by.writable = False
db.review.created_by.readable = False
db.review.parent.on_delete = "SET NULL"