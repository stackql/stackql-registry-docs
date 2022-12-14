---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - service_fabric
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
<tr><td><b>Id</b></td><td><code>azure.service_fabric.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `location` | `string` | Azure resource location. |
| `properties` | `object` | Describes the cluster resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Azure resource tags. |
| `type` | `string` | Azure resource type. |
| `etag` | `string` | Azure resource etag. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Clusters_Get` | `SELECT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Get a Service Fabric cluster resource created or in the process of being created in the specified resource group. |
| `Clusters_List` | `SELECT` | `api-version, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the subscription. |
| `Clusters_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets all Service Fabric cluster resources created or in the process of being created in the resource group. |
| `Clusters_CreateOrUpdate` | `INSERT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Create or update a Service Fabric cluster resource with the specified name. |
| `Clusters_Delete` | `DELETE` | `api-version, clusterName, resourceGroupName, subscriptionId` | Delete a Service Fabric cluster resource with the specified name. |
| `Clusters_ListUpgradableVersions` | `EXEC` | `api-version, clusterName, resourceGroupName, subscriptionId, data__targetVersion` | If a target is not provided, it will get the minimum and maximum versions available from the current cluster version. If a target is given, it will provide the required path to get from the current cluster version to the target version. |
| `Clusters_Update` | `EXEC` | `api-version, clusterName, resourceGroupName, subscriptionId` | Update the configuration of a Service Fabric cluster resource with the specified name. |
