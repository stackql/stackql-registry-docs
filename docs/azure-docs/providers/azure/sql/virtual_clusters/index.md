---
title: virtual_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_clusters
  - sql
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
<tr><td><b>Name</b></td><td><code>virtual_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.virtual_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The properties of a virtual cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualClusters_Get` | `SELECT` | `resourceGroupName, subscriptionId, virtualClusterName` | Gets a virtual cluster. |
| `VirtualClusters_List` | `SELECT` | `subscriptionId` | Gets a list of all virtualClusters in the subscription. |
| `VirtualClusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of virtual clusters in a resource group. |
| `VirtualClusters_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualClusterName` | Deletes a virtual cluster. |
| `VirtualClusters_Update` | `EXEC` | `resourceGroupName, subscriptionId, virtualClusterName` | Updates an existing virtual cluster. |
| `VirtualClusters_UpdateDnsServers` | `EXEC` | `resourceGroupName, subscriptionId, virtualClusterName` | Synchronizes the DNS server settings used by the managed instances inside the given virtual cluster. |
