---
title: workstation_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - workstation_configs
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
<tr><td><b>Name</b></td><td><code>workstation_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workstations.workstation_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Full name of this resource. |
| `createTime` | `string` | Output only. Time when this resource was created. |
| `uid` | `string` | Output only. A system-assigned unique identified for this resource. |
| `container` | `object` | A Docker container. |
| `displayName` | `string` | Human-readable name for this resource. |
| `updateTime` | `string` | Output only. Time when this resource was most recently updated. |
| `idleTimeout` | `string` | How long to wait before automatically stopping an instance that hasn't received any user traffic. A value of 0 indicates that this instance should never time out due to idleness. Defaults to 20 minutes. |
| `degraded` | `boolean` | Output only. Whether this resource is in degraded mode, in which case it may require user action to restore full functionality. Details can be found in the `conditions` field. |
| `runningTimeout` | `string` | How long to wait before automatically stopping a workstation after it started. A value of 0 indicates that workstations using this config should never time out. Must be greater than 0 and less than 24 hours if encryption_key is set. Defaults to 12 hours. |
| `conditions` | `array` | Output only. Status conditions describing the current resource state. |
| `reconciling` | `boolean` | Output only. Indicates whether this resource is currently being updated to match its intended state. |
| `persistentDirectories` | `array` | Directories to persist across workstation sessions. |
| `etag` | `string` | Checksum computed by the server. May be sent on update and delete requests to ensure that the client has an up-to-date value before proceeding. |
| `host` | `object` | Runtime host for a workstation. |
| `annotations` | `object` | Client-specified annotations. |
| `deleteTime` | `string` | Output only. Time when this resource was soft-deleted. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_workstationClusters_workstationConfigs_get` | `SELECT` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Returns the requested workstation configuration. |
| `projects_locations_workstationClusters_workstationConfigs_list` | `SELECT` | `locationsId, projectsId, workstationClustersId` | Returns all workstation configurations in the specified cluster. |
| `projects_locations_workstationClusters_workstationConfigs_create` | `INSERT` | `locationsId, projectsId, workstationClustersId` | Creates a new workstation configuration. |
| `projects_locations_workstationClusters_workstationConfigs_delete` | `DELETE` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Deletes the specified workstation configuration. |
| `projects_locations_workstationClusters_workstationConfigs_patch` | `EXEC` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Updates an existing workstation configuration. |
