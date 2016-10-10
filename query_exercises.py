import pg

db = pg.DB(dbname='restaurant_db')

query = db.query(' select * from restaurant')
print query

result_list = query.namedresult()
for result in result_list:
	print "The %s has a rating of %d stars." % (result.name, result.stars)

# inserting a new row of data
# adding a new restaurant called 'The Salty Pig'
# db.query("""insert into restaurant (name, distance, stars, category, favorite_dish, does_takeout, last_time_you_ate_there) values ('The Salthy Pig', 361, 4, 'American', 'Polenta Spin Rosso', FALSE, '2015-08-12')""")

# updating a new row of data
# now the restaurant, 'The Salty Pig', has a rating of 5 stars instead of 4
# db.query("""
# update restaurant set
#     stars = 5
# where
#     id = 8;
# """)

# deleting a row of data
# the restaurant we just create => 'The Salty Pig' is no longer in our table
# db.delete('restaurant', {'id': 8})
