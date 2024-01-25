---
title: queries
hide_title: false
hide_table_of_contents: false
keywords:
  - queries
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
<tr><td><b>Name</b></td><td><code>queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.log_analytics.queries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `properties` | `object` | Properties that define an Log Analytics QueryPack-Query resource. |
| `systemData` | `object` | Read only system data |
| `type` | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, queryPackName, resourceGroupName, subscriptionId` | Gets a specific Log Analytics Query defined within a Log Analytics QueryPack. |
| `list` | `SELECT` | `queryPackName, resourceGroupName, subscriptionId` | Gets a list of Queries defined within a Log Analytics QueryPack. |
| `delete` | `DELETE` | `id, queryPackName, resourceGroupName, subscriptionId` | Deletes a specific Query defined within an Log Analytics QueryPack. |
| `_list` | `EXEC` | `queryPackName, resourceGroupName, subscriptionId` | Gets a list of Queries defined within a Log Analytics QueryPack. |
| `put` | `EXEC` | `id, queryPackName, resourceGroupName, subscriptionId` | Adds or Updates a specific Query within a Log Analytics QueryPack. |
| `search` | `EXEC` | `queryPackName, resourceGroupName, subscriptionId` | Search a list of Queries defined within a Log Analytics QueryPack according to given search properties. |
| `update` | `EXEC` | `id, queryPackName, resourceGroupName, subscriptionId` | Adds or Updates a specific Query within a Log Analytics QueryPack. |
