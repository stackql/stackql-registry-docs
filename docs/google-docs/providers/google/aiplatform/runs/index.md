---
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - runs
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
<tr><td><b>Name</b></td><td><code>runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the TensorboardRun. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/tensorboards/&#123;tensorboard&#125;/experiments/&#123;experiment&#125;/runs/&#123;run&#125;` |
| `description` | `string` | Description of this TensorboardRun. |
| `displayName` | `string` | Required. User provided name of this TensorboardRun. This value must be unique among all TensorboardRuns belonging to the same parent TensorboardExperiment. |
| `etag` | `string` | Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `labels` | `object` | The labels with user-defined metadata to organize your TensorboardRuns. This field will be used to filter and visualize Runs in the Tensorboard UI. For example, a Vertex AI training job can set a label aiplatform.googleapis.com/training_job_id=xxxxx to all the runs created within that job. An end user can set a label experiment_id=xxxxx for all the runs produced in a Jupyter notebook. These runs can be grouped by a label value and visualized together in the Tensorboard UI. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one TensorboardRun (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| `updateTime` | `string` | Output only. Timestamp when this TensorboardRun was last updated. |
| `createTime` | `string` | Output only. Timestamp when this TensorboardRun was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId` | Gets a TensorboardRun. |
| `list` | `SELECT` | `experimentsId, locationsId, projectsId, tensorboardsId` | Lists TensorboardRuns in a Location. |
| `create` | `INSERT` | `experimentsId, locationsId, projectsId, tensorboardsId` | Creates a TensorboardRun. |
| `delete` | `DELETE` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId` | Deletes a TensorboardRun. |
| `_list` | `EXEC` | `experimentsId, locationsId, projectsId, tensorboardsId` | Lists TensorboardRuns in a Location. |
| `batch_create` | `EXEC` | `experimentsId, locationsId, projectsId, tensorboardsId` | Batch create TensorboardRuns. |
| `patch` | `EXEC` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId` | Updates a TensorboardRun. |
| `write` | `EXEC` | `experimentsId, locationsId, projectsId, runsId, tensorboardsId` | Write time series data points into multiple TensorboardTimeSeries under a TensorboardRun. If any data fail to be ingested, an error is returned. |
