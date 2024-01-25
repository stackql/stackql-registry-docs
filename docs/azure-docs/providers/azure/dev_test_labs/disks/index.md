---
title: disks
hide_title: false
hide_table_of_contents: false
keywords:
  - disks
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_test_labs.disks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a disk. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Get disk. |
| `list` | `SELECT` | `api-version, labName, resourceGroupName, subscriptionId, userName` | List disks in a given user profile. |
| `create_or_update` | `INSERT` | `api-version, labName, name, resourceGroupName, subscriptionId, userName, data__properties` | Create or replace an existing disk. This operation can take a while to complete. |
| `delete` | `DELETE` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Delete disk. This operation can take a while to complete. |
| `_list` | `EXEC` | `api-version, labName, resourceGroupName, subscriptionId, userName` | List disks in a given user profile. |
| `attach` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Attach and create the lease of the disk to the virtual machine. This operation can take a while to complete. |
| `detach` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Detach and break the lease of the disk attached to the virtual machine. This operation can take a while to complete. |
| `update` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Allows modifying tags of disks. All other properties will be ignored. |
