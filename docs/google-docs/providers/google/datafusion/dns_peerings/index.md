---
title: dns_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_peerings
  - datafusion
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
<tr><td><b>Name</b></td><td><code>dns_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datafusion.dns_peerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the dns peering zone. Format: projects/{project}/locations/{location}/instances/{instance}/dnsPeerings/{dns_peering} |
| `description` | `string` | Optional. Optional description of the dns zone. |
| `targetNetwork` | `string` | Optional. Optional target network to which dns peering should happen. |
| `targetProject` | `string` | Optional. Optional target project to which dns peering should happen. |
| `domain` | `string` | Required. The dns name suffix of the zone. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_instances_dnsPeerings_list` | `SELECT` | `instancesId, locationsId, projectsId` | Lists DNS peerings for a given resource. |
| `projects_locations_instances_dnsPeerings_create` | `INSERT` | `instancesId, locationsId, projectsId` | Creates DNS peering on the given resource. |
| `projects_locations_instances_dnsPeerings_delete` | `DELETE` | `dnsPeeringsId, instancesId, locationsId, projectsId` | Deletes DNS peering on the given resource. |
