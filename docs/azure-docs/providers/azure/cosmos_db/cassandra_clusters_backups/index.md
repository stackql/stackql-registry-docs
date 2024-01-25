---
title: cassandra_clusters_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_clusters_backups
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>cassandra_clusters_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.cassandra_clusters_backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `backupExpiryTimestamp` | `string` | The time at which the backup will expire. |
| `backupId` | `string` | The unique identifier of backup. |
| `backupStartTimestamp` | `string` | The time at which the backup process begins. |
| `backupState` | `string` | The current state of the backup. |
| `backupStopTimestamp` | `string` | The time at which the backup process ends. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupId, clusterName, resourceGroupName, subscriptionId` | Get the properties of an individual backup of this cluster that is available to restore. |
| `list` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | List the backups of this cluster that are available to restore. |
| `_list` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | List the backups of this cluster that are available to restore. |
