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
| `location` | `string` | Resource location. |
| `properties` | `object` | The properties of a virtual cluster. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, virtualClusterName` | Gets a virtual cluster. |
| `list` | `SELECT` | `subscriptionId` | Gets a list of all virtualClusters in the subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of virtual clusters in a resource group. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualClusterName` | Deletes a virtual cluster. |
| `_list` | `EXEC` | `subscriptionId` | Gets a list of all virtualClusters in the subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of virtual clusters in a resource group. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, virtualClusterName` | Updates an existing virtual cluster. |
