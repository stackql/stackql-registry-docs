---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - event_hubs
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_hubs.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | Event Hubs Cluster properties supplied in responses in List or Get operations. |
| `sku` | `object` | SKU parameters particular to a cluster instance. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets the resource description of the specified Event Hubs Cluster. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the available Event Hubs Clusters within an ARM resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists the available Event Hubs Clusters within an ARM resource group |
| `create_or_update` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Creates or updates an instance of an Event Hubs Cluster. |
| `delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes an existing Event Hubs Cluster. This operation is idempotent. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists the available Event Hubs Clusters within an ARM resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists the available Event Hubs Clusters within an ARM resource group |
| `trigger_upgrade_post` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Trigger pending cluster upgrades if any. Bypasses any upgrade preferences set by customer. |
| `update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Modifies mutable properties on the Event Hubs Cluster. This operation is idempotent. |
