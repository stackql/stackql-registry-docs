---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - container_storage
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
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_storage.snapshots</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `poolName, resourceGroupName, snapshotName, subscriptionId` | Get a Snapshot |
| `list_by_pool` | `SELECT` | `poolName, resourceGroupName, subscriptionId` | List Snapshot resources by Pool |
| `create_or_update` | `INSERT` | `poolName, resourceGroupName, snapshotName, subscriptionId` | Create a Snapshot |
| `delete` | `DELETE` | `poolName, resourceGroupName, snapshotName, subscriptionId` | Compliant create or update template/** |
| `_list_by_pool` | `EXEC` | `poolName, resourceGroupName, subscriptionId` | List Snapshot resources by Pool |
