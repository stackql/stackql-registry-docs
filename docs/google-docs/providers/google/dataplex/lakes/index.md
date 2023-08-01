---
title: lakes
hide_title: false
hide_table_of_contents: false
keywords:
  - lakes
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
<tr><td><b>Name</b></td><td><code>lakes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.lakes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachableLocations` | `array` | Locations that could not be reached. |
| `lakes` | `array` | Lakes under the given parent location. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_list` | `SELECT` | `locationsId, projectsId` | Lists lake resources in a project and location. |
| `projects_locations_lakes_create` | `INSERT` | `locationsId, projectsId` | Creates a lake resource. |
| `projects_locations_lakes_delete` | `DELETE` | `lakesId, locationsId, projectsId` | Deletes a lake resource. All zones within the lake must be deleted before the lake can be deleted. |
| `projects_locations_lakes_get` | `EXEC` | `lakesId, locationsId, projectsId` | Retrieves a lake resource. |
| `projects_locations_lakes_patch` | `EXEC` | `lakesId, locationsId, projectsId` | Updates a lake resource. |
