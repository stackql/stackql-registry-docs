---
title: workstations
hide_title: false
hide_table_of_contents: false
keywords:
  - workstations
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
<tr><td><b>Name</b></td><td><code>workstations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workstations.workstations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Full name of this workstation. |
| `annotations` | `object` | Optional. Client-specified annotations. |
| `updateTime` | `string` | Output only. Time when this workstation was most recently updated. |
| `deleteTime` | `string` | Output only. Time when this workstation was soft-deleted. |
| `etag` | `string` | Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding. |
| `labels` | `object` | Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation and that are also propagated to the underlying Compute Engine resources. |
| `reconciling` | `boolean` | Output only. Indicates whether this workstation is currently being updated to match its intended state. |
| `displayName` | `string` | Optional. Human-readable name for this workstation. |
| `env` | `object` | Optional. Environment variables passed to the workstation container's entrypoint. |
| `uid` | `string` | Output only. A system-assigned unique identifier for this workstation. |
| `host` | `string` | Output only. Host to which clients can send HTTPS traffic that will be received by the workstation. Authorized traffic will be received to the workstation as HTTP on port 80. To send traffic to a different port, clients may prefix the host with the destination port in the format `&#123;port&#125;-&#123;host&#125;`. |
| `createTime` | `string` | Output only. Time when this workstation was created. |
| `state` | `string` | Output only. Current state of the workstation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId` | Returns the requested workstation. |
| `list` | `SELECT` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Returns all Workstations using the specified workstation configuration. |
| `create` | `INSERT` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Creates a new workstation. |
| `delete` | `DELETE` | `locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId` | Deletes the specified workstation. |
| `_list` | `EXEC` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Returns all Workstations using the specified workstation configuration. |
| `generate_access_token` | `EXEC` | `locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId` | Returns a short-lived credential that can be used to send authenticated and authorized traffic to a workstation. |
| `patch` | `EXEC` | `locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId` | Updates an existing workstation. |
| `start` | `EXEC` | `locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId` | Starts running a workstation so that users can connect to it. |
| `stop` | `EXEC` | `locationsId, projectsId, workstationClustersId, workstationConfigsId, workstationsId` | Stops running a workstation, reducing costs. |
