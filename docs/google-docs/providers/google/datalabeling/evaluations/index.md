---
title: evaluations
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluations
  - datalabeling
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
<tr><td><b>Name</b></td><td><code>evaluations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalabeling.evaluations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of an evaluation. The name has the following format: "projects/{project_id}/datasets/{dataset_id}/evaluations/ {evaluation_id}' |
| `evaluationMetrics` | `object` |  |
| `annotationType` | `string` | Output only. Type of task that the model version being evaluated performs, as defined in the evaluationJobConfig.inputConfig.annotationType field of the evaluation job that created this evaluation. |
| `config` | `object` | Configuration details used for calculating evaluation metrics and creating an Evaluation. |
| `createTime` | `string` | Output only. Timestamp for when this evaluation was created. |
| `evaluatedItemCount` | `string` | Output only. The number of items in the ground truth dataset that were used for this evaluation. Only populated when the evaulation is for certain AnnotationTypes. |
| `evaluationJobRunTime` | `string` | Output only. Timestamp for when the evaluation job that created this evaluation ran. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_datasets_evaluations_get` | `SELECT` | `datasetsId, evaluationsId, projectsId` | Gets an evaluation by resource name (to search, use projects.evaluations.search). |
| `projects_evaluations_search` | `EXEC` | `projectsId` | Searches evaluations within a project. |
