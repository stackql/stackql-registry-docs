---
title: data_taxonomies
hide_title: false
hide_table_of_contents: false
keywords:
  - data_taxonomies
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
<tr><td><b>Name</b></td><td><code>data_taxonomies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.data_taxonomies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachableLocations` | `array` | Locations that could not be reached. |
| `dataTaxonomies` | `array` | DataTaxonomies under the given parent location. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_data_taxonomies_list` | `SELECT` | `locationsId, projectsId` | Lists DataTaxonomy resources in a project and location. |
| `projects_locations_data_taxonomies_create` | `INSERT` | `locationsId, projectsId` | Create a DataTaxonomy resource. |
| `projects_locations_data_taxonomies_delete` | `DELETE` | `dataTaxonomiesId, locationsId, projectsId` | Deletes a DataTaxonomy resource. All attributes within the DataTaxonomy must be deleted before the DataTaxonomy can be deleted. |
| `projects_locations_data_taxonomies_get` | `EXEC` | `dataTaxonomiesId, locationsId, projectsId` | Retrieves a DataTaxonomy resource. |
| `projects_locations_data_taxonomies_patch` | `EXEC` | `dataTaxonomiesId, locationsId, projectsId` | Updates a DataTaxonomy resource. |
