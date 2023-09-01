---
title: annotated_datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - annotated_datasets
  - datalabeling
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
<tr><td><b>Name</b></td><td><code>annotated_datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalabeling.annotated_datasets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. AnnotatedDataset resource name in format of: projects/&#123;project_id&#125;/datasets/&#123;dataset_id&#125;/annotatedDatasets/ &#123;annotated_dataset_id&#125; |
| `description` | `string` | Output only. The description of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 10000 characters. |
| `labelStats` | `object` | Statistics about annotation specs. |
| `blockingResources` | `array` | Output only. The names of any related resources that are blocking changes to the annotated dataset. |
| `completedExampleCount` | `string` | Output only. Number of examples that have annotation in the annotated dataset. |
| `metadata` | `object` | Metadata on AnnotatedDataset. |
| `displayName` | `string` | Output only. The display name of the AnnotatedDataset. It is specified in HumanAnnotationConfig when user starts a labeling task. Maximum of 64 characters. |
| `createTime` | `string` | Output only. Time the AnnotatedDataset was created. |
| `exampleCount` | `string` | Output only. Number of examples in the annotated dataset. |
| `annotationSource` | `string` | Output only. Source of the annotation. |
| `annotationType` | `string` | Output only. Type of the annotation. It is specified when starting labeling task. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_datasets_annotated_datasets_get` | `SELECT` | `annotatedDatasetsId, datasetsId, projectsId` | Gets an annotated dataset by resource name. |
| `projects_datasets_annotated_datasets_list` | `SELECT` | `datasetsId, projectsId` | Lists annotated datasets for a dataset. Pagination is supported. |
| `projects_datasets_annotated_datasets_delete` | `DELETE` | `annotatedDatasetsId, datasetsId, projectsId` | Deletes an annotated dataset by resource name. |
| `_projects_datasets_annotated_datasets_list` | `EXEC` | `datasetsId, projectsId` | Lists annotated datasets for a dataset. Pagination is supported. |
