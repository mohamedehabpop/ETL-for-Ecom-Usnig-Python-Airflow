import pandas as pd 
import requests
def run_sghut_ETL():
    API_url = 'https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651837'
    results = []
    # Extracting Data using the Hidden API 
    cookies = {
        'aka-cc': 'EG',
        'aka-ct': 'CAIRO',
        'aka-zp': '',
        'bm_sz': '9B1811068BF0DD724B53F5A6C0BA523C~YAAQbm04F04BnyGGAQAA/G8NKRLFlsRPRGT3QAoYPVFUxZ8sjP4DxNHNnl0E5TSuocKFyI4JHyGqbvYzFtLf0CmtrechA9evAw33hox1evt45l/cFztocsGsBoqU4TV7VLNLrW9TvJipXQvvwnbjzxq1PY2CKdUNhvyeKiZOYaRDrmO9RM2tw/ADF4sBBJ6iyAmiKbnnfxZGWtoEctqJaQcyWFhY7v9VZbDXdDLEq3UW9znZCrfDu7xZpLIyxbZ+87xIr09jsB5rHlYVrenSd4DEJHYRmTqCqOLASsJqabDfwoUpDgldMw==~3752755~4469298',
        'bm_mi': '2DDE776573A49696556A83529EDC9A78~YAAQbm04F2MDnyGGAQAAucgNKRJL/lK5hrWl9J+MXWVttmnME0uT8EeuYzIzvJMWrBM/NBrQkbzatqNRkLNrOnjFDdTbjYAWzQMX8Uf/f0k9hiziBf5uvPkeiFkYAL4Phh4pJpSSMx7Asw/CTbovCLTx4EIMQQ2jg0xrmN/nXph682qB7tMgUIBikOantYJY1RnacYUwI52F4j6ddEkgY7r7qJMz1UhRl1S1z6O4yXKgPMAqxSvUlLZ9oxwCmkzG3cRCIruyLj1yb6o4d0F74nsHCXHIKHMi6VYwGB4LKqpdA0z3Ro5fhsOha8MWh/knuaze~1',
        'rxVisitor': '1675726019584J7KHHMSR61L4FRI676MGIFRHGJ5HMNSE',
        'mt.v': '2.1449551936.1675726020221',
        'sgh-desktop-facet-state-search': '',
        'ftr_ncd': '6',
        '__wid': '144495777',
        'ak_bmsc': 'ACAF454EE7F640AC5DF399D921D4395E~000000000000000000000000000000~YAAQbm04FzcEnyGGAQAA3vANKRIPPtrA6sxdLvt2S2Bin+mPgHtM6XiWiQkT5lKqP2a/Tuabjx/HD+Nzwv5vzOonOHmvwW+4RFtZ9LXGMsrArRoseoEOvJj4SfPYdeWOQhTrCLs20d01oaCV1/Bz9RFzxx3JmdcqJ58Bgzd3KNHRLLmTj6jmu8loC6qgZdIKtUP2czu5/srCnR7bOSBH1VDqfd7wrbJcnO1eth6l90GPD+j5lcF/ORi9eCYX8M3804dAyKnUi0Hv7zCfDw3QhToKCWwedwKdjUtsicnQnpClT4pIMrOO15PzQA6Lb9j7yWBqHVXA8PHXhRNFIGtnDv2wPDRZwYcHZdyoSEfkXYbVNU6bqNltMljlZIjvjfaiPu4QKuiJaPfMi97lwvdUl7oLfmYR82SNmAxf5ues6mBtYmA=',
        'tealium_data2track_Tags_AdobeAnalytics_TrafficSourceMid_ThisHit': 'direct',
        'tealium_data_tags_adobeAnalytics_trafficSourceMid_thisSession': 'direct',
        'tealium_data_session_timeStamp': '1675726025472',
        'userToken': 'undefined',
        'TrafficSource_Override': '1',
        'tiktok_click_id': 'undefined',
        'dtPC': '-72$526027902_217h1vKGIRPRQRDGDWPWBVUPPBACKUNMJGKIWG-0e0',
        'dtLatC': '131',
        'dtSa': '-',
        'rxvt': '1675727828121|1675726019591',
        'SGPF': '3aBRAK1_1Yw_CWJ_R2Yi8FUasuRKssMfh1N8QabIAuawcme5XXvjyDA',
        'sgh-desktop-facet-state-plp': 'categoryid:undefined|gender:true|brands:partial|polarized:true|price:true|frame-shape:partial|color:true|face-shape:false|fit:false|materials:false|lens-treatment:false',
        'tealium_data2track_Tags_AdobeAnalytics_TrafficSourceJid_ThisHit': '302062REF',
        'tealium_data_tags_adobeAnalytics_trafficSourceJid_stackingInSession': '302061RES-302062REF',
        'AMCVS_125138B3527845350A490D4C%40AdobeOrg': '1',
        '_cs_mk': '0.8931457231310493_1675726030867',
        's_ecid': 'MCMID%7C65726101286083906843740582849603896268',
        'AMCV_125138B3527845350A490D4C%40AdobeOrg': '-1303530583%7CMCIDTS%7C19395%7CvVersion%7C3.3.0%7CMCMID%7C65726101286083906843740582849603896268%7CMCAAMLH-1676330830%7C6%7CMCAAMB-1676330830%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1675733230s%7CNONE%7CMCAID%7CNONE',
        's_cc': 'true',
        '_abck': '43D31B88BB131E1E7FEB6E6D7924AE97~0~YAAQbm04F4EEnyGGAQAAfAkOKQnBRx1mfFpPO03+5BDrxkbVZ3QsyJKDEG0socz9FiTLoGXZ3spb+G0Cd8+P9dr2BR4ZuX/2UMW58TdzsZ6PgmgyR68I6qnP/UoAecSXB0rUaEuLHUfXwpBUwWySqMOwTCnPeoeQaI7S6pUEULhlSr2p8BDBqf497FBlVGWOxHyDQ8KQO7zMigdvKEV8ddc8nyXMZW3IGNoNfTcb1+4Q9ttYuB5qZU1gbuFD88sHUa34qQqAhRr/QbXuPwhI1p5XXzwZreRjCDa27OfnFNXcl9VCo2fEFyJO8cSyz4jnYA3chxjEZMnIZww23bG3DZTdWTVaNFlMkdOP7UfxEOAzX41LNKaI/8WKQSbilB96YTeOHYF5sLf5J9PB0nEMf5QyfaF8TCgUzRKXzxs=~-1~||-1||~-1',
        'CONSENTMGR': 'consent:true%7Cts:1675726033612',
        'bounceClientVisit5415v': 'N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgO6kB0KArgHYDmYAhiinJQmQMYD2AtkZegI8AptRQBaKnUbNhKEABoQAJxghSxCjXpMWbTr0UgAligD6tLmZRyUxrtRgAzBmBtLTFiNdv3H0FzdhAF8gA',
        'UserTrackingProducts': '0',
        'dtCookie': 'v_4_srv_8_sn_SS92RM4PLP5OURJTT42ITEEV6TTHDTK3_app-3Ab359c07662f0b428_0_ol_0_perc_100000_mul_1',
        '__utma': '110589831.1136782806.1675726038.1675726038.1675726038.1',
        '__utmc': '110589831',
        '__utmz': '110589831.1675726038.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__utmt': '1',
        '__utmb': '110589831.1.10.1675726038',
        '_cs_c': '1',
        '_gcl_au': '1.1.1681274199.1675726038',
        '_uetsid': 'cc2fd780a67511eda6c86543fcb27827',
        '_uetvid': '4a8569803d9311ed987ce9a22cc31c1a',
        '_pin_unauth': 'dWlkPVpETmtNVEl6WTJZdE1tUTVZUzAwTVdFM0xUbG1PVGd0WW1Fd01EY3pOMlZoWkdVNA',
        '_scid': '0689851b-6969-4eab-a39f-784bafdaca0f',
        '_cs_cvars': '%7B%221%22%3A%5B%22Page%20Type%22%2C%22Plp%22%5D%2C%222%22%3A%5B%22Page%20Name%22%2C%22Men%3ASun%3APlp%22%5D%2C%223%22%3A%5B%22Page%20Section%201%22%2C%22Men%22%5D%2C%224%22%3A%5B%22Action%22%2C%22Men%3ASun%3APlp%22%5D%2C%228%22%3A%5B%22User%20Login%20Status%22%2C%22Guest%22%5D%7D',
        '_cs_id': '7845f8eb-5708-aac3-f5f0-8c64f7c25a87.1675726039.1.1675726039.1675726039.1.1709890039908',
        '_cs_s': '1.0.0.1675727839912',
        'cto_bundle': 'vfYJQF91ZVZvekliTnFZQ1pNUDNuOTclMkJwUHlUbkNVd2xSaFhVMHVFekVWSk16bXI1TmxHcmJoaXBIa3NUYzVaeXVpNW8welh2RjZZS09TSEZFRE1LamJtZldZWGI3VlM3NEYlMkZGQTByck4xWFpUMnhkbTFRNDVhJTJGNktmRk51Wld2ekdzMklxc1pYZkJ2dUN3cmxLTWtIVU9HU2clM0QlM0Q',
        'forterToken': '1fae876ee3d140479edc1f28184d1c7a_1675726028069__UDF43-mnf_6',
        '_sctr': '1|1675670400000',
        'outbrain_cid_fetch': 'true',
        'bm_sv': '446DAD8E9DE980985286F02709A5C421~YAAQbm04F28GnyGGAQAAQDwOKRKaRJom6SdD66z1uL7K2sJGOgdrjNvJYc8OGMPo+0sPGP5pYQrHUdyv9VUVsTKgwPpKlxAHs+XvxeJEM2lxpj2SMSMSSdDnrJXq4Py+eirsmeMal6LO7UW8/LXviDC13YKgx7FItZLLW8I1uO+3pw7iOwnRbHo5Kkr8JsN3BpVhPR4O83yFcx3UmCrLcGsQGqjzLZsuwTobgTl/ueddXNI4GboL3DVDNOgBQvsvJZNaXUs=~1',
        '_tt_enable_cookie': '1',
        '_ttp': 'RyVNcSzQVbYkoLu3WXyjYXGTrS1',
        '_fbp': 'fb.1.1675726044617.1431463011',
        'MGX_UC': 'JTdCJTIyTUdYX1AlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyM2EyZmI1YzQtOTQ1My00ZWFhLTkwYTYtMTMyMGIwNWEzZDk4JTIyJTJDJTIyZSUyMiUzQTE2NzYyNTE2Mzc2ODAlN0QlMkMlMjJNR1hfUFglMjIlM0ElN0IlMjJ2JTIyJTNBJTIyNDUxYzM5OWQtNGMxOC00ZDNmLTgxYzQtNzM3YzQ4MDBkN2E4JTIyJTJDJTIycyUyMiUzQXRydWUlMkMlMjJlJTIyJTNBMTY3NTcyNzg0NTgzMiU3RCUyQyUyMk1HWF9DSUQlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyOWY1NTYzNjYtZTdlMi00NTdhLWI1NjItYjhhZjhkMDY2OGMxJTIyJTJDJTIyZSUyMiUzQTE2NzYyNTE2Mzc2ODglN0QlMkMlMjJNR1hfVlMlMjIlM0ElN0IlMjJ2JTIyJTNBMSUyQyUyMnMlMjIlM0F0cnVlJTJDJTIyZSUyMiUzQTE2NzU3Mjc4NDU4MzIlN0QlMkMlMjJNR1hfRUlEJTIyJTNBJTdCJTIydiUyMiUzQSUyMm5zX3NlZ18wMDAlMjIlMkMlMjJzJTIyJTNBdHJ1ZSUyQyUyMmUlMjIlM0ExNjc1NzI3ODQ1ODMyJTdEJTdE',
        'utag_main': 'v_id:0186290df2d60024e62286be08ec0506f001c067007e8$_sn:1$_se:8$_ss:0$_st:1675727853103$ses_id:1675726025431%3Bexp-session$_pn:2%3Bexp-session$vapi_domain:sunglasshut.com$dc_visit:1$dc_event:1%3Bexp-session$dc_region:eu-central-1%3Bexp-session',
        'tealium_data_action_lastAction': 'Men:Sun:Plp click [:#][Loadmoresunglasses]',
        'tealium_data_action_lastEvent': 'click [:#][Loadmoresunglasses]',
    }

    headers = {
        'authority': 'www.sunglasshut.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'aka-cc=EG; aka-ct=CAIRO; aka-zp=; bm_sz=9B1811068BF0DD724B53F5A6C0BA523C~YAAQbm04F04BnyGGAQAA/G8NKRLFlsRPRGT3QAoYPVFUxZ8sjP4DxNHNnl0E5TSuocKFyI4JHyGqbvYzFtLf0CmtrechA9evAw33hox1evt45l/cFztocsGsBoqU4TV7VLNLrW9TvJipXQvvwnbjzxq1PY2CKdUNhvyeKiZOYaRDrmO9RM2tw/ADF4sBBJ6iyAmiKbnnfxZGWtoEctqJaQcyWFhY7v9VZbDXdDLEq3UW9znZCrfDu7xZpLIyxbZ+87xIr09jsB5rHlYVrenSd4DEJHYRmTqCqOLASsJqabDfwoUpDgldMw==~3752755~4469298; bm_mi=2DDE776573A49696556A83529EDC9A78~YAAQbm04F2MDnyGGAQAAucgNKRJL/lK5hrWl9J+MXWVttmnME0uT8EeuYzIzvJMWrBM/NBrQkbzatqNRkLNrOnjFDdTbjYAWzQMX8Uf/f0k9hiziBf5uvPkeiFkYAL4Phh4pJpSSMx7Asw/CTbovCLTx4EIMQQ2jg0xrmN/nXph682qB7tMgUIBikOantYJY1RnacYUwI52F4j6ddEkgY7r7qJMz1UhRl1S1z6O4yXKgPMAqxSvUlLZ9oxwCmkzG3cRCIruyLj1yb6o4d0F74nsHCXHIKHMi6VYwGB4LKqpdA0z3Ro5fhsOha8MWh/knuaze~1; rxVisitor=1675726019584J7KHHMSR61L4FRI676MGIFRHGJ5HMNSE; mt.v=2.1449551936.1675726020221; sgh-desktop-facet-state-search=; ftr_ncd=6; __wid=144495777; ak_bmsc=ACAF454EE7F640AC5DF399D921D4395E~000000000000000000000000000000~YAAQbm04FzcEnyGGAQAA3vANKRIPPtrA6sxdLvt2S2Bin+mPgHtM6XiWiQkT5lKqP2a/Tuabjx/HD+Nzwv5vzOonOHmvwW+4RFtZ9LXGMsrArRoseoEOvJj4SfPYdeWOQhTrCLs20d01oaCV1/Bz9RFzxx3JmdcqJ58Bgzd3KNHRLLmTj6jmu8loC6qgZdIKtUP2czu5/srCnR7bOSBH1VDqfd7wrbJcnO1eth6l90GPD+j5lcF/ORi9eCYX8M3804dAyKnUi0Hv7zCfDw3QhToKCWwedwKdjUtsicnQnpClT4pIMrOO15PzQA6Lb9j7yWBqHVXA8PHXhRNFIGtnDv2wPDRZwYcHZdyoSEfkXYbVNU6bqNltMljlZIjvjfaiPu4QKuiJaPfMi97lwvdUl7oLfmYR82SNmAxf5ues6mBtYmA=; tealium_data2track_Tags_AdobeAnalytics_TrafficSourceMid_ThisHit=direct; tealium_data_tags_adobeAnalytics_trafficSourceMid_thisSession=direct; tealium_data_session_timeStamp=1675726025472; userToken=undefined; TrafficSource_Override=1; tiktok_click_id=undefined; dtPC=-72$526027902_217h1vKGIRPRQRDGDWPWBVUPPBACKUNMJGKIWG-0e0; dtLatC=131; dtSa=-; rxvt=1675727828121|1675726019591; SGPF=3aBRAK1_1Yw_CWJ_R2Yi8FUasuRKssMfh1N8QabIAuawcme5XXvjyDA; sgh-desktop-facet-state-plp=categoryid:undefined|gender:true|brands:partial|polarized:true|price:true|frame-shape:partial|color:true|face-shape:false|fit:false|materials:false|lens-treatment:false; tealium_data2track_Tags_AdobeAnalytics_TrafficSourceJid_ThisHit=302062REF; tealium_data_tags_adobeAnalytics_trafficSourceJid_stackingInSession=302061RES-302062REF; AMCVS_125138B3527845350A490D4C%40AdobeOrg=1; _cs_mk=0.8931457231310493_1675726030867; s_ecid=MCMID%7C65726101286083906843740582849603896268; AMCV_125138B3527845350A490D4C%40AdobeOrg=-1303530583%7CMCIDTS%7C19395%7CvVersion%7C3.3.0%7CMCMID%7C65726101286083906843740582849603896268%7CMCAAMLH-1676330830%7C6%7CMCAAMB-1676330830%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1675733230s%7CNONE%7CMCAID%7CNONE; s_cc=true; _abck=43D31B88BB131E1E7FEB6E6D7924AE97~0~YAAQbm04F4EEnyGGAQAAfAkOKQnBRx1mfFpPO03+5BDrxkbVZ3QsyJKDEG0socz9FiTLoGXZ3spb+G0Cd8+P9dr2BR4ZuX/2UMW58TdzsZ6PgmgyR68I6qnP/UoAecSXB0rUaEuLHUfXwpBUwWySqMOwTCnPeoeQaI7S6pUEULhlSr2p8BDBqf497FBlVGWOxHyDQ8KQO7zMigdvKEV8ddc8nyXMZW3IGNoNfTcb1+4Q9ttYuB5qZU1gbuFD88sHUa34qQqAhRr/QbXuPwhI1p5XXzwZreRjCDa27OfnFNXcl9VCo2fEFyJO8cSyz4jnYA3chxjEZMnIZww23bG3DZTdWTVaNFlMkdOP7UfxEOAzX41LNKaI/8WKQSbilB96YTeOHYF5sLf5J9PB0nEMf5QyfaF8TCgUzRKXzxs=~-1~||-1||~-1; CONSENTMGR=consent:true%7Cts:1675726033612; bounceClientVisit5415v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgO6kB0KArgHYDmYAhiinJQmQMYD2AtkZegI8AptRQBaKnUbNhKEABoQAJxghSxCjXpMWbTr0UgAligD6tLmZRyUxrtRgAzBmBtLTFiNdv3H0FzdhAF8gA; UserTrackingProducts=0; dtCookie=v_4_srv_8_sn_SS92RM4PLP5OURJTT42ITEEV6TTHDTK3_app-3Ab359c07662f0b428_0_ol_0_perc_100000_mul_1; __utma=110589831.1136782806.1675726038.1675726038.1675726038.1; __utmc=110589831; __utmz=110589831.1675726038.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=110589831.1.10.1675726038; _cs_c=1; _gcl_au=1.1.1681274199.1675726038; _uetsid=cc2fd780a67511eda6c86543fcb27827; _uetvid=4a8569803d9311ed987ce9a22cc31c1a; _pin_unauth=dWlkPVpETmtNVEl6WTJZdE1tUTVZUzAwTVdFM0xUbG1PVGd0WW1Fd01EY3pOMlZoWkdVNA; _scid=0689851b-6969-4eab-a39f-784bafdaca0f; _cs_cvars=%7B%221%22%3A%5B%22Page%20Type%22%2C%22Plp%22%5D%2C%222%22%3A%5B%22Page%20Name%22%2C%22Men%3ASun%3APlp%22%5D%2C%223%22%3A%5B%22Page%20Section%201%22%2C%22Men%22%5D%2C%224%22%3A%5B%22Action%22%2C%22Men%3ASun%3APlp%22%5D%2C%228%22%3A%5B%22User%20Login%20Status%22%2C%22Guest%22%5D%7D; _cs_id=7845f8eb-5708-aac3-f5f0-8c64f7c25a87.1675726039.1.1675726039.1675726039.1.1709890039908; _cs_s=1.0.0.1675727839912; cto_bundle=vfYJQF91ZVZvekliTnFZQ1pNUDNuOTclMkJwUHlUbkNVd2xSaFhVMHVFekVWSk16bXI1TmxHcmJoaXBIa3NUYzVaeXVpNW8welh2RjZZS09TSEZFRE1LamJtZldZWGI3VlM3NEYlMkZGQTByck4xWFpUMnhkbTFRNDVhJTJGNktmRk51Wld2ekdzMklxc1pYZkJ2dUN3cmxLTWtIVU9HU2clM0QlM0Q; forterToken=1fae876ee3d140479edc1f28184d1c7a_1675726028069__UDF43-mnf_6; _sctr=1|1675670400000; outbrain_cid_fetch=true; bm_sv=446DAD8E9DE980985286F02709A5C421~YAAQbm04F28GnyGGAQAAQDwOKRKaRJom6SdD66z1uL7K2sJGOgdrjNvJYc8OGMPo+0sPGP5pYQrHUdyv9VUVsTKgwPpKlxAHs+XvxeJEM2lxpj2SMSMSSdDnrJXq4Py+eirsmeMal6LO7UW8/LXviDC13YKgx7FItZLLW8I1uO+3pw7iOwnRbHo5Kkr8JsN3BpVhPR4O83yFcx3UmCrLcGsQGqjzLZsuwTobgTl/ueddXNI4GboL3DVDNOgBQvsvJZNaXUs=~1; _tt_enable_cookie=1; _ttp=RyVNcSzQVbYkoLu3WXyjYXGTrS1; _fbp=fb.1.1675726044617.1431463011; MGX_UC=JTdCJTIyTUdYX1AlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyM2EyZmI1YzQtOTQ1My00ZWFhLTkwYTYtMTMyMGIwNWEzZDk4JTIyJTJDJTIyZSUyMiUzQTE2NzYyNTE2Mzc2ODAlN0QlMkMlMjJNR1hfUFglMjIlM0ElN0IlMjJ2JTIyJTNBJTIyNDUxYzM5OWQtNGMxOC00ZDNmLTgxYzQtNzM3YzQ4MDBkN2E4JTIyJTJDJTIycyUyMiUzQXRydWUlMkMlMjJlJTIyJTNBMTY3NTcyNzg0NTgzMiU3RCUyQyUyMk1HWF9DSUQlMjIlM0ElN0IlMjJ2JTIyJTNBJTIyOWY1NTYzNjYtZTdlMi00NTdhLWI1NjItYjhhZjhkMDY2OGMxJTIyJTJDJTIyZSUyMiUzQTE2NzYyNTE2Mzc2ODglN0QlMkMlMjJNR1hfVlMlMjIlM0ElN0IlMjJ2JTIyJTNBMSUyQyUyMnMlMjIlM0F0cnVlJTJDJTIyZSUyMiUzQTE2NzU3Mjc4NDU4MzIlN0QlMkMlMjJNR1hfRUlEJTIyJTNBJTdCJTIydiUyMiUzQSUyMm5zX3NlZ18wMDAlMjIlMkMlMjJzJTIyJTNBdHJ1ZSUyQyUyMmUlMjIlM0ExNjc1NzI3ODQ1ODMyJTdEJTdE; utag_main=v_id:0186290df2d60024e62286be08ec0506f001c067007e8$_sn:1$_se:8$_ss:0$_st:1675727853103$ses_id:1675726025431%3Bexp-session$_pn:2%3Bexp-session$vapi_domain:sunglasshut.com$dc_visit:1$dc_event:1%3Bexp-session$dc_region:eu-central-1%3Bexp-session; tealium_data_action_lastAction=Men:Sun:Plp click [:#][Loadmoresunglasses]; tealium_data_action_lastEvent=click [:#][Loadmoresunglasses]',
        'referer': 'https://www.sunglasshut.com/us/mens-sunglasses',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    params = {
        'isProductNeeded': 'true',
        'isChanelCategory': 'false',
        'pageSize': '50',
        'responseFormat': 'json',
        'currency': 'USD',
        'catalogId': '20602',
        'top': 'Y',
        'beginIndex': '0',
        'viewTaskName': 'CategoryDisplayView',
        'storeId': '10152',
        'langId': '-1',
        'categoryId': '3074457345626651837',
        'pageView': 'image',
        'orderBy': 'default',
        'currentPage': '2',
    }

    response = requests.get(
        API_url,
        params=params,
        cookies=cookies,
        headers=headers,
    )
    data = response.json()

    # Transforming Data
    for p in data['plpView']['products']['products']['product']:
        results.append(p)
    df = pd.json_normalize(results)
    df = df[['brand','name','modelName','listPrice','offerPrice']]
    df.rename(columns={'brand': 'Brand','name':'Name', 'modelName': 'Model Name','listPrice':'Price','offerPrice':'Offer Price'}, inplace=True)

    # Loading Data
    df.to_csv('sghut.csv', index = False, header = True)
