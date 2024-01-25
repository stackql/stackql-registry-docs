---
title: sql_pool_maintenance_windows
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_maintenance_windows
  - synapse
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
<tr><td><b>Name</b></td><td><code>sql_pool_maintenance_windows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_maintenance_windows</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `maintenanceWindowName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get a SQL pool's Maintenance Windows. |
| `create_or_update` | `INSERT` | `maintenanceWindowName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Creates or updates a Sql pool's maintenance windows settings. |
