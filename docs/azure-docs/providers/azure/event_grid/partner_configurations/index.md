---
title: partner_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_configurations
  - event_grid
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
<tr><td><b>Name</b></td><td><code>partner_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.partner_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of the partner configuration. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Tags of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the partner configurations under a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all the partner configurations under an Azure subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId` | Synchronously creates or updates a partner configuration with the specified parameters. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId` | Delete existing partner configuration. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the partner configurations under a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all the partner configurations under an Azure subscription. |
| `authorize_partner` | `EXEC` | `resourceGroupName, subscriptionId` | Authorize a single partner either by partner registration immutable Id or by partner name. |
| `exec_get` | `EXEC` | `resourceGroupName, subscriptionId` | Get properties of a partner configuration. |
| `unauthorize_partner` | `EXEC` | `resourceGroupName, subscriptionId` | Unauthorize a single partner either by partner registration immutable Id or by partner name. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId` | Synchronously updates a partner configuration with the specified parameters. |
