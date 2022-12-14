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
| `properties` | `object` | Describes the properties of a Machine Extension. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MachineExtensions_Get` | `SELECT` | `extensionName, machineName, resourceGroupName, subscriptionId` | The operation to get the extension. |
| `MachineExtensions_List` | `SELECT` | `machineName, resourceGroupName, subscriptionId` | The operation to get all extensions of a non-Azure machine |
| `MachineExtensions_CreateOrUpdate` | `INSERT` | `extensionName, machineName, resourceGroupName, subscriptionId` | The operation to create or update the extension. |
| `MachineExtensions_Delete` | `DELETE` | `extensionName, machineName, resourceGroupName, subscriptionId` | The operation to delete the extension. |
| `MachineExtensions_Update` | `EXEC` | `extensionName, machineName, resourceGroupName, subscriptionId` | The operation to create or update the extension. |
