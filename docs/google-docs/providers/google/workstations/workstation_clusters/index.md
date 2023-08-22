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
| `name` | `string` | Full name of this workstation cluster. |
| `etag` | `string` | Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding. |
| `controlPlaneIp` | `string` | Output only. The private IP address of the control plane for this workstation cluster. Workstation VMs need access to this IP address to work with the service, so make sure that your firewall rules allow egress from the workstation VMs to this address. |
| `labels` | `object` | Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation cluster and that are also propagated to the underlying Compute Engine resources. |
| `reconciling` | `boolean` | Output only. Indicates whether this workstation cluster is currently being updated to match its intended state. |
| `privateClusterConfig` | `object` | Configuration options for private workstation clusters. |
| `subnetwork` | `string` | Immutable. Name of the Compute Engine subnetwork in which instances associated with this workstation cluster will be created. Must be part of the subnetwork specified for this workstation cluster. |
| `annotations` | `object` | Optional. Client-specified annotations. |
| `deleteTime` | `string` | Output only. Time when this workstation cluster was soft-deleted. |
| `createTime` | `string` | Output only. Time when this workstation cluster was created. |
| `conditions` | `array` | Output only. Status conditions describing the workstation cluster's current state. |
| `uid` | `string` | Output only. A system-assigned unique identifier for this workstation cluster. |
| `degraded` | `boolean` | Output only. Whether this workstation cluster is in degraded mode, in which case it may require user action to restore full functionality. Details can be found in conditions. |
| `displayName` | `string` | Optional. Human-readable name for this workstation cluster. |
| `network` | `string` | Immutable. Name of the Compute Engine network in which instances associated with this workstation cluster will be created. |
| `updateTime` | `string` | Output only. Time when this workstation cluster was most recently updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, workstationClustersId` | Returns the requested workstation cluster. |
| `list` | `SELECT` | `locationsId, projectsId` | Returns all workstation clusters in the specified location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new workstation cluster. |
| `delete` | `DELETE` | `locationsId, projectsId, workstationClustersId` | Deletes the specified workstation cluster. |
| `_list` | `EXEC` | `locationsId, projectsId` | Returns all workstation clusters in the specified location. |
| `patch` | `EXEC` | `locationsId, projectsId, workstationClustersId` | Updates an existing workstation cluster. |
