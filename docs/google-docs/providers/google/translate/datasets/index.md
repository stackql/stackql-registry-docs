---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
  - translate
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
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.translate.datasets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `datasets` | `array` | The datasets read. |
| `nextPageToken` | `string` | A token to retrieve next page of results. Pass this token to the page_token field in the ListDatasetsRequest to obtain the corresponding page. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_datasets_get` | `SELECT` | `datasetsId, locationsId, projectsId` | Gets a Dataset. |
| `projects_locations_datasets_list` | `SELECT` | `locationsId, projectsId` | Lists datasets. |
| `projects_locations_datasets_create` | `INSERT` | `locationsId, projectsId` | Creates a Dataset. |
| `projects_locations_datasets_delete` | `DELETE` | `datasetsId, locationsId, projectsId` | Deletes a dataset and all of its contents. |
| `projects_locations_datasets_export_data` | `EXEC` | `datasetsId, locationsId, projectsId` | Exports dataset's data to the provided output location. |
| `projects_locations_datasets_import_data` | `EXEC` | `datasetsId, locationsId, projectsId` | Import sentence pairs into translation Dataset. |
