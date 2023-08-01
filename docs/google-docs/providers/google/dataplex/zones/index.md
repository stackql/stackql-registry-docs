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
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `zones` | `array` | Zones under the given parent lake. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_zones_list` | `SELECT` | `lakesId, locationsId, projectsId` | Lists zone resources in a lake. |
| `projects_locations_lakes_zones_create` | `INSERT` | `lakesId, locationsId, projectsId` | Creates a zone resource within a lake. |
| `projects_locations_lakes_zones_delete` | `DELETE` | `lakesId, locationsId, projectsId, zonesId` | Deletes a zone resource. All assets within a zone must be deleted before the zone can be deleted. |
| `projects_locations_lakes_zones_get` | `EXEC` | `lakesId, locationsId, projectsId, zonesId` | Retrieves a zone resource. |
| `projects_locations_lakes_zones_patch` | `EXEC` | `lakesId, locationsId, projectsId, zonesId` | Updates a zone resource. |
