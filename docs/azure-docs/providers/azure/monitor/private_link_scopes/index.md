---
title: private_link_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_scopes
  - monitor
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
<tr><td><b>Name</b></td><td><code>private_link_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.private_link_scopes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties that define a Azure Monitor PrivateLinkScope resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, scopeName, subscriptionId` | Returns a Azure Monitor PrivateLinkScope. |
| `list` | `SELECT` | `subscriptionId` | Gets a list of all Azure Monitor PrivateLinkScopes within a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of Azure Monitor PrivateLinkScopes within a resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, scopeName, subscriptionId, data__properties` | Creates (or updates) a Azure Monitor PrivateLinkScope. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation. |
| `delete` | `DELETE` | `resourceGroupName, scopeName, subscriptionId` | Deletes a Azure Monitor PrivateLinkScope. |
| `_list` | `EXEC` | `subscriptionId` | Gets a list of all Azure Monitor PrivateLinkScopes within a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of Azure Monitor PrivateLinkScopes within a resource group. |
