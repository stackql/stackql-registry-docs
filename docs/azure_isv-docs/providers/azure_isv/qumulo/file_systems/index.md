---
title: file_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - file_systems
  - qumulo
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>file_systems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.qumulo.file_systems</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the File System resource |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties specific to the Qumulo File System resource |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `fileSystemName, resourceGroupName, subscriptionId` | Get a FileSystemResource |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List FileSystemResource resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List FileSystemResource resources by subscription ID |
| `create_or_update` | `INSERT` | `fileSystemName, resourceGroupName, subscriptionId, data__properties` | Create a FileSystemResource |
| `delete` | `DELETE` | `fileSystemName, resourceGroupName, subscriptionId` | Delete a FileSystemResource |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List FileSystemResource resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List FileSystemResource resources by subscription ID |
| `update` | `EXEC` | `fileSystemName, resourceGroupName, subscriptionId` | Update a FileSystemResource |
