import json, sys, shutil, os, pandas as pd
import psycopg
from psycopg.rows import dict_row
from functions import *
from provider_data import *

provider = sys.argv[1]
provider_ver = sys.argv[2]

conn = psycopg.connect(
      host="localhost", port=5444,
      autocommit = True,
      row_factory=dict_row
)

def run_query(query):
      print("running %s..." % query)
      try:
            r = conn.execute(query)
            data = r.fetchall()
            return pd.DataFrame([i.copy() for i in data])
      except Exception as e:
            print("ERROR [%s]" % str(e))
            sys.exit(1)

def run_command(query):
      print("running %s..." % query)
      try:
            r = conn.execute(query)
      except Exception as e:
            print("ERROR [%s]" % str(e))
            sys.exit(1)            

# pull docs for provider
print('pulling docs for %s %s' % (provider, provider_ver))
if provider_ver == "latest":
      iql_query = "REGISTRY PULL %s" % provider
else:
      iql_query = "REGISTRY PULL %s %s" % (provider, provider_ver)
run_command(iql_query)

provider_root_dir = "%s/devdocs/%s-docs" % (os.getcwd(), provider)
provider_providers_root_dir = "%s/providers" % (provider_root_dir)
services_dir = "%s/%s" % (provider_providers_root_dir, provider)

# clean output dir
print('cleaning %s if it exists...' % (provider_root_dir))
shutil.rmtree(provider_root_dir, ignore_errors=True)

total_provider_resources = 0
total_provider_selectable_resources = 0
total_provider_methods = 0

# get services and add to provider doc
iql_query = "SHOW EXTENDED SERVICES IN %s" % provider
services = run_query(iql_query)
services = services.groupby("name", as_index=False).max()

# create output dir (root)
create_dir(provider_root_dir)
create_dir(provider_providers_root_dir)

# create services dir
create_dir(services_dir)
    
#
# create service and resource docs
#

for serviceIx, serviceRow in services.iterrows():

    total_service_resources = 0
    total_service_selectable_resources = 0
    total_service_methods = 0

    serviceName = serviceRow["name"]

    print("serviceName: %s" % serviceName)

    # create service dir
    this_service_dir = "%s/%s" % (services_dir, serviceName)
    create_dir(this_service_dir)

    #
    # get resources
    #

    iql_query = "SHOW EXTENDED RESOURCES IN %s.%s" % (provider, serviceName)
    resources = run_query(iql_query)
    total_service_resources = len(resources)
    total_provider_resources = total_provider_resources + total_service_resources

    for resourceIx, resourceRow in resources.iterrows():
        try:
            resourceName = resourceRow["name"]
        except:
            break

        print("resourceName: %s" % resourceName)
        
        # create resource dir
        this_resource_dir = "%s/%s" % (this_service_dir, resourceName)
        create_dir(this_resource_dir)

        # create resource doc
        resource_doc = generate_front_matter(resourceName, 
                                    provider_data[provider]['meta_description'],
                                    resourceRow["description"],
                                    provider_data[provider]['image'],
                                    serviceName,
                                    provider
                                    )
        resource_doc = resource_doc + generate_resource_overview(provider, serviceName, resourceRow)

        # get methods
        iql_query = "SHOW EXTENDED METHODS IN %s.%s.%s" % (provider, serviceName, resourceName)
        methods = run_query(iql_query)
        total_service_methods = total_service_methods + len(methods)
        total_provider_methods = total_provider_methods + len(methods)

        if len(methods.query("SQLVerb == 'SELECT'")) > 0:
                total_service_selectable_resources = total_service_selectable_resources + 1
                total_provider_selectable_resources = total_provider_selectable_resources + 1
                # get fields
                iql_query = "DESCRIBE EXTENDED %s.%s.%s" % (provider, serviceName, resourceName)
                fields = run_query(iql_query)
                resource_doc = resource_doc + generate_fields_table(fields)
        else:
                resource_doc = resource_doc + generate_select_not_supported()

        resource_doc = resource_doc + generate_methods_table(methods)

        # write resource doc
        write_file("%s/index.md" % (this_resource_dir), resource_doc)

    # create service doc
    service_doc = generate_front_matter(serviceName, 
                                    provider_data[provider]['meta_description'],
                                    serviceRow["description"],
                                    provider_data[provider]['image'],
                                    provider
                                    )
    

    service_doc = service_doc + generate_service_summary(total_service_methods, total_service_resources, total_service_selectable_resources)
    service_doc = service_doc + generate_service_overview(provider, serviceRow)

    service_doc = service_doc + "## Resources\n"
    service_doc = service_doc + generate_two_col_list(provider, resources, serviceName)

    # write service doc
    write_file("%s/index.md" % (this_service_dir), service_doc)

    
#
# generate provider root doc
#

print('%s/index.md' % (provider_root_dir))

provider_doc = generate_front_matter(provider, 
                                    provider_data[provider]['meta_description'],
                                    provider_data[provider]['description'],
                                    provider_data[provider]['image']
                                    )

# add provider summary and see also links
provider_doc = provider_doc + generate_provider_summary(len(services), total_provider_methods, total_provider_resources, total_provider_selectable_resources)
provider_doc = provider_doc + generate_see_also_links()

# add install and auth blocks to provider doc
provider_doc = provider_doc + generate_installation_block(provider)
provider_doc = provider_doc + generate_auth_block(provider)

if server_variables_blocks[provider]:
    provider_doc = provider_doc + generate_server_variables_block(provider)

# add service list
provider_doc = provider_doc + "## Services\n"
provider_doc = provider_doc + generate_two_col_list(provider, services)

# write provider doc
write_file("%s/index.md" % provider_root_dir, provider_doc)

# write stackql-provider-registry.mdx
print('%s/stackql-provider-registry.mdx' % (provider_root_dir))
providers_list_page = generate_providers_list_page(provider)
write_file("%s/stackql-provider-registry.mdx" % provider_root_dir, providers_list_page)
