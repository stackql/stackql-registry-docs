---
title: flexible_server
hide_title: false
hide_table_of_contents: false
keywords:
  - flexible_server
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
<tr><td><b>Name</b></td><td><code>flexible_server</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql.flexible_server</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `start_ltr_backup` | `EXEC` | `resourceGroupName, serverName, subscriptionId, data__targetDetails` | Start the Long Term Retention Backup operation |
| `trigger_ltr_pre_backup` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | PreBackup operation performs all the checks that are needed for the subsequent long term retention backup operation to succeed. |
