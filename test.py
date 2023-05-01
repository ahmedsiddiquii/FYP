

from jinja2 import Environment, FileSystemLoader
import json

def generate(key,key_data):

    for form in key_data:
        print(form)
        break

    # Create the Jinja2 environment
    env = Environment(loader=FileSystemLoader("templates"))

    # Load the template
    template = env.get_template("form.html")

    # Render the template with a context

    context = {"table_name": form,"fields":key_data[form],"tables":key_data}
    print(context['fields'])
    print(len(context['fields']))
    rendered_template = template.render(context)
    with open(f"templates/{key}.html", "w", encoding="utf-8") as file:
        file.write(rendered_template)


# Open the file and load the JSON data
with open('data_list.txt', 'r') as f:
    data = json.load(f)

for i in data["hospitalManagement"]:
    for k in i:

        generate(k,i[k])




