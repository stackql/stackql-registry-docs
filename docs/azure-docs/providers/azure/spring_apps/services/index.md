---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The GEO location of the resource. |
| `properties` | `object` | Service properties payload |
| `sku` | `object` | Sku of Azure Spring Apps |
| `tags` | `object` | Tags of the service which is a list of key value pairs that describe the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Get a Service and its properties. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, serviceName, subscriptionId` | Create a new Service or update an exiting Service. |
| `delete` | `DELETE` | `resourceGroupName, serviceName, subscriptionId` | Operation to delete a Service. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `check_name_availability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks that the resource name is valid and is not already in use. |
| `disable_apm_globally` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, data__resourceId` | Disable an APM globally. |
| `disable_test_endpoint` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Disable test endpoint functionality for a Service. |
| `enable_apm_globally` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, data__resourceId` | Enable an APM globally. |
| `enable_test_endpoint` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Enable test endpoint functionality for a Service. |
| `flush_vnet_dns_setting` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Flush Virtual Network DNS settings for a VNET injected Service. |
| `regenerate_test_key` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, data__keyType` | Regenerate a test key for a Service. |
| `start` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Start a Service. |
| `stop` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Stop a Service. |
| `update` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Operation to update an exiting Service. |
