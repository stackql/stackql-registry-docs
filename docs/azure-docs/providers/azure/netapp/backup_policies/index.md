---
title: backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_policies
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
<tr><td><b>Name</b></td><td><code>backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.backup_policies</code></td></tr>
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
| `BackupPolicies_Get` | `SELECT` | `accountName, backupPolicyName, resourceGroupName, subscriptionId` | Get a particular backup Policy |
| `BackupPolicies_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List backup policies for Netapp Account |
| `BackupPolicies_Create` | `INSERT` | `accountName, backupPolicyName, resourceGroupName, subscriptionId, data__location, data__properties` | Create a backup policy for Netapp Account |
| `BackupPolicies_Delete` | `DELETE` | `accountName, backupPolicyName, resourceGroupName, subscriptionId` | Delete backup policy |
| `BackupPolicies_Update` | `EXEC` | `accountName, backupPolicyName, resourceGroupName, subscriptionId` | Patch a backup policy for Netapp Account |
