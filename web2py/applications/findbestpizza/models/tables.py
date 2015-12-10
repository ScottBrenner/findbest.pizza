from datetime import datetime

db.define_table('review',
                Field('title', required=True),
                Field('description', 'text', required=True),
                Field('created_on', 'datetime'),
                Field('pizzeria', required=True),
                Field('created_by'),
                Field('first_name'),
                Field('last_name'),
                )

db.review.created_on.default = datetime.utcnow()
db.review.created_on.readable = False
db.review.pizzeria.readable = False
db.review.created_on.writable = False
db.review.pizzeria.writable = False
db.review.id.readable = False
db.review.id.writable = False
db.review.first_name.writable = False
db.review.first_name.readable = False
db.review.last_name.writable = False
db.review.last_name.readable = False
db.review.created_by.writable = False
db.review.created_by.readable = False
db.review.pizzeria.on_delete = "SET NULL"