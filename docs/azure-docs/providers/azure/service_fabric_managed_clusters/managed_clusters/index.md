---
title: managed_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters
  - service_fabric_managed_clusters
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
<tr><td><b>Name</b></td><td><code>managed_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_managed_clusters.managed_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `etag` | `string` | Azure resource etag. |
| `location` | `string` | Azure resource location. |
| `properties` | `object` | Describes the managed cluster resource properties. |
| `sku` | `object` | Service Fabric managed cluster Sku definition |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Azure resource tags. |
| `type` | `string` | Azure resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Get a Service Fabric managed cluster resource created or in the process of being created in the specified resource group. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the resource group. |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the subscription. |
| `create_or_update` | `INSERT` | `api-version, clusterName, resourceGroupName, subscriptionId, data__sku` | Create or update a Service Fabric managed cluster resource with the specified name. |
| `delete` | `DELETE` | `api-version, clusterName, resourceGroupName, subscriptionId` | Delete a Service Fabric managed cluster resource with the specified name. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the resource group. |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the subscription. |
| `update` | `EXEC` | `api-version, clusterName, resourceGroupName, subscriptionId` | Update the tags of of a Service Fabric managed cluster resource with the specified name. |
