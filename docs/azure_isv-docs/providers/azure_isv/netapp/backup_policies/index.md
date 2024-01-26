---
title: backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_policies
  - netapp
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
<tr><td><b>Name</b></td><td><code>backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.netapp.backup_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Backup policy properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, backupPolicyName, resourceGroupName, subscriptionId` | Get a particular backup Policy |
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List backup policies for Netapp Account |
| `create` | `INSERT` | `accountName, backupPolicyName, resourceGroupName, subscriptionId, data__location, data__properties` | Create a backup policy for Netapp Account |
| `delete` | `DELETE` | `accountName, backupPolicyName, resourceGroupName, subscriptionId` | Delete backup policy |
| `_list` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | List backup policies for Netapp Account |
| `update` | `EXEC` | `accountName, backupPolicyName, resourceGroupName, subscriptionId` | Patch a backup policy for Netapp Account |
