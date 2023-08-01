---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
  - retail
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
<tr><td><b>Id</b></td><td><code>google.retail.models</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `models` | `array` | List of Models. |
| `nextPageToken` | `string` | Pagination token, if not returned indicates the last page. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_models_get` | `SELECT` | `catalogsId, locationsId, modelsId, projectsId` | Gets a model. |
| `projects_locations_catalogs_models_list` | `SELECT` | `catalogsId, locationsId, projectsId` | Lists all the models linked to this event store. |
| `projects_locations_catalogs_models_create` | `INSERT` | `catalogsId, locationsId, projectsId` | Creates a new model. |
| `projects_locations_catalogs_models_delete` | `DELETE` | `catalogsId, locationsId, modelsId, projectsId` | Deletes an existing model. |
| `projects_locations_catalogs_models_patch` | `EXEC` | `catalogsId, locationsId, modelsId, projectsId` | Update of model metadata. Only fields that currently can be updated are: `filtering_option` and `periodic_tuning_state`. If other values are provided, this API method ignores them. |
| `projects_locations_catalogs_models_pause` | `EXEC` | `catalogsId, locationsId, modelsId, projectsId` | Pauses the training of an existing model. |
| `projects_locations_catalogs_models_resume` | `EXEC` | `catalogsId, locationsId, modelsId, projectsId` | Resumes the training of an existing model. |
| `projects_locations_catalogs_models_tune` | `EXEC` | `catalogsId, locationsId, modelsId, projectsId` | Tunes an existing model. |
