import json, sys, shutil, os, pandas as pd
from functions import *
from provider_data import *

provider = sys.argv[1]
provider_ver = sys.argv[2]

# pull docs for provider
print('pulling docs for %s %s' % (provider, provider_ver))
iql_query = "REGISTRY PULL %s %s" % (provider, provider_ver)
run_stackql_query(iql_query, 0)

# clean output dir
print('cleaning %s/docs/%s if it exists...' % (os.getcwd(), provider))
shutil.rmtree("./docs/%s" % provider, ignore_errors=True)

#
# generate provider root doc
#

print('initiializing %s/docs/%s/index.md' % (os.getcwd(), provider))
provider_doc = generate_front_matter(provider, 
                                    provider_data[provider]['meta_description'],
                                    provider_data[provider]['description'],
                                    provider_data[provider]['image']
                                    )
provider_doc = provider_doc + generate_see_also_links()

# add install and auth blocks to provider doc
provider_doc = provider_doc + generate_installation_block(provider, provider_ver)
provider_doc = provider_doc + generate_auth_block(provider)

# get services and add to provider doc
iql_query = "SHOW EXTENDED SERVICES IN %s" % provider
services = run_stackql_query(iql_query, 5)
services = services.groupby("name", as_index=False).max()
provider_doc = provider_doc + "## Services\n"
provider_doc = provider_doc + generate_two_col_list(provider, services)

# create output dir
create_dir("./docs/%s" % provider)
    
# write provider doc
write_file("./docs/%s/index.md" % provider, provider_doc)

#
# create service and resource docs
#

for serviceIx, serviceRow in services.iterrows():
    
    serviceName = serviceRow["name"]

    print("serviceName: %s" % serviceName)

    # create service dir
    create_dir("./docs/%s/%s" % (provider, serviceName))

    # create service doc
    service_doc = generate_front_matter(serviceName, 
                                    provider_data[provider]['meta_description'],
                                    serviceRow["description"],
                                    provider_data[provider]['image'],
                                    provider
                                    )
    service_doc = service_doc + generate_service_overview(provider, serviceRow)

    #
    # get resources
    #

    iql_query = "SHOW EXTENDED RESOURCES IN %s.%s" % (provider, serviceName)
    resources = run_stackql_query(iql_query, 5)

    service_doc = service_doc + "## Resources\n"
    service_doc = service_doc + generate_two_col_list(provider, resources, serviceName)

    # write service doc
    write_file("./docs/%s/%s/index.md" % (provider, serviceName), service_doc)

    for resourceIx, resourceRow in resources.iterrows():
        try:
            resourceName = resourceRow["name"]
        except:
            break

        print("resourceName: %s" % resourceName)
        
        # create resource dir
        create_dir("./docs/%s/%s/%s" % (provider, serviceName, resourceName))

        # create resource doc
        resource_doc = generate_front_matter(resourceName, 
                                    provider_data[provider]['meta_description'],
                                    resourceRow["description"],
                                    provider_data[provider]['image'],
                                    serviceName,
                                    provider
                                    )
        resource_doc = resource_doc + generate_resource_overview(provider, serviceName, resourceRow)

        # get fields
        iql_query = "DESCRIBE EXTENDED %s.%s.%s" % (provider, serviceName, resourceName)
        fields = run_stackql_query(iql_query, 5)
        resource_doc = resource_doc + generate_fields_table(fields)
        
        # get methods
        iql_query = "SHOW EXTENDED METHODS IN %s.%s.%s" % (provider, serviceName, resourceName)
        methods = run_stackql_query(iql_query, 5)
        resource_doc = resource_doc + generate_methods_table(methods)

        # write resource doc
        write_file("./docs/%s/%s/%s/index.md" % (provider, serviceName, resourceName), resource_doc)

    