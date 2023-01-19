---
title: workstation_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - workstation_clusters
  - workstations
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
<tr><td><b>Name</b></td><td><code>workstation_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workstations.workstation_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Full name of this resource. |
| `displayName` | `string` | Human-readable name for this resource. |
| `privateClusterConfig` | `object` | Configuration options for private clusters. |
| `network` | `string` | Immutable. Name of the Compute Engine network in which instances associated with this cluster will be created. |
| `deleteTime` | `string` | Output only. Time when this resource was soft-deleted. |
| `updateTime` | `string` | Output only. Time when this resource was most recently updated. |
| `labels` | `object` | Client-specified labels that are applied to the resource and that are also propagated to the underlying Compute Engine resources. |
| `etag` | `string` | Checksum computed by the server. May be sent on update and delete requests to ensure that the client has an up-to-date value before proceeding. |
| `annotations` | `object` | Client-specified annotations. |
| `conditions` | `array` | Output only. Status conditions describing the current resource state. |
| `subnetwork` | `string` | Immutable. Name of the Compute Engine subnetwork in which instances associated with this cluster will be created. Must be part of the subnetwork specified for this cluster. |
| `uid` | `string` | Output only. A system-assigned unique identified for this resource. |
| `reconciling` | `boolean` | Output only. Indicates whether this resource is currently being updated to match its intended state. |
| `createTime` | `string` | Output only. Time when this resource was created. |
| `degraded` | `boolean` | Output only. Whether this resource is in degraded mode, in which case it may require user action to restore full functionality. Details can be found in the `conditions` field. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_workstationClusters_get` | `SELECT` | `locationsId, projectsId, workstationClustersId` | Returns the requested workstation cluster. |
| `projects_locations_workstationClusters_list` | `SELECT` | `locationsId, projectsId` | Returns all workstation clusters in the specified location. |
| `projects_locations_workstationClusters_create` | `INSERT` | `locationsId, projectsId` | Creates a new workstation cluster. |
| `projects_locations_workstationClusters_delete` | `DELETE` | `locationsId, projectsId, workstationClustersId` | Deletes the specified workstation cluster. |
| `projects_locations_workstationClusters_patch` | `EXEC` | `locationsId, projectsId, workstationClustersId` | Updates an existing workstation cluster. |
