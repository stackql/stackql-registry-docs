---
title: fabric
hide_title: false
hide_table_of_contents: false
keywords:
  - fabric
  - data_replication
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
<tr><td><b>Name</b></td><td><code>fabric</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_replication.fabric</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id of the resource. |
| `name` | `string` | Gets or sets the name of the resource. |
| `location` | `string` | Gets or sets the location of the fabric. |
| `properties` | `object` | Fabric model properties. |
| `systemData` | `object` | System data required to be defined for Azure resources. |
| `tags` | `object` | Gets or sets the resource tags. |
| `type` | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fabricName, resourceGroupName, subscriptionId` | Gets the details of the fabric. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the list of fabrics in the given subscription and resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets the list of fabrics in the given subscription. |
| `create` | `INSERT` | `fabricName, resourceGroupName, subscriptionId, data__location, data__properties` | Creates the fabric. |
| `delete` | `DELETE` | `fabricName, resourceGroupName, subscriptionId` | Removes the fabric. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Gets the list of fabrics in the given subscription and resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets the list of fabrics in the given subscription. |
| `update` | `EXEC` | `fabricName, resourceGroupName, subscriptionId` | Performs update on the fabric. |
