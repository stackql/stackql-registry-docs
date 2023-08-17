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
| `name` | `string` | Required. The fully qualified resource name of the model. Format: `projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/catalogs/&#123;catalog_id&#125;/models/&#123;model_id&#125;` catalog_id has char limit of 50. recommendation_model_id has char limit of 40. |
| `type` | `string` | Required. The type of model e.g. `home-page`. Currently supported values: `recommended-for-you`, `others-you-may-like`, `frequently-bought-together`, `page-optimization`, `similar-items`, `buy-it-again`, `on-sale-items`, and `recently-viewed`(readonly value). This field together with optimization_objective describe model metadata to use to control model training and serving. See https://cloud.google.com/retail/docs/models for more details on what the model metadata control and which combination of parameters are valid. For invalid combinations of parameters (e.g. type = `frequently-bought-together` and optimization_objective = `ctr`), you receive an error 400 if you try to create/update a recommendation with this set of knobs. |
| `periodicTuningState` | `string` | Optional. The state of periodic tuning. The period we use is 3 months - to do a one-off tune earlier use the `TuneModel` method. Default value is `PERIODIC_TUNING_ENABLED`. |
| `displayName` | `string` | Required. The display name of the model. Should be human readable, used to display Recommendation Models in the Retail Cloud Console Dashboard. UTF-8 encoded string with limit of 1024 characters. |
| `servingConfigLists` | `array` | Output only. The list of valid serving configs associated with the PageOptimizationConfig. |
| `servingState` | `string` | Output only. The serving state of the model: `ACTIVE`, `NOT_ACTIVE`. |
| `createTime` | `string` | Output only. Timestamp the Recommendation Model was created at. |
| `dataState` | `string` | Output only. The state of data requirements for this model: `DATA_OK` and `DATA_ERROR`. Recommendation model cannot be trained if the data is in `DATA_ERROR` state. Recommendation model can have `DATA_ERROR` state even if serving state is `ACTIVE`: models were trained successfully before, but cannot be refreshed because model no longer has sufficient data for training. |
| `filteringOption` | `string` | Optional. If `RECOMMENDATIONS_FILTERING_ENABLED`, recommendation filtering by attributes is enabled for the model. |
| `tuningOperation` | `string` | Output only. The tune operation associated with the model. Can be used to determine if there is an ongoing tune for this recommendation. Empty field implies no tune is goig on. |
| `modelFeaturesConfig` | `object` | Additional model features config. |
| `lastTuneTime` | `string` | Output only. The timestamp when the latest successful tune finished. |
| `updateTime` | `string` | Output only. Timestamp the Recommendation Model was last updated. E.g. if a Recommendation Model was paused - this would be the time the pause was initiated. |
| `optimizationObjective` | `string` | Optional. The optimization objective e.g. `cvr`. Currently supported values: `ctr`, `cvr`, `revenue-per-order`. If not specified, we choose default based on model type. Default depends on type of recommendation: `recommended-for-you` =&gt; `ctr` `others-you-may-like` =&gt; `ctr` `frequently-bought-together` =&gt; `revenue_per_order` This field together with optimization_objective describe model metadata to use to control model training and serving. See https://cloud.google.com/retail/docs/models for more details on what the model metadata control and which combination of parameters are valid. For invalid combinations of parameters (e.g. type = `frequently-bought-together` and optimization_objective = `ctr`), you receive an error 400 if you try to create/update a recommendation with this set of knobs. |
| `trainingState` | `string` | Optional. The training state that the model is in (e.g. `TRAINING` or `PAUSED`). Since part of the cost of running the service is frequency of training - this can be used to determine when to train model in order to control cost. If not specified: the default value for `CreateModel` method is `TRAINING`. The default value for `UpdateModel` method is to keep the state the same as before. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_models_get` | `SELECT` | `catalogsId, locationsId, modelsId, projectsId` | Gets a model. |
| `projects_locations_catalogs_models_list` | `SELECT` | `catalogsId, locationsId, projectsId` | Lists all the models linked to this event store. |
| `projects_locations_catalogs_models_create` | `INSERT` | `catalogsId, locationsId, projectsId` | Creates a new model. |
| `projects_locations_catalogs_models_delete` | `DELETE` | `catalogsId, locationsId, modelsId, projectsId` | Deletes an existing model. |
| `_projects_locations_catalogs_models_list` | `EXEC` | `catalogsId, locationsId, projectsId` | Lists all the models linked to this event store. |
| `projects_locations_catalogs_models_patch` | `EXEC` | `catalogsId, locationsId, modelsId, projectsId` | Update of model metadata. Only fields that currently can be updated are: `filtering_option` and `periodic_tuning_state`. If other values are provided, this API method ignores them. |
| `projects_locations_catalogs_models_pause` | `EXEC` | `catalogsId, locationsId, modelsId, projectsId` | Pauses the training of an existing model. |
| `projects_locations_catalogs_models_resume` | `EXEC` | `catalogsId, locationsId, modelsId, projectsId` | Resumes the training of an existing model. |
| `projects_locations_catalogs_models_tune` | `EXEC` | `catalogsId, locationsId, modelsId, projectsId` | Tunes an existing model. |
