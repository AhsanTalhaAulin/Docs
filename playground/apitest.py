url = 'http://odoo.hww'
db = "odoo12"
username = 'admin'
password = 'hww@1234'
apikey = "8e8f5ec832d58e090f67799f38b830e6f9d54d1c"


from xml.etree.ElementTree import tostring
import xmlrpc.client
info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
url, db, username, password = info['host'], info['database'], info['user'], info['password']


common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

print(common.version())

uid = common.authenticate(db, username, password, {})
print("UID is " + str(uid) )


models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False})


# list_records = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
# print(list_records)

# list_records = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids], {'fields': ['name', 'country_id', 'comment']})
# print(list_records)

# list_records = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids], {'fields': ['name', 'country_id', 'comment']})
# print(list_records)

searchRead = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['id', '=', 14]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
print(searchRead)
# im = file_get_contents('asdf.jpg');
# imdata = str(base64.b64encode(im.encode("utf-8")),"utf-8");
# # Product creation
# product_id = models.execute_kw(db, uid, password, 'product.product', 'create', OrderedDict([(0,OrderedDict([('default_code',"test_default_code"),('name',"test_name"),('list_price',"100"),('image',imdata)]))]));

id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "New Partner"}])
print( str(id) + " created")