---
title: workstations_usable
hide_title: false
hide_table_of_contents: false
keywords:
  - workstations_usable
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
<tr><td><b>Name</b></td><td><code>workstations_usable</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workstations.workstations_usable</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Full name of this workstation. |
| `etag` | `string` | Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding. |
| `reconciling` | `boolean` | Output only. Indicates whether this workstation is currently being updated to match its intended state. |
| `updateTime` | `string` | Output only. Time when this workstation was most recently updated. |
| `createTime` | `string` | Output only. Time when this workstation was created. |
| `uid` | `string` | Output only. A system-assigned unique identifier for this workstation. |
| `labels` | `object` | Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation and that are also propagated to the underlying Compute Engine resources. |
| `state` | `string` | Output only. Current state of the workstation. |
| `annotations` | `object` | Optional. Client-specified annotations. |
| `deleteTime` | `string` | Output only. Time when this workstation was soft-deleted. |
| `host` | `string` | Output only. Host to which clients can send HTTPS traffic that will be received by the workstation. Authorized traffic will be received to the workstation as HTTP on port 80. To send traffic to a different port, clients may prefix the host with the destination port in the format `&#123;port&#125;-&#123;host&#125;`. |
| `env` | `object` | Optional. Environment variables passed to the workstation container's entrypoint. |
| `displayName` | `string` | Optional. Human-readable name for this workstation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_usable` | `SELECT` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` |
| `_list_usable` | `EXEC` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` |
