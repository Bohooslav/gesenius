# import shutil
# import os
import localurls
# import urls
# import re
import urllib.request
for index, url in enumerate(localurls.urls):
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")
        # begin = html.find('id="content"') - 5
        # end = html.find('class="content_right">') - 28
        # text = html[begin:end]
        # print(text)
        # text = re.sub(r'<div class="crumbtrail">.*\n.*</h1>', '', text)
        # text = re.sub(r'view.cgi?n=\d', '', text)
        # text = text.replace('view.cgi?n=', '')
        # text = text.replace('#GHGpar', '.html#GHGpar')
        # text = "<html><head><title>Gesenius' Hebrew Grammar</title><link rel='stylesheet' type='text/css' href='style.css'><meta name = "viewport" content = "width=device-width, initial-scale=1.0, minimum-scale=1.0" ></head><body>" + text + "</body></html>"


        # arrows_index = html.find('</body>')
        # text = html[:arrows_index] + '<div class="arrows"><a href="' + str(index) + '.html" class="arrow" title="Prev"><svg class="arrow_prev" xmlns="http://www.w3.org/2000/svg" width="8" height="5" viewBox="0 0 8 5"><title>Prev</title><polygon points="4,3 1,0 0,1 4,5 8,1 7,0"></polygon></svg></a><a href="' + str(index + 2) + '.html" class="arrow" title="Next"><svg class="arrow_next" xmlns="http://www.w3.org/2000/svg" width="8" height="5" viewBox="0 0 8 5"><title>Next</title><polygon points="4,3 1,0 0,1 4,5 8,1 7,0"></polygon></svg></a></div>' + \
        #     html[arrows_index:]
        # print(text)






        ############ FILE PART #############
        # print(url)
        filename = url[7:] # for local files
        # filename = url[36:]
        # print(filename)
        f = open(filename, "w+")
        f.write(text)
        f.close()
        # old_path_to_file = "/home/b/imba/imba-electron-hello-world/" + filename
        # new_path_to_file = "/home/b/imba/imba-electron-hello-world/" + filename
        # shutil.move(old_path_to_file, new_path_to_file)
        # print(urls.urls)
        # print(html)
