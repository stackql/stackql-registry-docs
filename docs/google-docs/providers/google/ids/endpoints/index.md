---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - ids
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
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.ids.endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the endpoint. |
| `description` | `string` | User-provided description of the endpoint |
| `network` | `string` | Required. The fully qualified URL of the network to which the IDS Endpoint is attached. |
| `createTime` | `string` | Output only. The create time timestamp. |
| `endpointIp` | `string` | Output only. The IP address of the IDS Endpoint's ILB. |
| `labels` | `object` | The labels of the endpoint. |
| `severity` | `string` | Required. Lowest threat severity that this endpoint will alert on. |
| `state` | `string` | Output only. Current state of the endpoint. |
| `trafficLogs` | `boolean` | Whether the endpoint should report traffic logs in addition to threat logs. |
| `updateTime` | `string` | Output only. The update time timestamp. |
| `endpointForwardingRule` | `string` | Output only. The fully qualified URL of the endpoint's ILB Forwarding Rule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_endpoints_get` | `SELECT` | `endpointsId, locationsId, projectsId` | Gets details of a single Endpoint. |
| `projects_locations_endpoints_list` | `SELECT` | `locationsId, projectsId` | Lists Endpoints in a given project and location. |
| `projects_locations_endpoints_create` | `INSERT` | `locationsId, projectsId` | Creates a new Endpoint in a given project and location. |
| `projects_locations_endpoints_delete` | `DELETE` | `endpointsId, locationsId, projectsId` | Deletes a single Endpoint. |
