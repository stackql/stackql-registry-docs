---
title: machine_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - machine_extensions
  - connected_vsphere
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.connected_vsphere.machine_extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id. |
| `name` | `string` | Gets or sets the name. |
| `properties` | `object` | Describes the properties of a Machine Extension. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Gets or sets the Resource tags. |
| `type` | `string` | Gets or sets the type of the resource. |
| `location` | `string` | Gets or sets the location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MachineExtensions_Get` | `SELECT` | `api-version, extensionName, name, resourceGroupName, subscriptionId` | The operation to get the extension. |
| `MachineExtensions_List` | `SELECT` | `api-version, name, resourceGroupName, subscriptionId` | The operation to get all extensions of a non-Azure machine |
| `MachineExtensions_CreateOrUpdate` | `INSERT` | `api-version, extensionName, name, resourceGroupName, subscriptionId` | The operation to create or update the extension. |
| `MachineExtensions_Delete` | `DELETE` | `api-version, extensionName, name, resourceGroupName, subscriptionId` | The operation to delete the extension. |
| `MachineExtensions_Update` | `EXEC` | `api-version, extensionName, name, resourceGroupName, subscriptionId` | The operation to update the extension. |
