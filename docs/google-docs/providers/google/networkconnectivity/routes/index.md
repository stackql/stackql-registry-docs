---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
  - networkconnectivity
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
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The name of the route. Route names must be unique. Route names use the following form: `projects/&#123;project_number&#125;/locations/global/hubs/&#123;hub&#125;/routeTables/&#123;route_table_id&#125;/routes/&#123;route_id&#125;` |
| `description` | `string` | An optional description of the route. |
| `createTime` | `string` | Output only. The time the route was created. |
| `state` | `string` | Output only. The current lifecycle state of the route. |
| `updateTime` | `string` | Output only. The time the route was last updated. |
| `labels` | `object` | Optional labels in key:value format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |
| `uid` | `string` | Output only. The Google-generated UUID for the route. This value is unique across all Network Connectivity Center route resources. If a route is deleted and another with the same name is created, the new route is assigned a different `uid`. |
| `location` | `string` | Output only. The location of the route. Uses the following form: "projects/&#123;project&#125;/locations/&#123;location&#125;" Example: projects/1234/locations/us-central1 |
| `nextHopVpcNetwork` | `object` |  |
| `spoke` | `string` | Immutable. The spoke that this route leads to. Example: projects/12345/locations/global/spokes/SPOKE |
| `type` | `string` | Output only. The route's type. Its type is determined by the properties of its IP address range. |
| `ipCidrRange` | `string` | The destination IP address range. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hubsId, projectsId, routeTablesId, routesId` | Gets details about the specified route. |
| `list` | `SELECT` | `hubsId, projectsId, routeTablesId` | Lists routes in a given project. |
| `_list` | `EXEC` | `hubsId, projectsId, routeTablesId` | Lists routes in a given project. |
