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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `name` | `string` | Immutable. The name of the hub. Hub names must be unique. They use the following form: `projects/&#123;project_number&#125;/locations/global/hubs/&#123;hub_id&#125;` |
| `description` | `string` | An optional description of the hub. |
| `routingVpcs` | `array` | The VPC networks associated with this hub's spokes. This field is read-only. Network Connectivity Center automatically populates it based on the set of spokes attached to the hub. |
| `labels` | `object` | Optional labels in key:value format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |
| `routeTables` | `array` | Output only. The route tables that belong to this hub. They use the following form: `projects/&#123;project_number&#125;/locations/global/hubs/&#123;hub_id&#125;/routeTables/&#123;route_table_id&#125;` This field is read-only. Network Connectivity Center automatically populates it based on the route tables nested under the hub. |
| `state` | `string` | Output only. The current lifecycle state of this hub. |
| `uniqueId` | `string` | Output only. The Google-generated UUID for the hub. This value is unique across all hub resources. If a hub is deleted and another with the same name is created, the new hub is assigned a different unique_id. |
| `updateTime` | `string` | Output only. The time the hub was last updated. |
| `spokeSummary` | `object` | Summarizes information about the spokes associated with a hub. The summary includes a count of spokes according to type and according to state. If any spokes are inactive, the summary also lists the reasons they are inactive, including a count for each reason. |
| `createTime` | `string` | Output only. The time the hub was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hubsId, projectsId` | Gets details about a Network Connectivity Center hub. |
| `list` | `SELECT` | `projectsId` | Lists the Network Connectivity Center hubs associated with a given project. |
| `create` | `INSERT` | `projectsId` | Creates a new Network Connectivity Center hub in the specified project. |
| `delete` | `DELETE` | `hubsId, projectsId` | Deletes a Network Connectivity Center hub. |
| `_list` | `EXEC` | `projectsId` | Lists the Network Connectivity Center hubs associated with a given project. |
| `patch` | `EXEC` | `hubsId, projectsId` | Updates the description and/or labels of a Network Connectivity Center hub. |
