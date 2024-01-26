---
title: vm_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - vm_extensions
  - compute_admin
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
<tr><td><b>Name</b></td><td><code>vm_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.compute_admin.vm_extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of a Virtual Machine Extension Image. |
| `type` | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `location, publisher, subscriptionId, type, version` | Returns requested Virtual Machine Extension Image matching publisher, type, version. |
| `list` | `SELECT` | `location, subscriptionId` | List of all Virtual Machine Extension Images for the current location are returned. |
| `create` | `INSERT` | `location, publisher, subscriptionId, type, version` | Create a Virtual Machine Extension Image with publisher, version. |
| `delete` | `DELETE` | `location, publisher, subscriptionId, type, version` | Deletes specified Virtual Machine Extension Image. |
