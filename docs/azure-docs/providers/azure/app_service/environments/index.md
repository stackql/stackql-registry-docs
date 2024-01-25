---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Description of an App Service Environment. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Get the properties of an App Service Environment. |
| `list` | `SELECT` | `subscriptionId` | Description for Get all App Service Environments for a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Description for Get all App Service Environments in a resource group. |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId` | Description for Create or update an App Service Environment. |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Description for Delete an App Service Environment. |
| `_list` | `EXEC` | `subscriptionId` | Description for Get all App Service Environments for a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Description for Get all App Service Environments in a resource group. |
| `approve_or_reject_private_endpoint_connection` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Description for Approves or rejects a private endpoint connection |
| `change_vnet` | `EXEC` | `name, resourceGroupName, subscriptionId, data__id` | Description for Move an App Service Environment to a different VNET. |
| `reboot` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Reboot all machines in an App Service Environment. |
| `resume` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Resume an App Service Environment. |
| `suspend` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Suspend an App Service Environment. |
| `test_upgrade_available_notification` | `EXEC` | `name, resourceGroupName, subscriptionId` |  |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Create or update an App Service Environment. |
| `upgrade` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Initiate an upgrade of an App Service Environment if one is available. |
