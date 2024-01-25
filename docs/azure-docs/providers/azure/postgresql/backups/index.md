---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql.backups</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupName, resourceGroupName, serverName, subscriptionId` | Get specific backup for a given server. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | List all the backups for a given server. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | List all the backups for a given server. |
