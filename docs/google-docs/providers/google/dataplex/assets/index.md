---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
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
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.assets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `assets` | `array` | Asset under the given parent zone. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_zones_assets_list` | `SELECT` | `lakesId, locationsId, projectsId, zonesId` | Lists asset resources in a zone. |
| `projects_locations_lakes_zones_assets_create` | `INSERT` | `lakesId, locationsId, projectsId, zonesId` | Creates an asset resource. |
| `projects_locations_lakes_zones_assets_delete` | `DELETE` | `assetsId, lakesId, locationsId, projectsId, zonesId` | Deletes an asset resource. The referenced storage resource is detached (default) or deleted based on the associated Lifecycle policy. |
| `projects_locations_lakes_zones_assets_get` | `EXEC` | `assetsId, lakesId, locationsId, projectsId, zonesId` | Retrieves an asset resource. |
| `projects_locations_lakes_zones_assets_patch` | `EXEC` | `assetsId, lakesId, locationsId, projectsId, zonesId` | Updates an asset resource. |
