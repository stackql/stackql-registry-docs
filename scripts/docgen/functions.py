import os, sys, json, pandas as pd
from math import ceil
from provider_data import *
from pystackql import StackQL
iql = StackQL(exe="./stackql")

def make_web_safe(str):
    safe_str = str
    safe_str = safe_str.replace("<", "&lt;").replace(">", "&gt;")
    safe_str = safe_str.replace("{", "&#123;").replace("}", "&#125;")
    safe_str = safe_str.replace("\r\n", "<br />")
    safe_str = safe_str.replace("\n", "<br />")
    # TODO internal MD links
    return safe_str

def make_markdown_table_safe(str):
    return make_web_safe(str).replace("|", "\|")

def create_dir(dirName):
    print("creating directory %s..." % dirName)
    try:
        os.mkdir(dirName)
    except FileExistsError:
        print("ERROR: directory already exists")
        sys.exit(1)
    except:
        print("ERROR: unknown error")
        sys.exit(1)

def write_file(fileName, contents):
    print("writing file %s..." % fileName)
    file = open(fileName, "w")
    file.write(contents)
    file.close

def generate_front_matter(title, meta_description, description, image, keyword2=None, keyword3=None):
    if keyword2 is None and keyword3 is None:
        return """---
title: %s
hide_title: false
hide_table_of_contents: false
keywords:
  - %s
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: %s
custom_edit_url: null
image: %s
---
%s  
    
""" % (title, title, meta_description, image, description)
    elif keyword3 is None and keyword2 is not None:
        return """---
title: %s
hide_title: false
hide_table_of_contents: false
keywords:
  - %s
  - %s
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: %s
custom_edit_url: null
image: %s
---
%s  
    
""" % (title, title, keyword2, meta_description, image, description)
    else:
        return """---
title: %s
hide_title: false
hide_table_of_contents: false
keywords:
  - %s
  - %s
  - %s    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: %s
custom_edit_url: null
image: %s
---
%s  
    
""" % (title, title, keyword2, keyword3, meta_description, image, description)


def generate_see_also_links():
    return """
See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 
"""

def generate_installation_block(provider, version):
    return """
## Installation
```bash
REGISTRY PULL %s %s;
```
""" % (provider, version)

def generate_auth_block(provider):
    return """
## Authentication
```javascript
%s
```
### Example (Mac/Linux)
```bash
%s
```
### Example (PowerShell)
```powershell
%s
```
""" % (auth_blocks[provider]['auth'], auth_blocks[provider]['example']['linux'], auth_blocks[provider]['example']['windows'])

def generate_two_col_list(provider, list_of_objects, service_name=None):
    try:
        num_objects = list_of_objects.shape[0]
        first_col_len = ceil(num_objects/2.0)
        output = '<div class="row">\n'
        # col1
        output = output + '<div class="providerDocColumn">\n'
        for ix, this_obj in list_of_objects.iterrows():
            if service_name is None:
                link = create_html_link("/providers/%s/%s/" % (provider, this_obj["name"]), this_obj["name"])
            else:
                link = create_html_link("/providers/%s/%s/%s/" % (provider, service_name, this_obj["name"]), this_obj["name"])
            if ix < first_col_len:
                output = output + link + "<br />\n"
        output = output + '</div>\n'
        # col2
        output = output + '<div class="providerDocColumn">\n'
        for ix, this_obj in list_of_objects.iterrows():
            if service_name is None:
                link = create_html_link("/providers/%s/%s/" % (provider, this_obj["name"]), this_obj["name"])
            else:
                link = create_html_link("/providers/%s/%s/%s/" % (provider, service_name, this_obj["name"]), this_obj["name"])
            if ix >= first_col_len:
                output = output + link + "<br />\n"
        output = output + '</div>\n'
        output = output + '</div>\n'
        return output
    except:
        return '<div class="row"><div class="providerDocColumn">Not Available</div></div>'

def generate_service_overview(provider, serviceObj):
    return """
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>%s.%s</code></td></tr>
<tr><td><b>Type</b></td><td>Service</td></tr>
<tr><td><b>Title</b></td><td>%s</td></tr>
<tr><td><b>Description</b></td><td>%s</td></tr>
<tr><td><b>Id</b></td><td><code>%s</code></td></tr>
</tbody></table>

""" % (provider, serviceObj["name"], serviceObj["title"], make_web_safe(serviceObj["description"]), serviceObj["id"])


def generate_resource_overview(provider, serviceName, resourceObj):
    if (resourceObj["description"] == ""):
        # no description, dont display the column
        return """
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>%s</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>%s</code></td></tr>
</tbody></table>

""" % (resourceObj["name"], resourceObj["id"])
    else:
        return """
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>%s</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>%s</code></td></tr>
<tr><td><b>Description</b></td><td>%s</td></tr>
</tbody></table>

""" % (resourceObj["name"], resourceObj["id"], make_web_safe(resourceObj["description"]))

def generate_fields_table(fields):
    output = "## Fields\n"
    if fields.shape[0] > 1:
        if (fields["description"] == fields["description"][0]).all():
            output = output + "| Name | Datatype |\n"
            output = output + "|:-----|:---------|\n"
            for fieldIx, fieldRow in fields.iterrows():
                output = output + "| `%s` | `%s` |\n" % (fieldRow["name"], fieldRow["type"])
        else:
            output = output + "| Name | Datatype | Description |\n"
            output = output + "|:-----|:---------|:------------|\n"
            for fieldIx, fieldRow in fields.iterrows():
                output = output + "| `%s` | `%s` | %s |\n" % (fieldRow["name"], fieldRow["type"], make_markdown_table_safe(fieldRow["description"]))
    else:
        output = output + "`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  \n"
    return output

def generate_methods_table(methods):
    output = "## Methods\n"
    try:
        if (methods["description"] == methods["description"][0]).all():
            output = output + "| Name | Accessible by | Required Params |\n"
            output = output + "|:-----|:--------------|:----------------|\n"
            for methodIx, methodRow in methods.iterrows():
                if (methodRow["RequiredParams"] == ""):
                    output = output + "| `%s` | `%s` | %s |\n" % (methodRow["MethodName"], methodRow["SQLVerb"], methodRow["RequiredParams"])
                else:
                    output = output + "| `%s` | `%s` | `%s` |\n" % (methodRow["MethodName"], methodRow["SQLVerb"], methodRow["RequiredParams"])
        else:
            output = output + "| Name | Accessible by | Required Params | Description |\n"
            output = output + "|:-----|:--------------|:----------------|:------------|\n"
            for methodIx, methodRow in methods.iterrows():
                if (methodRow["RequiredParams"] == ""):
                    output = output + "| `%s` | `%s` | %s | %s |\n" % (methodRow["MethodName"], methodRow["SQLVerb"], methodRow["RequiredParams"], make_markdown_table_safe(methodRow["description"]))
                else:
                    output = output + "| `%s` | `%s` | `%s` | %s |\n" % (methodRow["MethodName"], methodRow["SQLVerb"], methodRow["RequiredParams"], make_markdown_table_safe(methodRow["description"]))
        return output
    except:
        output = output + "No methods available for the resource\n"
        return output


def run_stackql_query(query, retries):
    print("running %s..." % query)
    try:
        resp = iql.execute(query)
        resp_dict = json.loads(resp)
        return pd.DataFrame.from_dict(resp_dict)
    except:
        print("retrying [%s] (%s left)" % (query, retries))
        if retries > 0:
            return run_stackql_query(query, retries-1)
        else:
            print("ERROR [%s]" % query)
            return None

def create_html_link(url, title):
    return """<a href="%s">%s</a>""" % (url, title)