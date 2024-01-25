---
title: ltr_backup_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - ltr_backup_operations
  - postgresql
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
<tr><td><b>Name</b></td><td><code>ltr_backup_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql.ltr_backup_operations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupName, resourceGroupName, serverName, subscriptionId` | Gets the result of the give long term retention backup operation for the flexible server. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets the result of the give long term retention backup operations for the flexible server. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets the result of the give long term retention backup operations for the flexible server. |
