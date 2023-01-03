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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Required. The name specified for the model when it was created. The model name must be unique within the project it is created in. |
| `description` | `string` | Optional. The description specified for the model when it was created. |
| `labels` | `object` | Optional. One or more labels that you can add, to organize your models. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels. Note that this field is not updatable for mls1* models. |
| `onlinePredictionConsoleLogging` | `boolean` | Optional. If true, online prediction nodes send `stderr` and `stdout` streams to Cloud Logging. These can be more verbose than the standard access logs (see `onlinePredictionLogging`) and can incur higher cost. However, they are helpful for debugging. Note that [logs may incur a cost](/stackdriver/pricing), especially if your project receives prediction requests at a high QPS. Estimate your costs before enabling this option. Default is false. |
| `onlinePredictionLogging` | `boolean` | Optional. If true, online prediction access logs are sent to Cloud Logging. These logs are like standard server access logs, containing information like timestamp and latency for each request. Note that [logs may incur a cost](/stackdriver/pricing), especially if your project receives prediction requests at a high queries per second rate (QPS). Estimate your costs before enabling this option. Default is false. |
| `regions` | `array` | Optional. The list of regions where the model is going to be deployed. Only one region per model is supported. Defaults to 'us-central1' if nothing is set. See the available regions for AI Platform services. Note: * No matter where a model is deployed, it can always be accessed by users from anywhere, both for online and batch prediction. * The region for a batch prediction job is set by the region field when submitting the batch prediction job and does not take its value from this field. |
| `defaultVersion` | `object` | Represents a version of the model. Each version is a trained model deployed in the cloud, ready to handle prediction requests. A model can have multiple versions. You can get information about all of the versions of a given model by calling projects.models.versions.list. |
| `etag` | `string` | `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a model from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform model updates in order to avoid race conditions: An `etag` is returned in the response to `GetModel`, and systems are expected to put that etag in the request to `UpdateModel` to ensure that their change will be applied to the model as intended. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_models_get` | `SELECT` | `modelsId, projectsId` | Gets information about a model, including its name, the description (if set), and the default version (if at least one version of the model has been deployed). |
| `projects_models_list` | `SELECT` | `projectsId` | Lists the models in a project. Each project can contain multiple models, and each model can have multiple versions. If there are no models that match the request parameters, the list request returns an empty response body: {}. |
| `projects_models_create` | `INSERT` | `projectsId` | Creates a model which will later contain one or more versions. You must add at least one version before you can request predictions from the model. Add versions by calling projects.models.versions.create. |
| `projects_models_delete` | `DELETE` | `modelsId, projectsId` | Deletes a model. You can only delete a model if there are no versions in it. You can delete versions by calling projects.models.versions.delete. |
| `projects_models_patch` | `EXEC` | `modelsId, projectsId` | Updates a specific model resource. Currently the only supported fields to update are `description` and `default_version.name`. |
