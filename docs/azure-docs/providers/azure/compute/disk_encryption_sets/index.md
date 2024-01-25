---
title: disk_encryption_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_encryption_sets
  - compute
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
<tr><td><b>Name</b></td><td><code>disk_encryption_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.disk_encryption_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `identity` | `object` | The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks. |
| `location` | `string` | Resource location |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `diskEncryptionSetName, resourceGroupName, subscriptionId` | Gets information about a disk encryption set. |
| `list` | `SELECT` | `subscriptionId` | Lists all the disk encryption sets under a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the disk encryption sets under a resource group. |
| `create_or_update` | `INSERT` | `diskEncryptionSetName, resourceGroupName, subscriptionId` | Creates or updates a disk encryption set |
| `delete` | `DELETE` | `diskEncryptionSetName, resourceGroupName, subscriptionId` | Deletes a disk encryption set. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the disk encryption sets under a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the disk encryption sets under a resource group. |
| `update` | `EXEC` | `diskEncryptionSetName, resourceGroupName, subscriptionId` | Updates (patches) a disk encryption set. |
