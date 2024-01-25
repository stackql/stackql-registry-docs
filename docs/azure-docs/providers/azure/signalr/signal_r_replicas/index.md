---
title: signal_r_replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_r_replicas
  - signalr
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
<tr><td><b>Name</b></td><td><code>signal_r_replicas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.signalr.signal_r_replicas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `sku` | `object` | The billing information of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `replicaName, resourceGroupName, resourceName, subscriptionId` | Get the replica and its properties. |
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | List all replicas belong to this resource |
| `create_or_update` | `INSERT` | `replicaName, resourceGroupName, resourceName, subscriptionId` | Create or update a replica. |
| `delete` | `DELETE` | `replicaName, resourceGroupName, resourceName, subscriptionId` | Operation to delete a replica. |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | List all replicas belong to this resource |
| `restart` | `EXEC` | `replicaName, resourceGroupName, resourceName, subscriptionId` | Operation to restart a replica. |
| `update` | `EXEC` | `replicaName, resourceGroupName, resourceName, subscriptionId` | Operation to update an exiting replica. |
