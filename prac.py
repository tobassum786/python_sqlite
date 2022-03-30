import database

#  add Multi data in database
# add_users = [
# 				('huzain', 'ida', 'huzain@ida.com', '20'),
# 				('munail', 'vila', 'munail@vila.com', '30'),
# 				('vitlo', 'vinga', 'vitlo@vinga.com', '22')
# 		]


# database.add_data(add_users)


#  Add Only one Entry

database.add_one("wila", "bibo", "wila@bibo.com", "44")

database.delete_one('3')

database.ahow_all()