---
title: bare_metal_node_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - bare_metal_node_pools
  - gkeonprem
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bare_metal_node_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkeonprem.bare_metal_node_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `unreachable` | `array` | Locations that could not be reached. |
| `bareMetalNodePools` | `array` | The node pools from the specified parent resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_list` | `SELECT` | `bareMetalClustersId, locationsId, projectsId` | Lists bare metal node pools in a given project, location and bare metal cluster. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_create` | `INSERT` | `bareMetalClustersId, locationsId, projectsId` | Creates a new bare metal node pool in a given project, location and Bare Metal cluster. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_delete` | `DELETE` | `bareMetalClustersId, bareMetalNodePoolsId, locationsId, projectsId` | Deletes a single bare metal node pool. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_enroll` | `EXEC` | `bareMetalClustersId, locationsId, projectsId` | Enrolls an existing bare metal node pool to the Anthos On-Prem API within a given project and location. Through enrollment, an existing node pool will become Anthos On-Prem API managed. The corresponding GCP resources will be created. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_get` | `EXEC` | `bareMetalClustersId, bareMetalNodePoolsId, locationsId, projectsId` | Gets details of a single bare metal node pool. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_patch` | `EXEC` | `bareMetalClustersId, bareMetalNodePoolsId, locationsId, projectsId` | Updates the parameters of a single bare metal node pool. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_unenroll` | `EXEC` | `bareMetalClustersId, bareMetalNodePoolsId, locationsId, projectsId` | Unenrolls a bare metal node pool from Anthos On-Prem API. |
