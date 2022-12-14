---
title: recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_points
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>recovery_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.recovery_points</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `properties` | `object` | Recovery point properties. |
| `type` | `string` | Resource Type |
| `location` | `string` | Resource Location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RecoveryPoints_Get` | `SELECT` | `api-version, fabricName, protectionContainerName, recoveryPointName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Get the details of specified recovery point. |
| `RecoveryPoints_ListByReplicationProtectedItems` | `SELECT` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` | Lists the available recovery points for a replication protected item. |
