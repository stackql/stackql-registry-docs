---
title: attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - attributes
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
<tr><td><b>Name</b></td><td><code>attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.attributes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `dataAttributes` | `array` | DataAttributes under the given parent DataTaxonomy. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `unreachableLocations` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_data_taxonomies_attributes_list` | `SELECT` | `dataTaxonomiesId, locationsId, projectsId` | Lists Data Attribute resources in a DataTaxonomy. |
| `projects_locations_data_taxonomies_attributes_create` | `INSERT` | `dataTaxonomiesId, locationsId, projectsId` | Create a DataAttribute resource. |
| `projects_locations_data_taxonomies_attributes_delete` | `DELETE` | `attributesId, dataTaxonomiesId, locationsId, projectsId` | Deletes a Data Attribute resource. |
| `projects_locations_data_taxonomies_attributes_get` | `EXEC` | `attributesId, dataTaxonomiesId, locationsId, projectsId` | Retrieves a Data Attribute resource. |
| `projects_locations_data_taxonomies_attributes_patch` | `EXEC` | `attributesId, dataTaxonomiesId, locationsId, projectsId` | Updates a DataAttribute resource. |
