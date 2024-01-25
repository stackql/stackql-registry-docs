---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - engagement_fabric
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
<tr><td><b>Id</b></td><td><code>azure.engagement_fabric.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The location of the resource |
| `sku` | `object` | The EngagementFabric SKU |
| `tags` | `object` | The tags of the resource |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `subscriptionId` |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__location, data__sku` |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `subscriptionId` |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` |
| `regenerate_key` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__name, data__rank` |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` |
