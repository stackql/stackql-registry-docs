---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
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
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.translate.models</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `models` | `array` | The models read. |
| `nextPageToken` | `string` | A token to retrieve next page of results. Pass this token to the page_token field in the ListModelsRequest to obtain the corresponding page. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_models_get` | `SELECT` | `locationsId, modelsId, projectsId` | Gets a model. |
| `projects_locations_models_list` | `SELECT` | `locationsId, projectsId` | Lists models. |
| `projects_locations_models_create` | `INSERT` | `locationsId, projectsId` | Creates a Model. |
| `projects_locations_models_delete` | `DELETE` | `locationsId, modelsId, projectsId` | Deletes a model. |
