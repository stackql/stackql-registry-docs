---
title: consoles
hide_title: false
hide_table_of_contents: false
keywords:
  - consoles
  - nexus
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
<tr><td><b>Name</b></td><td><code>consoles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.consoles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `consoleName, resourceGroupName, subscriptionId, virtualMachineName` | Get properties of the provided virtual machine console. |
| `list_by_virtual_machine` | `SELECT` | `resourceGroupName, subscriptionId, virtualMachineName` | Get a list of consoles for the provided virtual machine. |
| `create_or_update` | `INSERT` | `consoleName, resourceGroupName, subscriptionId, virtualMachineName, data__extendedLocation, data__properties` | Create a new virtual machine console or update the properties of the existing virtual machine console. |
| `delete` | `DELETE` | `consoleName, resourceGroupName, subscriptionId, virtualMachineName` | Delete the provided virtual machine console. |
| `_list_by_virtual_machine` | `EXEC` | `resourceGroupName, subscriptionId, virtualMachineName` | Get a list of consoles for the provided virtual machine. |
| `update` | `EXEC` | `consoleName, resourceGroupName, subscriptionId, virtualMachineName` | Patch the properties of the provided virtual machine console, or update the tags associated with the virtual machine console. Properties and tag updates can be done independently. |
