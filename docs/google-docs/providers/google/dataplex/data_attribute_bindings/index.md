---
title: data_attribute_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - data_attribute_bindings
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
<tr><td><b>Name</b></td><td><code>data_attribute_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.data_attribute_bindings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `dataAttributeBindings` | `array` | DataAttributeBindings under the given parent Location. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `unreachableLocations` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_data_attribute_bindings_list` | `SELECT` | `locationsId, projectsId` | Lists DataAttributeBinding resources in a project and location. |
| `projects_locations_data_attribute_bindings_create` | `INSERT` | `locationsId, projectsId` | Create a DataAttributeBinding resource. |
| `projects_locations_data_attribute_bindings_delete` | `DELETE` | `dataAttributeBindingsId, locationsId, projectsId` | Deletes a DataAttributeBinding resource. All attributes within the DataAttributeBinding must be deleted before the DataAttributeBinding can be deleted. |
| `projects_locations_data_attribute_bindings_get` | `EXEC` | `dataAttributeBindingsId, locationsId, projectsId` | Retrieves a DataAttributeBinding resource. |
| `projects_locations_data_attribute_bindings_patch` | `EXEC` | `dataAttributeBindingsId, locationsId, projectsId` | Updates a DataAttributeBinding resource. |
