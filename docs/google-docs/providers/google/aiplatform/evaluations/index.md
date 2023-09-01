---
title: evaluations
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluations
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
<tr><td><b>Name</b></td><td><code>evaluations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.evaluations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the ModelEvaluation. |
| `metricsSchemaUri` | `string` | Points to a YAML file stored on Google Cloud Storage describing the metrics of this ModelEvaluation. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). |
| `dataItemSchemaUri` | `string` | Points to a YAML file stored on Google Cloud Storage describing EvaluatedDataItemView.data_item_payload and EvaluatedAnnotation.data_item_payload. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). This field is not populated if there are neither EvaluatedDataItemViews nor EvaluatedAnnotations under this ModelEvaluation. |
| `explanationSpecs` | `array` | Describes the values of ExplanationSpec that are used for explaining the predicted values on the evaluated data. |
| `displayName` | `string` | The display name of the ModelEvaluation. |
| `modelExplanation` | `object` | Aggregated explanation metrics for a Model over a set of instances. |
| `metadata` | `any` | The metadata of the ModelEvaluation. For the ModelEvaluation uploaded from Managed Pipeline, metadata contains a structured value with keys of "pipeline_job_id", "evaluation_dataset_type", "evaluation_dataset_path". |
| `annotationSchemaUri` | `string` | Points to a YAML file stored on Google Cloud Storage describing EvaluatedDataItemView.predictions, EvaluatedDataItemView.ground_truths, EvaluatedAnnotation.predictions, and EvaluatedAnnotation.ground_truths. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). This field is not populated if there are neither EvaluatedDataItemViews nor EvaluatedAnnotations under this ModelEvaluation. |
| `sliceDimensions` | `array` | All possible dimensions of ModelEvaluationSlices. The dimensions can be used as the filter of the ModelService.ListModelEvaluationSlices request, in the form of `slice.dimension = `. |
| `metrics` | `any` | Evaluation metrics of the Model. The schema of the metrics is stored in metrics_schema_uri |
| `createTime` | `string` | Output only. Timestamp when this ModelEvaluation was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `evaluationsId, locationsId, modelsId, projectsId` | Gets a ModelEvaluation. |
| `list` | `SELECT` | `locationsId, modelsId, projectsId` | Lists ModelEvaluations in a Model. |
| `_list` | `EXEC` | `locationsId, modelsId, projectsId` | Lists ModelEvaluations in a Model. |
| `import` | `EXEC` | `locationsId, modelsId, projectsId` | Imports an externally generated ModelEvaluation. |
