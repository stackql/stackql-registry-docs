---
title: account_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - account_backups
  - netapp
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
<tr><td><b>Name</b></td><td><code>account_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.account_backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | Backup properties |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AccountBackups_Get` | `SELECT` | `accountName, backupName, resourceGroupName, subscriptionId` | Gets the specified backup for a Netapp Account |
| `AccountBackups_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List all Backups for a Netapp Account |
| `AccountBackups_Delete` | `DELETE` | `accountName, backupName, resourceGroupName, subscriptionId` | Delete the specified Backup for a Netapp Account |
