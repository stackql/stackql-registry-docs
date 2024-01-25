---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - graph_services
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.graph_services.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Property bag from billing account |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Returns account resource for a given name. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Returns list of accounts apps. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Returns list of accounts belonging to a subscription. |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes a account resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns list of accounts apps. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Returns list of accounts belonging to a subscription. |
| `create_and_update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId, data__properties` | Create or update account resource. |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update account details. |
