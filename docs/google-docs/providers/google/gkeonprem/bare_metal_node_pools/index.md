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
| `name` | `string` | Immutable. The bare metal node pool resource name. |
| `displayName` | `string` | The display name for the bare metal node pool. |
| `upgradePolicy` | `object` | BareMetalNodePoolUpgradePolicy defines the node pool upgrade policy. |
| `state` | `string` | Output only. The current state of the bare metal node pool. |
| `etag` | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control. |
| `reconciling` | `boolean` | Output only. If set, there are currently changes in flight to the bare metal node pool. |
| `annotations` | `object` | Annotations on the bare metal node pool. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| `nodePoolConfig` | `object` | BareMetalNodePoolConfig describes the configuration of all nodes within a given bare metal node pool. |
| `status` | `object` | ResourceStatus describes why a cluster or node pool has a certain status. (e.g., ERROR or DEGRADED). |
| `createTime` | `string` | Output only. The time at which this bare metal node pool was created. |
| `updateTime` | `string` | Output only. The time at which this bare metal node pool was last updated. |
| `uid` | `string` | Output only. The unique identifier of the bare metal node pool. |
| `deleteTime` | `string` | Output only. The time at which this bare metal node pool was deleted. If the resource is not deleted, this must be empty |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_get` | `SELECT` | `bareMetalClustersId, bareMetalNodePoolsId, locationsId, projectsId` | Gets details of a single bare metal node pool. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_list` | `SELECT` | `bareMetalClustersId, locationsId, projectsId` | Lists bare metal node pools in a given project, location and bare metal cluster. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_create` | `INSERT` | `bareMetalClustersId, locationsId, projectsId` | Creates a new bare metal node pool in a given project, location and Bare Metal cluster. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_delete` | `DELETE` | `bareMetalClustersId, bareMetalNodePoolsId, locationsId, projectsId` | Deletes a single bare metal node pool. |
| `_projects_locations_bare_metal_clusters_bare_metal_node_pools_list` | `EXEC` | `bareMetalClustersId, locationsId, projectsId` | Lists bare metal node pools in a given project, location and bare metal cluster. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_enroll` | `EXEC` | `bareMetalClustersId, locationsId, projectsId` | Enrolls an existing bare metal node pool to the Anthos On-Prem API within a given project and location. Through enrollment, an existing node pool will become Anthos On-Prem API managed. The corresponding GCP resources will be created. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_patch` | `EXEC` | `bareMetalClustersId, bareMetalNodePoolsId, locationsId, projectsId` | Updates the parameters of a single bare metal node pool. |
| `projects_locations_bare_metal_clusters_bare_metal_node_pools_unenroll` | `EXEC` | `bareMetalClustersId, bareMetalNodePoolsId, locationsId, projectsId` | Unenrolls a bare metal node pool from Anthos On-Prem API. |
