---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - log_analytics
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
<tr><td><b>Id</b></td><td><code>azure.log_analytics.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Cluster properties. |
| `sku` | `object` | The cluster sku definition. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets a Log Analytics cluster instance. |
| `list` | `SELECT` | `subscriptionId` | Gets the Log Analytics clusters in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets Log Analytics clusters in a resource group. |
| `create_or_update` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Create or update a Log Analytics cluster. |
| `delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes a cluster instance. |
| `_list` | `EXEC` | `subscriptionId` | Gets the Log Analytics clusters in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets Log Analytics clusters in a resource group. |
| `update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Updates a Log Analytics cluster. |
