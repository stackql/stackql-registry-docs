---
title: hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - hubs
  - networkconnectivity
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
<tr><td><b>Name</b></td><td><code>hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networkconnectivity.hubs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The name of the hub. Hub names must be unique. They use the following form: `projects/{project_number}/locations/global/hubs/{hub_id}` |
| `description` | `string` | An optional description of the hub. |
| `labels` | `object` | Optional labels in key:value format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |
| `routingVpcs` | `array` | The VPC networks associated with this hub's spokes. This field is read-only. Network Connectivity Center automatically populates it based on the set of spokes attached to the hub. |
| `state` | `string` | Output only. The current lifecycle state of this hub. |
| `uniqueId` | `string` | Output only. The Google-generated UUID for the hub. This value is unique across all hub resources. If a hub is deleted and another with the same name is created, the new hub is assigned a different unique_id. |
| `updateTime` | `string` | Output only. The time the hub was last updated. |
| `createTime` | `string` | Output only. The time the hub was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_global_hubs_get` | `SELECT` | `hubsId, projectsId` | Gets details about the specified hub. |
| `projects_locations_global_hubs_list` | `SELECT` | `projectsId` | Lists hubs in a given project. |
| `projects_locations_global_hubs_create` | `INSERT` | `projectsId` | Creates a new hub in the specified project. |
| `projects_locations_global_hubs_delete` | `DELETE` | `hubsId, projectsId` | Deletes the specified hub. |
| `projects_locations_global_hubs_patch` | `EXEC` | `hubsId, projectsId` | Updates the description and/or labels of the specified hub. |
