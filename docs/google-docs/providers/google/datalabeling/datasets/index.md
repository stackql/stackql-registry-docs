---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
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
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalabeling.datasets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Dataset resource name, format is: projects/{project_id}/datasets/{dataset_id} |
| `description` | `string` | Optional. User-provided description of the annotation specification set. The description can be up to 10000 characters long. |
| `dataItemCount` | `string` | Output only. The number of data items in the dataset. |
| `displayName` | `string` | Required. The display name of the dataset. Maximum of 64 characters. |
| `inputConfigs` | `array` | Output only. This is populated with the original input configs where ImportData is called. It is available only after the clients import data to this dataset. |
| `lastMigrateTime` | `string` | Last time that the Dataset is migrated to AI Platform V2. If any of the AnnotatedDataset is migrated, the last_migration_time in Dataset is also updated. |
| `blockingResources` | `array` | Output only. The names of any related resources that are blocking changes to the dataset. |
| `createTime` | `string` | Output only. Time the dataset is created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_datasets_get` | `SELECT` | `datasetsId, projectsId` | Gets dataset by resource name. |
| `projects_datasets_list` | `SELECT` | `projectsId` | Lists datasets under a project. Pagination is supported. |
| `projects_datasets_create` | `INSERT` | `projectsId` | Creates dataset. If success return a Dataset resource. |
| `projects_datasets_delete` | `DELETE` | `datasetsId, projectsId` | Deletes a dataset by resource name. |
| `projects_datasets_exportData` | `EXEC` | `datasetsId, projectsId` | Exports data and annotations from dataset. |
| `projects_datasets_importData` | `EXEC` | `datasetsId, projectsId` | Imports data into dataset based on source locations defined in request. It can be called multiple times for the same dataset. Each dataset can only have one long running operation running on it. For example, no labeling task (also long running operation) can be started while importing is still ongoing. Vice versa. |
