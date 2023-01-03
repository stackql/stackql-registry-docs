---
title: peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - peerings
  - managedidentities
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
<tr><td><b>Name</b></td><td><code>peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.managedidentities.peerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Unique name of the peering in this scope including projects and location using the form: `projects/{project_id}/locations/global/peerings/{peering_id}`. |
| `state` | `string` | Output only. The current state of this Peering. |
| `statusMessage` | `string` | Output only. Additional information about the current status of this peering, if available. |
| `updateTime` | `string` | Output only. Last update time. |
| `authorizedNetwork` | `string` | Required. The full names of the Google Compute Engine [networks](/compute/docs/networks-and-firewalls#networks) to which the instance is connected. Caller needs to make sure that CIDR subnets do not overlap between networks, else peering creation will fail. |
| `createTime` | `string` | Output only. The time the instance was created. |
| `domainResource` | `string` | Required. Full domain resource path for the Managed AD Domain involved in peering. The resource path should be in the form: `projects/{project_id}/locations/global/domains/{domain_name}` |
| `labels` | `object` | Optional. Resource labels to represent user-provided metadata. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_global_peerings_get` | `SELECT` | `peeringsId, projectsId` | Gets details of a single Peering. |
| `projects_locations_global_peerings_list` | `SELECT` | `projectsId` | Lists Peerings in a given project. |
| `projects_locations_global_peerings_create` | `INSERT` | `projectsId` | Creates a Peering for Managed AD instance. |
| `projects_locations_global_peerings_delete` | `DELETE` | `peeringsId, projectsId` | Deletes identified Peering. |
| `projects_locations_global_peerings_patch` | `EXEC` | `peeringsId, projectsId` | Updates the labels for specified Peering. |
