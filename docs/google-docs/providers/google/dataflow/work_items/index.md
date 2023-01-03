---
title: work_items
hide_title: false
hide_table_of_contents: false
keywords:
  - work_items
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
<tr><td><b>Name</b></td><td><code>work_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataflow.work_items</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_jobs_workItems_lease` | `EXEC` | `jobId, projectId` | Leases a dataflow WorkItem to run. |
| `projects_jobs_workItems_reportStatus` | `EXEC` | `jobId, projectId` | Reports the status of dataflow WorkItems leased by a worker. |
| `projects_locations_jobs_workItems_lease` | `EXEC` | `jobId, location, projectId` | Leases a dataflow WorkItem to run. |
| `projects_locations_jobs_workItems_reportStatus` | `EXEC` | `jobId, location, projectId` | Reports the status of dataflow WorkItems leased by a worker. |
