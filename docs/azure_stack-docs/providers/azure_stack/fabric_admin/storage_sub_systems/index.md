---
title: storage_sub_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_sub_systems
  - fabric_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>storage_sub_systems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.fabric_admin.storage_sub_systems</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | The region where the resource is located. |
| `properties` | `object` | All properties of a storage subsystem. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `location, resourceGroupName, scaleUnit, storageSubSystem, subscriptionId` | Return the requested storage subsystem. |
| `list` | `SELECT` | `location, resourceGroupName, scaleUnit, subscriptionId` | Returns a list of all storage subsystems for a location. |
| `_list` | `EXEC` | `location, resourceGroupName, scaleUnit, subscriptionId` | Returns a list of all storage subsystems for a location. |
