---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
  - ml
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
<tr><td><b>Id</b></td><td><code>google.ml.models</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `models` | `array` | The list of models. |
| `nextPageToken` | `string` | Optional. Pass this token as the `page_token` field of the request for a subsequent call. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_models_list` | `SELECT` | `projectsId` | Lists the models in a project. Each project can contain multiple models, and each model can have multiple versions. If there are no models that match the request parameters, the list request returns an empty response body: &#123;&#125;. |
| `projects_models_create` | `INSERT` | `projectsId` | Creates a model which will later contain one or more versions. You must add at least one version before you can request predictions from the model. Add versions by calling projects.models.versions.create. |
| `projects_models_delete` | `DELETE` | `modelsId, projectsId` | Deletes a model. You can only delete a model if there are no versions in it. You can delete versions by calling projects.models.versions.delete. |
| `projects_models_get` | `EXEC` | `modelsId, projectsId` | Gets information about a model, including its name, the description (if set), and the default version (if at least one version of the model has been deployed). |
| `projects_models_patch` | `EXEC` | `modelsId, projectsId` | Updates a specific model resource. Currently the only supported fields to update are `description` and `default_version.name`. |
