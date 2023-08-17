---
title: slices
hide_title: false
hide_table_of_contents: false
keywords:
  - slices
  - aiplatform
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
<tr><td><b>Name</b></td><td><code>slices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.slices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the ModelEvaluationSlice. |
| `slice` | `object` | Definition of a slice. |
| `createTime` | `string` | Output only. Timestamp when this ModelEvaluationSlice was created. |
| `metrics` | `any` | Output only. Sliced evaluation metrics of the Model. The schema of the metrics is stored in metrics_schema_uri |
| `metricsSchemaUri` | `string` | Output only. Points to a YAML file stored on Google Cloud Storage describing the metrics of this ModelEvaluationSlice. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). |
| `modelExplanation` | `object` | Aggregated explanation metrics for a Model over a set of instances. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `evaluationsId, locationsId, modelsId, projectsId, slicesId` | Gets a ModelEvaluationSlice. |
| `list` | `SELECT` | `evaluationsId, locationsId, modelsId, projectsId` | Lists ModelEvaluationSlices in a ModelEvaluation. |
| `_list` | `EXEC` | `evaluationsId, locationsId, modelsId, projectsId` | Lists ModelEvaluationSlices in a ModelEvaluation. |
| `batch_import` | `EXEC` | `evaluationsId, locationsId, modelsId, projectsId, slicesId` | Imports a list of externally generated EvaluatedAnnotations. |
