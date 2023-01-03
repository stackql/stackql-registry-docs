---
title: zones
hide_title: false
hide_table_of_contents: false
keywords:
  - zones
  - dataplex
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
<tr><td><b>Name</b></td><td><code>zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The relative resource name of the zone, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}. |
| `description` | `string` | Optional. Description of the zone. |
| `resourceSpec` | `object` | Settings for resources attached as assets within a zone. |
| `state` | `string` | Output only. Current state of the zone. |
| `updateTime` | `string` | Output only. The time when the zone was last updated. |
| `uid` | `string` | Output only. System generated globally unique ID for the zone. This ID will be different if the zone is deleted and re-created with the same name. |
| `displayName` | `string` | Optional. User friendly display name. |
| `labels` | `object` | Optional. User defined labels for the zone. |
| `createTime` | `string` | Output only. The time when the zone was created. |
| `type` | `string` | Required. Immutable. The type of the zone. |
| `assetStatus` | `object` | Aggregated status of the underlying assets of a lake or zone. |
| `discoverySpec` | `object` | Settings to manage the metadata discovery and publishing in a zone. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_zones_get` | `SELECT` | `lakesId, locationsId, projectsId, zonesId` | Retrieves a zone resource. |
| `projects_locations_lakes_zones_list` | `SELECT` | `lakesId, locationsId, projectsId` | Lists zone resources in a lake. |
| `projects_locations_lakes_zones_create` | `INSERT` | `lakesId, locationsId, projectsId` | Creates a zone resource within a lake. |
| `projects_locations_lakes_zones_delete` | `DELETE` | `lakesId, locationsId, projectsId, zonesId` | Deletes a zone resource. All assets within a zone must be deleted before the zone can be deleted. |
| `projects_locations_lakes_zones_patch` | `EXEC` | `lakesId, locationsId, projectsId, zonesId` | Updates a zone resource. |
