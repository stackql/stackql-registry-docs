---
title: machine_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - machine_extensions
  - hybrid_compute
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
<tr><td><b>Name</b></td><td><code>machine_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_compute.machine_extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of a Machine Extension. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `extensionName, machineName, resourceGroupName, subscriptionId` | The operation to get the extension. |
| `list` | `SELECT` | `machineName, resourceGroupName, subscriptionId` | The operation to get all extensions of a non-Azure machine |
| `create_or_update` | `INSERT` | `extensionName, machineName, resourceGroupName, subscriptionId` | The operation to create or update the extension. |
| `delete` | `DELETE` | `extensionName, machineName, resourceGroupName, subscriptionId` | The operation to delete the extension. |
| `_list` | `EXEC` | `machineName, resourceGroupName, subscriptionId` | The operation to get all extensions of a non-Azure machine |
| `update` | `EXEC` | `extensionName, machineName, resourceGroupName, subscriptionId` | The operation to create or update the extension. |
