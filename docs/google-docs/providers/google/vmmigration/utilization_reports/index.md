---
title: utilization_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - utilization_reports
  - vmmigration
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
<tr><td><b>Name</b></td><td><code>utilization_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.utilization_reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The report unique name. |
| `vms` | `array` | List of utilization information per VM. When sent as part of the request, the "vm_id" field is used in order to specify which VMs to include in the report. In that case all other fields are ignored. |
| `frameEndTime` | `string` | Output only. The point in time when the time frame ends. Notice that the time frame is counted backwards. For instance if the "frame_end_time" value is 2021/01/20 and the time frame is WEEK then the report covers the week between 2021/01/20 and 2021/01/14. |
| `vmCount` | `integer` | Output only. Total number of VMs included in the report. |
| `state` | `string` | Output only. Current state of the report. |
| `createTime` | `string` | Output only. The time the report was created (this refers to the time of the request, not the time the report creation completed). |
| `displayName` | `string` | The report display name, as assigned by the user. |
| `stateTime` | `string` | Output only. The time the state was last set. |
| `timeFrame` | `string` | Time frame of the report. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_sources_utilizationReports_get` | `SELECT` | `locationsId, projectsId, sourcesId, utilizationReportsId` | Gets a single Utilization Report. |
| `projects_locations_sources_utilizationReports_list` | `SELECT` | `locationsId, projectsId, sourcesId` | Lists Utilization Reports of the given Source. |
| `projects_locations_sources_utilizationReports_create` | `INSERT` | `locationsId, projectsId, sourcesId` | Creates a new UtilizationReport. |
| `projects_locations_sources_utilizationReports_delete` | `DELETE` | `locationsId, projectsId, sourcesId, utilizationReportsId` | Deletes a single Utilization Report. |
