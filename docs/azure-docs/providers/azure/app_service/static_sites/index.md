---
title: static_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - static_sites
  - app_service
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>static_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.static_sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `identity` | `object` | Managed service identity. |
| `properties` | `object` | A static site. |
| `sku` | `object` | Description of a SKU for a scalable resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `subscriptionId` | Description for Get all Static Sites for a subscription. |
| `_list` | `EXEC` | `subscriptionId` | Description for Get all Static Sites for a subscription. |
| `approve_or_reject_private_endpoint_connection` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Description for Approves or rejects a private endpoint connection |
| `detach_static_site` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Detaches a static site. |
| `detach_user_provided_function_app_from_static_site` | `EXEC` | `functionAppName, name, resourceGroupName, subscriptionId` | Description for Detach the user provided function app from the static site |
| `detach_user_provided_function_app_from_static_site_build` | `EXEC` | `environmentName, functionAppName, name, resourceGroupName, subscriptionId` | Description for Detach the user provided function app from the static site build |
| `link_backend` | `EXEC` | `linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `link_backend_to_build` | `EXEC` | `environmentName, linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `preview_workflow` | `EXEC` | `location, subscriptionId` | Description for Generates a preview workflow file for the static site |
| `register_user_provided_function_app_with_static_site` | `EXEC` | `functionAppName, name, resourceGroupName, subscriptionId` | Description for Register a user provided function app with a static site |
| `register_user_provided_function_app_with_static_site_build` | `EXEC` | `environmentName, functionAppName, name, resourceGroupName, subscriptionId` | Description for Register a user provided function app with a static site build |
| `reset_static_site_api_key` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Resets the api key for an existing static site. |
| `unlink_backend` | `EXEC` | `linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `unlink_backend_from_build` | `EXEC` | `environmentName, linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `validate_backend` | `EXEC` | `linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `validate_backend_for_build` | `EXEC` | `environmentName, linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `validate_custom_domain_can_be_added_to_static_site` | `EXEC` | `domainName, name, resourceGroupName, subscriptionId` | Description for Validates a particular custom domain can be added to a static site. |
