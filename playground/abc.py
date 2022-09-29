# # import json




# # kw = {
# #     "customer_email": "hoque.talha@gmail.com",
# #     "state": "sale",
# #     "order_line":
# #         [
# #             [
# #                 0,
# #                 0,
# #                 {
# #                     "default_code": "FURN_9001",
# #                     "product_uom_qty": 5
# #                 }
# #             ]
# #             ,
# #             [
# #                 0,
# #                 0,
# #                 {
# #                     "default_code": "FURN_9001",
# #                     "product_uom_qty": 3
# #                 }
# #             ]
# #         ]
# # }

# # kw.update({"customer_id": 83})
# # kw.pop("customer_email")

# # # kw["order_line"].update({"partner_id": 83})
# # i = 0
# # for product in kw["order_line"]:
# #     # product.update({"partner_id": 83})
# #     product[2].update({"product_id": i})
# #     product[2].pop("default_code")
# #     print(product[2])
# #     i += 1





# # # print(type(kw))

# # # print(type(json.dumps(kw)))


# # # kw["order_line"][0].update({[
# # #                 0,
# # #                 0,
# # #                 {
# # #                     "product_id": 27,
# # #                     "product_uom_qty": 3
# # #                 }
# # #             ]"})

# # # data_type = type(kw["order_line"])
# # # # print(data_type)

# # # data = [
# # #     0,
# # #     0,
# # #     {
# # #         "product_id": 27,
# # #         "product_uom_qty": 3
# # #     }
# # # ]


# # # kw["order_line"].append(data)
# # # kw["order_line"].append(data)

# # # for i in range(1, 5):
# # #     # print (i)
# # #     data[2]["product_id"] = i
# # #     # print(data)
# # #     kw["order_line"].append(data)
# # #     # print(kw["order_line"])


# # # print(kw["order_line"])


# # # kw = json.dumps(kw, indent=4)
# # # print(kw)


# # # print(kw["order_line"])
# # # print(kw["order_line"][0][2]["product_id"])
# # # print(kw['state'])


# # name = "ahsanul hoque"

# # size = len(name.split(" "))
# # fname = name.split(" ")[0]
# # lname = name.split(" ")[1]

# # print(size)
# # print(fname)
# # print(lname)

# # import json


# # kw1 = {
# #         "customer_email": "test@harriswebworks.com",
# #         "state": "sale",
# #         "order_line": [
# #             [
# #                 0,
# #                 0,
# #                 {
# #                     "default_code": "MS-Dime-M",
# #                     "product_uom_qty": 1
# #                 },
# #                 1,
# #                 0,
# #                 {
# #                     "default_code": "FURN_9001",
# #                     "product_uom_qty": 1
# #                 }
# #             ]
# #         ]
# #     }

# # print(type(kw1))

# # kw2 = kw1 - kw1

# # print( json.dumps(kw2, sort_keys=True, indent=4))

# # import deepdiff
# # import json

# # dict_1 = {
# #     "a": 1,
# #     "nested": {
# #         "b": 1,
# #     }
# # }

# # dict_2 = {
# #     "a": 2,
# #     "nested": {
# #         "b": 2,
# #     }
# # }

# # diff = deepdiff.DeepDiff(dict_1, dict_2)
# # print(json.dumps(diff, indent=4))


# response = [
#         {
#             "id": 83,
#             "is_seo_optimized": False,
#             "website_meta_title": False,
#             "website_meta_description": False,
#             "website_meta_keywords": False,
#             "website_meta_og_img": False,
#             "seo_name": False,
#             "website_id": False,
#             "website_published": False,
#             "is_published": False,
#             "can_publish": True,
#             "website_url": "/partners/ahsanulhoque-83",
#             "message_is_follower": False,
#             "message_follower_ids": [
#                 442
#             ],
#             "message_partner_ids": [],
#             "message_ids": [
#                 572
#             ],
#             "has_message": True,
#             "message_unread": False,
#             "message_unread_counter": 0,
#             "message_needaction": False,
#             "message_needaction_counter": 0,
#             "message_has_error": False,
#             "message_has_error_counter": 0,
#             "message_attachment_count": 0,
#             "message_main_attachment_id": False,
#             "website_message_ids": [],
#             "message_has_sms_error": False,
#             "email_normalized": "hoque.talha@gmail.com",
#             "is_blacklisted": False,
#             "message_bounce": 0,
#             "activity_ids": [],
#             "activity_state": False,
#             "activity_user_id": False,
#             "activity_type_id": False,
#             "activity_type_icon": False,
#             "activity_date_deadline": False,
#             "my_activity_date_deadline": False,
#             "activity_summary": False,
#             "activity_exception_decoration": False,
#             "activity_exception_icon": False,
#             "image_1920": False,
#             "image_1024": False,
#             "image_512": False,
#             "image_256": False,
#             "image_128": False,
#             "avatar_1920": "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",
#             "avatar_1024": "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",
#             "avatar_512": "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",
#             "avatar_256": "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",
#             "avatar_128": "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",
#             "name": "AhsanulHoque",
#             "display_name": "AhsanulHoque",
#             "date": False,
#             "title": False,
#             "parent_id": False,
#             "parent_name": False,
#             "child_ids": [],
#             "ref": False,
#             "lang": "en_US",
#             "active_lang_count": 1,
#             "tz": False,
#             "tz_offset": "+0000",
#             "user_id": False,
#             "vat": False,
#             "same_vat_partner_id": False,
#             "bank_ids": [],
#             "website": False,
#             "comment": "<p>{\"message\":\"A customer with the same email address already exists in an associated website.\",\"trace\":\"#0 \/var\/www\/testmage\/generated\/code\/Magento\/Customer\/Model\/AccountManagementApi\/Interceptor.php(104): Magento\\\\Customer\\\\Model\\\\AccountManagement-&gt;createAccountWithPasswordHash()\\n#1 \/var\/www\/testmage\/vendor\/magento\/module-customer\/Model\/AccountManagement.php(864): Magento\\\\Customer\\\\Model\\\\AccountManagementApi\\\\Interceptor-&gt;createAccountWithPasswordHash()\\n#2 \/var\/www\/testmage\/vendor\/magento\/module-customer\/Model\/AccountManagementApi.php(26): Magento\\\\Customer\\\\Model\\\\AccountManagement-&gt;createAccount()\\n#3 \/var\/www\/testmage\/generated\/code\/Magento\/Customer\/Model\/AccountManagementApi\/Interceptor.php(23): Magento\\\\Customer\\\\Model\\\\AccountManagementApi-&gt;createAccount()\\n#4 [internal function]: Magento\\\\Customer\\\\Model\\\\AccountManagementApi\\\\Interceptor-&gt;createAccount()\\n#5 \/var\/www\/testmage\/vendor\/magento\/module-webapi\/Controller\/Rest\/SynchronousRequestProcessor.php(95): call_user_func_array()\\n#6 \/var\/www\/testmage\/vendor\/magento\/module-webapi\/Controller\/Rest.php(188): Magento\\\\Webapi\\\\Controller\\\\Rest\\\\SynchronousRequestProcessor-&gt;process()\\n#7 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(58): Magento\\\\Webapi\\\\Controller\\\\Rest-&gt;dispatch()\\n#8 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(138): Magento\\\\Webapi\\\\Controller\\\\Rest\\\\Interceptor-&gt;___callParent()\\n#9 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(153): Magento\\\\Webapi\\\\Controller\\\\Rest\\\\Interceptor-&gt;Magento\\\\Framework\\\\Interception\\\\{closure}()\\n#10 \/var\/www\/testmage\/generated\/code\/Magento\/Webapi\/Controller\/Rest\/Interceptor.php(23): Magento\\\\Webapi\\\\Controller\\\\Rest\\\\Interceptor-&gt;___callPlugins()\\n#11 \/var\/www\/testmage\/vendor\/magento\/framework\/App\/Http.php(116): Magento\\\\Webapi\\\\Controller\\\\Rest\\\\Interceptor-&gt;dispatch()\\n#12 \/var\/www\/testmage\/generated\/code\/Magento\/Framework\/App\/Http\/Interceptor.php(23): Magento\\\\Framework\\\\App\\\\Http-&gt;launch()\\n#13 \/var\/www\/testmage\/vendor\/magento\/framework\/App\/Bootstrap.php(264): Magento\\\\Framework\\\\App\\\\Http\\\\Interceptor-&gt;launch()\\n#14 \/var\/www\/testmage\/pub\/index.php(30): Magento\\\\Framework\\\\App\\\\Bootstrap-&gt;run()\\n#15 {main}\"}</p>",
#             "category_id": [],
#             "credit_limit": 0.0,
#             "active": True,
#             "employee": False,
#             "function": False,
#             "type": "contact",
#             "street": False,
#             "street2": False,
#             "zip": False,
#             "city": False,
#             "state_id": False,
#             "country_id": False,
#             "country_code": False,
#             "partner_latitude": 0.0,
#             "partner_longitude": 0.0,
#             "email": "hoque.talha@gmail.com",
#             "email_formatted": "\"AhsanulHoque\" <hoque.talha@gmail.com>",
#             "phone": False,
#             "mobile": False,
#             "is_company": False,
#             "industry_id": False,
#             "company_type": "person",
#             "company_id": False,
#             "color": 0,
#             "user_ids": [],
#             "partner_share": True,
#             "contact_address": "\n\n  \n",
#             "commercial_partner_id": [
#                 83,
#                 "AhsanulHoque"
#             ],
#             "commercial_company_name": False,
#             "company_name": False,
#             "barcode": False,
#             "self": [
#                 83,
#                 "AhsanulHoque"
#             ],
#             "__last_update": "2022-08-22 08:09:29",
#             "create_uid": [
#                 4,
#                 "Public user"
#             ],
#             "create_date": "2022-08-03 10:43:09",
#             "write_uid": [
#                 4,
#                 "Public user"
#             ],
#             "write_date": "2022-08-22 08:09:29",
#             "im_status": "im_partner",
#             "channel_ids": [],
#             "signup_token": False,
#             "signup_type": False,
#             "signup_expiration": False,
#             "signup_valid": False,
#             "signup_url": False,
#             "employee_ids": [],
#             "employees_count": 0,
#             "property_product_pricelist": [
#                 1,
#                 "Public Pricelist (USD)"
#             ],
#             "team_id": False,
#             "partner_gid": 0,
#             "additional_info": False,
#             "phone_sanitized": False,
#             "phone_sanitized_blacklisted": False,
#             "phone_blacklisted": False,
#             "mobile_blacklisted": False,
#             "phone_mobile_search": False,
#             "credit": 0.0,
#             "debit": 0.0,
#             "debit_limit": 0.0,
#             "total_invoiced": 0.0,
#             "currency_id": [
#                 2,
#                 "USD"
#             ],
#             "journal_item_count": 0,
#             "property_account_payable_id": [
#                 14,
#                 "211000 Account Payable"
#             ],
#             "property_account_receivable_id": [
#                 6,
#                 "121000 Account Receivable"
#             ],
#             "property_account_position_id": False,
#             "property_payment_term_id": False,
#             "property_supplier_payment_term_id": False,
#             "ref_company_ids": [],
#             "has_unreconciled_entries": False,
#             "last_time_entries_checked": False,
#             "invoice_ids": [],
#             "contract_ids": [],
#             "bank_account_count": 0,
#             "trust": "normal",
#             "invoice_warn": "no-message",
#             "invoice_warn_msg": False,
#             "supplier_rank": 0,
#             "customer_rank": 0,
#             "property_stock_customer": [
#                 5,
#                 "Partner Locations/Customers"
#             ],
#             "property_stock_supplier": [
#                 4,
#                 "Partner Locations/Vendors"
#             ],
#             "picking_warn": "no-message",
#             "picking_warn_msg": False,
#             "visitor_ids": [],
#             "property_payment_method_id": False,
#             "payment_token_ids": [],
#             "payment_token_count": 0,
#             "website_description": False,
#             "website_short_description": False,
#             "sale_order_count": 41,
#             "sale_order_ids": [
#                 80,
#                 79,
#                 78,
#                 77,
#                 76,
#                 75,
#                 74,
#                 73,
#                 72,
#                 71,
#                 70,
#                 69,
#                 68,
#                 67,
#                 66,
#                 65,
#                 64,
#                 63,
#                 62,
#                 61,
#                 60,
#                 52,
#                 51,
#                 48,
#                 47,
#                 46,
#                 45,
#                 44,
#                 43,
#                 42,
#                 41,
#                 40,
#                 39,
#                 38,
#                 37,
#                 33,
#                 32,
#                 30,
#                 29,
#                 28,
#                 25
#             ],
#             "sale_warn": "no-message",
#             "sale_warn_msg": False
#         }
#     ]


# print(response[0]["id"])

from urllib import response


response =  {"message":"URL key for specified store already exists.","trace":"#0 \/var\/www\/testmage\/vendor\/magento\/module-url-rewrite\/Model\/Storage\/AbstractStorage.php(87): Magento\\UrlRewrite\\Model\\Storage\\DbStorage->doReplace()\n#1 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(58): Magento\\UrlRewrite\\Model\\Storage\\AbstractStorage->replace()\n#2 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(138): Magento\\UrlRewrite\\Model\\Storage\\DbStorage\\Interceptor->___callParent()\n#3 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(153): Magento\\UrlRewrite\\Model\\Storage\\DbStorage\\Interceptor->Magento\\Framework\\Interception\\{closure}()\n#4 \/var\/www\/testmage\/generated\/code\/Magento\/UrlRewrite\/Model\/Storage\/DbStorage\/Interceptor.php(50): Magento\\UrlRewrite\\Model\\Storage\\DbStorage\\Interceptor->___callPlugins()\n#5 \/var\/www\/testmage\/vendor\/magento\/module-catalog-url-rewrite\/Model\/Products\/AppendUrlRewritesToProducts.php(102): Magento\\UrlRewrite\\Model\\Storage\\DbStorage\\Interceptor->replace()\n#6 \/var\/www\/testmage\/vendor\/magento\/module-catalog-url-rewrite\/Observer\/ProductProcessUrlRewriteSavingObserver.php(85): Magento\\CatalogUrlRewrite\\Model\\Products\\AppendUrlRewritesToProducts->execute()\n#7 \/var\/www\/testmage\/vendor\/magento\/framework\/Event\/Invoker\/InvokerDefault.php(88): Magento\\CatalogUrlRewrite\\Observer\\ProductProcessUrlRewriteSavingObserver->execute()\n#8 \/var\/www\/testmage\/vendor\/magento\/framework\/Event\/Invoker\/InvokerDefault.php(74): Magento\\Framework\\Event\\Invoker\\InvokerDefault->_callObserverMethod()\n#9 \/var\/www\/testmage\/vendor\/magento\/framework\/Event\/Manager.php(66): Magento\\Framework\\Event\\Invoker\\InvokerDefault->dispatch()\n#10 \/var\/www\/testmage\/generated\/code\/Magento\/Framework\/Event\/Manager\/Proxy.php(95): Magento\\Framework\\Event\\Manager->dispatch()\n#11 \/var\/www\/testmage\/vendor\/magento\/framework\/Model\/AbstractModel.php(832): Magento\\Framework\\Event\\Manager\\Proxy->dispatch()\n#12 \/var\/www\/testmage\/vendor\/magento\/module-catalog\/Model\/Product.php(985): Magento\\Framework\\Model\\AbstractModel->afterSave()\n#13 \/var\/www\/testmage\/generated\/code\/Magento\/Catalog\/Model\/Product\/Interceptor.php(248): Magento\\Catalog\\Model\\Product->afterSave()\n#14 \/var\/www\/testmage\/vendor\/magento\/framework\/EntityManager\/Observer\/AfterEntitySave.php(34): Magento\\Catalog\\Model\\Product\\Interceptor->afterSave()\n#15 \/var\/www\/testmage\/vendor\/magento\/framework\/Event\/Invoker\/InvokerDefault.php(88): Magento\\Framework\\EntityManager\\Observer\\AfterEntitySave->execute()\n#16 \/var\/www\/testmage\/vendor\/magento\/framework\/Event\/Invoker\/InvokerDefault.php(74): Magento\\Framework\\Event\\Invoker\\InvokerDefault->_callObserverMethod()\n#17 \/var\/www\/testmage\/vendor\/magento\/framework\/Event\/Manager.php(66): Magento\\Framework\\Event\\Invoker\\InvokerDefault->dispatch()\n#18 \/var\/www\/testmage\/generated\/code\/Magento\/Framework\/Event\/Manager\/Proxy.php(95): Magento\\Framework\\Event\\Manager->dispatch()\n#19 \/var\/www\/testmage\/vendor\/magento\/framework\/EntityManager\/EventManager.php(51): Magento\\Framework\\Event\\Manager\\Proxy->dispatch()\n#20 \/var\/www\/testmage\/vendor\/magento\/framework\/EntityManager\/Operation\/Create.php(123): Magento\\Framework\\EntityManager\\EventManager->dispatchEntityEvent()\n#21 \/var\/www\/testmage\/vendor\/magento\/framework\/EntityManager\/EntityManager.php(106): Magento\\Framework\\EntityManager\\Operation\\Create->execute()\n#22 \/var\/www\/testmage\/vendor\/magento\/module-catalog\/Model\/ResourceModel\/Product.php(773): Magento\\Framework\\EntityManager\\EntityManager->save()\n#23 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(58): Magento\\Catalog\\Model\\ResourceModel\\Product->save()\n#24 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(138): Magento\\Catalog\\Model\\ResourceModel\\Product\\Interceptor->___callParent()\n#25 \/var\/www\/testmage\/vendor\/magento\/module-catalog-search\/Model\/Indexer\/Fulltext\/Plugin\/Product.php(58): Magento\\Catalog\\Model\\ResourceModel\\Product\\Interceptor->Magento\\Framework\\Interception\\{closure}()\n#26 \/var\/www\/testmage\/vendor\/magento\/module-catalog-search\/Model\/Indexer\/Fulltext\/Plugin\/Product.php(28): Magento\\CatalogSearch\\Model\\Indexer\\Fulltext\\Plugin\\Product->addCommitCallback()\n#27 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(135): Magento\\CatalogSearch\\Model\\Indexer\\Fulltext\\Plugin\\Product->aroundSave()\n#28 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(153): Magento\\Catalog\\Model\\ResourceModel\\Product\\Interceptor->Magento\\Framework\\Interception\\{closure}()\n#29 \/var\/www\/testmage\/generated\/code\/Magento\/Catalog\/Model\/ResourceModel\/Product\/Interceptor.php(194): Magento\\Catalog\\Model\\ResourceModel\\Product\\Interceptor->___callPlugins()\n#30 \/var\/www\/testmage\/vendor\/magento\/module-catalog\/Model\/ProductRepository.php(881): Magento\\Catalog\\Model\\ResourceModel\\Product\\Interceptor->save()\n#31 \/var\/www\/testmage\/vendor\/magento\/module-catalog\/Model\/ProductRepository.php(629): Magento\\Catalog\\Model\\ProductRepository->saveProduct()\n#32 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(58): Magento\\Catalog\\Model\\ProductRepository->save()\n#33 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(138): Magento\\Catalog\\Model\\ProductRepository\\Interceptor->___callParent()\n#34 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(153): Magento\\Catalog\\Model\\ProductRepository\\Interceptor->Magento\\Framework\\Interception\\{closure}()\n#35 \/var\/www\/testmage\/generated\/code\/Magento\/Catalog\/Model\/ProductRepository\/Interceptor.php(41): Magento\\Catalog\\Model\\ProductRepository\\Interceptor->___callPlugins()\n#36 [internal function]: Magento\\Catalog\\Model\\ProductRepository\\Interceptor->save()\n#37 \/var\/www\/testmage\/vendor\/magento\/module-webapi\/Controller\/Rest\/SynchronousRequestProcessor.php(95): call_user_func_array()\n#38 \/var\/www\/testmage\/vendor\/magento\/module-webapi\/Controller\/Rest.php(188): Magento\\Webapi\\Controller\\Rest\\SynchronousRequestProcessor->process()\n#39 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(58): Magento\\Webapi\\Controller\\Rest->dispatch()\n#40 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(138): Magento\\Webapi\\Controller\\Rest\\Interceptor->___callParent()\n#41 \/var\/www\/testmage\/vendor\/magento\/framework\/Interception\/Interceptor.php(153): Magento\\Webapi\\Controller\\Rest\\Interceptor->Magento\\Framework\\Interception\\{closure}()\n#42 \/var\/www\/testmage\/generated\/code\/Magento\/Webapi\/Controller\/Rest\/Interceptor.php(23): Magento\\Webapi\\Controller\\Rest\\Interceptor->___callPlugins()\n#43 \/var\/www\/testmage\/vendor\/magento\/framework\/App\/Http.php(116): Magento\\Webapi\\Controller\\Rest\\Interceptor->dispatch()\n#44 \/var\/www\/testmage\/generated\/code\/Magento\/Framework\/App\/Http\/Interceptor.php(23): Magento\\Framework\\App\\Http->launch()\n#45 \/var\/www\/testmage\/vendor\/magento\/framework\/App\/Bootstrap.php(264): Magento\\Framework\\App\\Http\\Interceptor->launch()\n#46 \/var\/www\/testmage\/pub\/index.php(30): Magento\\Framework\\App\\Bootstrap->run()\n#47 {main}"}

print(type(response))
print(response["message"])