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
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataflow.snapshots</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_jobs_snapshots_list` | `SELECT` | `jobId, location, projectId` | Lists snapshots. |
| `projects_locations_snapshots_get` | `SELECT` | `location, projectId, snapshotId` | Gets information about a snapshot. |
| `projects_locations_snapshots_list` | `SELECT` | `location, projectId` | Lists snapshots. |
| `projects_snapshots_get` | `SELECT` | `projectId, snapshotId` | Gets information about a snapshot. |
| `projects_snapshots_list` | `SELECT` | `projectId` | Lists snapshots. |
| `projects_delete_snapshots` | `DELETE` | `projectId` | Deletes a snapshot. |
| `projects_locations_snapshots_delete` | `DELETE` | `location, projectId, snapshotId` | Deletes a snapshot. |
