---
title: drives
hide_title: false
hide_table_of_contents: false
keywords:
  - drives
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
<tr><td><b>Name</b></td><td><code>drives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.fabric_admin.drives</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | The region where the resource is located. |
| `properties` | `object` | Properties of a drive. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `drive, location, resourceGroupName, scaleUnit, storageSubSystem, subscriptionId` | Return the requested a storage drive. |
| `list` | `SELECT` | `location, resourceGroupName, scaleUnit, storageSubSystem, subscriptionId` | Returns a list of all storage drives at a location. |
| `_list` | `EXEC` | `location, resourceGroupName, scaleUnit, storageSubSystem, subscriptionId` | Returns a list of all storage drives at a location. |
