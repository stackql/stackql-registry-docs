import os, sys, json, pandas as pd
from math import ceil
from provider_data import *

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
        # provider level
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
id: %s-doc
slug: /providers/%s
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

%s  
    
""" % (title, title, meta_description, image, title, title, description)

    elif keyword3 is None and keyword2 is not None:
        # service level
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
        # resource level
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

%s

""" % (title, title, keyword2, keyword3, meta_description, image, description)


def generate_see_also_links():
    return """
See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 
"""

def generate_installation_block(provider):
    return """
## Installation

To pull the latest version of the `%s` provider, run the following command:  

```bash
REGISTRY PULL %s;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  
""" % (provider, provider)

def generate_auth_block(provider):
    if auth_blocks[provider]['custom']:
        return generate_custom_auth_block(provider)
    else:
        return generate_standard_auth_block(provider)        

def generate_standard_auth_block(provider):
    return """
## Authentication

The following system environment variables are used for authentication by default:  
%s
These variables are sourced at runtime (from the local machine or as CI variables/secrets).  

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:  

```bash
%s
```
or using PowerShell:  

```powershell
%s
```
</details>

""" % (auth_blocks[provider]['variables'], auth_blocks[provider]['linux'], auth_blocks[provider]['windows'])

def generate_custom_auth_block(provider):
    return """
## Authentication

%s
""" % (auth_blocks[provider]['custom_markdown'])

def generate_server_variables_block(provider):
    return """
## Server Parameters

%s
""" % (server_variables_blocks[provider])

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
<tr><td><b>Id</b></td><td><CopyableCode code="%s" /></td></tr>
</tbody></table>

""" % (resourceObj["name"], resourceObj["id"])
    else:
        return """
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>%s</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="%s" /></td></tr>
<tr><td><b>Description</b></td><td>%s</td></tr>
</tbody></table>

""" % (resourceObj["name"], resourceObj["id"], make_web_safe(resourceObj["description"]))

def generate_select_not_supported():
    output = "## Fields\n"
    output = output + "`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  \n"
    return output

def generate_fields_table(provider, serviceName, resourceName, fields, is_view=False):

    view_source_url = "https://github.com/stackql/stackql-provider-registry/blob/dev/providers/src/%s/v00.00.00000/services/%s.yaml" % (provider, serviceName)

    output = "## Fields\n"
    if is_view:
        output = output + "> This resource is a view. For the view definition, please refer to the provider spec in the [stackql-provider-registry](%s), located under `components -> x-stackQL-resources -> %s`.\n\n" % (view_source_url, resourceName)
    if fields.shape[0] > 1:
        if (fields["description"] == fields["description"][0]).all():
            output = output + "| Name | Datatype |\n"
            output = output + "|:-----|:---------|\n"
            for fieldIx, fieldRow in fields.iterrows():
                if len(fieldRow["type"]) == 0:
                    output = output + '| <CopyableCode code="%s" /> ||\n' % (fieldRow["name"])
                else:
                    output = output + '| <CopyableCode code="%s" /> | `%s` |\n' % (fieldRow["name"], fieldRow["type"])
        else:
            output = output + "| Name | Datatype | Description |\n"
            output = output + "|:-----|:---------|:------------|\n"
            for fieldIx, fieldRow in fields.iterrows():
                output = output + '| <CopyableCode code="%s" /> | `%s` | %s |\n' % (fieldRow["name"], fieldRow["type"], make_markdown_table_safe(fieldRow["description"]))
    return output

def generate_methods_table(methods):
    output = "## Methods\n"
    try:
        if (methods["description"] == methods["description"][0]).all():
            output = output + "| Name | Accessible by | Required Params |\n"
            output = output + "|:-----|:--------------|:----------------|\n"
            for methodIx, methodRow in methods.iterrows():
                if (methodRow["RequiredParams"] == ""):
                    output = output + '| <CopyableCode code="%s" /> | `%s` | %s |\n' % (methodRow["MethodName"], methodRow["SQLVerb"], methodRow["RequiredParams"])
                else:
                    output = output + '| <CopyableCode code="%s" /> | `%s` | <CopyableCode code="%s" /> |\n' % (methodRow["MethodName"], methodRow["SQLVerb"], methodRow["RequiredParams"])
        else:
            output = output + "| Name | Accessible by | Required Params | Description |\n"
            output = output + "|:-----|:--------------|:----------------|:------------|\n"
            for methodIx, methodRow in methods.iterrows():
                if (methodRow["RequiredParams"] == ""):
                    output = output + '| <CopyableCode code="%s" /> | `%s` | %s | %s |\n' % (methodRow["MethodName"], methodRow["SQLVerb"], methodRow["RequiredParams"], make_markdown_table_safe(methodRow["description"]))
                else:
                    output = output + '| <CopyableCode code="%s" /> | `%s` | <CopyableCode code="%s" /> | %s |\n' % (methodRow["MethodName"], methodRow["SQLVerb"], methodRow["RequiredParams"], make_markdown_table_safe(methodRow["description"]))
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

def generate_provider_summary(num_services, num_methods, num_resources, num_selectable_resources, provider_ver):
    output = ":::info Provider Summary (" + provider_ver + ")\n\n"
    output = output + '<div class="row">\n'
    output = output + '<div class="providerDocColumn">\n'
    output = output + '<span>total services:&nbsp;<b>%s</b></span><br />\n' % num_services
    output = output + '<span>total methods:&nbsp;<b>%s</b></span><br />\n' % num_methods
    output = output + '</div>\n'
    output = output + '<div class="providerDocColumn">\n'
    output = output + '<span>total resources:&nbsp;<b>%s</b></span><br />\n' % num_resources
    output = output + '<span>total selectable resources:&nbsp;<b>%s</b></span><br />\n' % num_selectable_resources
    output = output + '</div>\n'
    output = output + '</div>\n\n'
    output = output + ":::\n"
    return output

def generate_service_summary(num_methods, num_resources, num_selectable_resources):
    output = ":::info Service Summary\n\n"
    output = output + '<div class="row">\n'
    output = output + '<div class="providerDocColumn">\n'
    output = output + '<span>total resources:&nbsp;<b>%s</b></span><br />\n' % num_resources
    output = output + '<span>total selectable resources:&nbsp;<b>%s</b></span><br />\n' % num_selectable_resources
    output = output + '<span>total methods:&nbsp;<b>%s</b></span><br />\n' % num_methods
    output = output + '</div>\n'
    output = output + '</div>\n\n'
    output = output + ":::\n"
    return output

def generate_providers_list_page(provider):
    return """---
title: StackQL Provider Registry
hide_title: true
hide_table_of_contents: true
keywords:
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
slug: /
---
import RegistryPage from '@site/src/shared/shared-stackql-provider-registry.mdx';

<RegistryPage currentProvider="%s" />

---

""" % (provider)

