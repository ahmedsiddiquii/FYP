

from jinja2 import Environment, FileSystemLoader
import json

projectName = ""
keyList = []

def generate(key,key_data):
    global keyList
    template_bgColor = "white"
    template_headingColor = "black"
    template_sub_headingColor = "blue"
    template_dividerColor = "orange"
    navBar_bgColor = "orange"
    navBar_hColor = "black"
    navbarItemText_color = "black"
    template_buttonColors = "orange"
    for form in key_data:
        print("")
    # Create the Jinja2 environment
    env = Environment(loader=FileSystemLoader("templates"))
    # Load the template
    template = env.get_template("form.html")
    # Render the template with a context
    context = {
                  "projectname": projectName,
                  "key": key,
                  "keylist": keyList,
                  "table_name": form,
                  "fields": key_data[form],
                  "tables": key_data,
                  "bgColor": template_bgColor,
                  "headingColor": template_headingColor,
                  "sub_heading_color": template_sub_headingColor,
                  "dividerColor ": template_dividerColor,
                  "nvbgColor": navBar_bgColor,
                  "navhColor": navBar_hColor,
                  "navbarItemText_color": navbarItemText_color,
                  "template_buttonColors": template_buttonColors,}

    # print(context)
    print(len(context['fields']))
    rendered_template = template.render(context)
    with open(f"templates/{key}.html", "w", encoding="utf-8") as file:
        file.write(rendered_template)


# Open the file and load the JSON data
with open('data_list.txt', 'r') as f:
    data = json.load(f)

for i in data:
    projectName = i
    for j in data[i]:
        for k in j:
            print(k)
            keyList.append(k)

for l in data:
    for m in data[l]:
        print(m)
        for k in m:

            if True:
                generate(k, m[k])
            if False:
                # print(e)
                pass

#for i in data["hospitalManagement"]:


    #for k in i:

        #try:
            #generate(k,i[k])
        #except:
            #pass





