---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - dataflow
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataflow.snapshots</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID of this snapshot. |
| `description` | `string` | User specified description of the snapshot. Maybe empty. |
| `diskSizeBytes` | `string` | The disk byte size of the snapshot. Only available for snapshots in READY state. |
| `creationTime` | `string` | The time this snapshot was created. |
| `state` | `string` | State of the snapshot. |
| `region` | `string` | Cloud region where this snapshot lives in, e.g., "us-central1". |
| `ttl` | `string` | The time after which this snapshot will be automatically deleted. |
| `pubsubMetadata` | `array` | Pub/Sub snapshot metadata. |
| `sourceJobId` | `string` | The job this snapshot was created from. |
| `projectId` | `string` | The project this snapshot belongs to. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_jobs_snapshots_list` | `SELECT` | `jobId, location, projectId` | Lists snapshots. |
| `projects_locations_snapshots_get` | `SELECT` | `location, projectId, snapshotId` | Gets information about a snapshot. |
| `projects_locations_snapshots_list` | `SELECT` | `location, projectId` | Lists snapshots. |
| `projects_snapshots_get` | `SELECT` | `projectId, snapshotId` | Gets information about a snapshot. |
| `projects_snapshots_list` | `SELECT` | `projectId` | Lists snapshots. |
| `projects_locations_snapshots_delete` | `DELETE` | `location, projectId, snapshotId` | Deletes a snapshot. |
