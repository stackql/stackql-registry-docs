---
title: file_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - file_containers
  - deployment_admin
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
<tr><td><b>Name</b></td><td><code>file_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.deployment_admin.file_containers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | File Container Properties. |
| `type` | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fileContainerId, subscriptionId` | Retrieves the specific file container details. |
| `list` | `SELECT` | `subscriptionId` | Returns an array of file containers. |
| `create` | `INSERT` | `fileContainerId, subscriptionId` | Creates a new file container. |
| `delete` | `DELETE` | `fileContainerId, subscriptionId` | Delete an existing file container. |
| `_list` | `EXEC` | `subscriptionId` | Returns an array of file containers. |
