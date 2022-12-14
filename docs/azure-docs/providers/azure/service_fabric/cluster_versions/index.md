---
title: cluster_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_versions
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
<tr><td><b>Name</b></td><td><code>cluster_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric.cluster_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | The URL to use for getting the next set of results. |
| `value` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ClusterVersions_Get` | `SELECT` | `api-version, clusterVersion, location, subscriptionId` | Gets information about an available Service Fabric cluster code version. |
| `ClusterVersions_List` | `SELECT` | `api-version, location, subscriptionId` | Gets all available code versions for Service Fabric cluster resources by location. |
| `ClusterVersions_ListByEnvironment` | `SELECT` | `api-version, environment, location, subscriptionId` | Gets all available code versions for Service Fabric cluster resources by environment. |
| `ClusterVersions_GetByEnvironment` | `EXEC` | `api-version, clusterVersion, environment, location, subscriptionId` | Gets information about an available Service Fabric cluster code version by environment. |
