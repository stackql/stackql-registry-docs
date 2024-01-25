---
title: query_packs
hide_title: false
hide_table_of_contents: false
keywords:
  - query_packs
  - log_analytics
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
<tr><td><b>Name</b></td><td><code>query_packs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.log_analytics.query_packs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | Properties that define a Log Analytics QueryPack resource. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `queryPackName, resourceGroupName, subscriptionId` | Returns a Log Analytics QueryPack. |
| `list` | `SELECT` | `subscriptionId` | Gets a list of all Log Analytics QueryPacks within a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of Log Analytics QueryPacks within a resource group. |
| `create_or_update` | `INSERT` | `queryPackName, resourceGroupName, subscriptionId, data__properties` | Creates (or updates) a Log Analytics QueryPack. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation. |
| `delete` | `DELETE` | `queryPackName, resourceGroupName, subscriptionId` | Deletes a Log Analytics QueryPack. |
| `_list` | `EXEC` | `subscriptionId` | Gets a list of all Log Analytics QueryPacks within a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of Log Analytics QueryPacks within a resource group. |
