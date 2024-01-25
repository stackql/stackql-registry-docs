---
title: plans
hide_title: false
hide_table_of_contents: false
keywords:
  - plans
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
<tr><td><b>Name</b></td><td><code>plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `extendedLocation` | `object` | Extended Location. |
| `properties` | `object` | AppServicePlan resource specific properties |
| `sku` | `object` | Description of a SKU for a scalable resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Get an App Service plan. |
| `list` | `SELECT` | `subscriptionId` | Description for Get all App Service plans for a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Description for Get all App Service plans in a resource group. |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId` | Description for Creates or updates an App Service Plan. |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Description for Delete an App Service plan. |
| `_list` | `EXEC` | `subscriptionId` | Description for Get all App Service plans for a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Description for Get all App Service plans in a resource group. |
| `reboot_worker` | `EXEC` | `name, resourceGroupName, subscriptionId, workerName` | Description for Reboot a worker machine in an App Service plan. |
| `restart_web_apps` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Restart all apps in an App Service plan. |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates or updates an App Service Plan. |
