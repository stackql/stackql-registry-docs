---
title: managed_cluster_version
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_cluster_version
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
<tr><td><b>Name</b></td><td><code>managed_cluster_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_managed_clusters.managed_cluster_version</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identification of the result |
| `name` | `string` | The name of the result |
| `properties` | `object` | The detail of the Service Fabric runtime version result |
| `type` | `string` | The result resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedClusterVersion_Get` | `SELECT` | `api-version, clusterVersion, location, subscriptionId` | Gets information about an available Service Fabric managed cluster code version. |
| `ManagedClusterVersion_List` | `SELECT` | `api-version, location, subscriptionId` | Gets all available code versions for Service Fabric cluster resources by location. |
| `ManagedClusterVersion_ListByEnvironment` | `SELECT` | `api-version, environment, location, subscriptionId` | Gets all available code versions for Service Fabric cluster resources by environment. |
| `ManagedClusterVersion_GetByEnvironment` | `EXEC` | `api-version, clusterVersion, environment, location, subscriptionId` | Gets information about an available Service Fabric cluster code version by environment. |
