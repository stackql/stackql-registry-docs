---
title: managed_cluster_snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_cluster_snapshots
  - container_service
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
<tr><td><b>Name</b></td><td><code>managed_cluster_snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_service.managed_cluster_snapshots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties for a managed cluster snapshot. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ManagedClusterSnapshots_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
| `ManagedClusterSnapshots_List` | `SELECT` | `subscriptionId` |
| `ManagedClusterSnapshots_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `ManagedClusterSnapshots_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` |
| `ManagedClusterSnapshots_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` |
| `ManagedClusterSnapshots_UpdateTags` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |
