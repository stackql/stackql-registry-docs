---
title: route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - route_tables
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
<tr><td><b>Name</b></td><td><code>route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.route_tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The name of the route table. Route table names must be unique. They use the following form: `projects/&#123;project_number&#125;/locations/global/hubs/&#123;hub&#125;/routeTables/&#123;route_table_id&#125;` |
| `description` | `string` | An optional description of the route table. |
| `createTime` | `string` | Output only. The time the route table was created. |
| `labels` | `object` | Optional labels in key:value format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |
| `state` | `string` | Output only. The current lifecycle state of this route table. |
| `uid` | `string` | Output only. The Google-generated UUID for the route table. This value is unique across all route table resources. If a route table is deleted and another with the same name is created, the new route table is assigned a different `uid`. |
| `updateTime` | `string` | Output only. The time the route table was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hubsId, projectsId, routeTablesId` | Gets details about a Network Connectivity Center route table. |
| `list` | `SELECT` | `hubsId, projectsId` | Lists route tables in a given project. |
| `_list` | `EXEC` | `hubsId, projectsId` | Lists route tables in a given project. |
