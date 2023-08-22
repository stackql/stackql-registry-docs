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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `name` | `string` | Output only. The relative resource name of the zone, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/lakes/&#123;lake_id&#125;/zones/&#123;zone_id&#125;. |
| `description` | `string` | Optional. Description of the zone. |
| `resourceSpec` | `object` | Settings for resources attached as assets within a zone. |
| `displayName` | `string` | Optional. User friendly display name. |
| `discoverySpec` | `object` | Settings to manage the metadata discovery and publishing in a zone. |
| `labels` | `object` | Optional. User defined labels for the zone. |
| `assetStatus` | `object` | Aggregated status of the underlying assets of a lake or zone. |
| `updateTime` | `string` | Output only. The time when the zone was last updated. |
| `createTime` | `string` | Output only. The time when the zone was created. |
| `state` | `string` | Output only. Current state of the zone. |
| `type` | `string` | Required. Immutable. The type of the zone. |
| `uid` | `string` | Output only. System generated globally unique ID for the zone. This ID will be different if the zone is deleted and re-created with the same name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_zones_get` | `SELECT` | `lakesId, locationsId, projectsId, zonesId` | Retrieves a zone resource. |
| `projects_locations_lakes_zones_list` | `SELECT` | `lakesId, locationsId, projectsId` | Lists zone resources in a lake. |
| `projects_locations_lakes_zones_create` | `INSERT` | `lakesId, locationsId, projectsId` | Creates a zone resource within a lake. |
| `projects_locations_lakes_zones_delete` | `DELETE` | `lakesId, locationsId, projectsId, zonesId` | Deletes a zone resource. All assets within a zone must be deleted before the zone can be deleted. |
| `_projects_locations_lakes_zones_list` | `EXEC` | `lakesId, locationsId, projectsId` | Lists zone resources in a lake. |
| `projects_locations_lakes_zones_patch` | `EXEC` | `lakesId, locationsId, projectsId, zonesId` | Updates a zone resource. |
