---
title: cluster_managers
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_managers
  - nexus
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
<tr><td><b>Name</b></td><td><code>cluster_managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.cluster_managers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterManagerName, resourceGroupName, subscriptionId` | Get the properties of the provided cluster manager. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of cluster managers in the provided resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get a list of cluster managers in the provided subscription. |
| `create_or_update` | `INSERT` | `clusterManagerName, resourceGroupName, subscriptionId, data__properties` | Create a new cluster manager or update properties of the cluster manager if it exists. |
| `delete` | `DELETE` | `clusterManagerName, resourceGroupName, subscriptionId` | Delete the provided cluster manager. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of cluster managers in the provided resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get a list of cluster managers in the provided subscription. |
| `update` | `EXEC` | `clusterManagerName, resourceGroupName, subscriptionId` | Patch properties of the provided cluster manager, or update the tags assigned to the cluster manager. Properties and tag updates can be done independently. |
