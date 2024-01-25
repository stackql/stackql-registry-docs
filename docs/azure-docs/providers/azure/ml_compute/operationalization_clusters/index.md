---
title: operationalization_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - operationalization_clusters
  - ml_compute
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
<tr><td><b>Name</b></td><td><code>operationalization_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_compute.operationalization_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the resource ID. |
| `name` | `string` | Specifies the name of the resource. |
| `location` | `string` | Specifies the location of the resource. |
| `properties` | `object` | Properties of an operationalization cluster |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
| `type` | `string` | Specifies the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets the operationalization cluster resource view. Note that the credentials are not returned by this call. Call ListKeys to get them. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the clusters in the specified resource group. |
| `list_by_subscription_id` | `SELECT` | `subscriptionId` | Gets the operationalization clusters in the specified subscription. |
| `create_or_update` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Create or update an operationalization cluster. |
| `delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes the specified cluster. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets the clusters in the specified resource group. |
| `_list_by_subscription_id` | `EXEC` | `subscriptionId` | Gets the operationalization clusters in the specified subscription. |
| `check_system_services_updates_available` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Checks if updates are available for system services in the cluster. |
| `update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | The PATCH operation can be used to update only the tags for a cluster. Use PUT operation to update other properties. |
