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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalabeling.datasets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Dataset resource name, format is: projects/&#123;project_id&#125;/datasets/&#123;dataset_id&#125; |
| <CopyableCode code="description" /> | `string` | Optional. User-provided description of the annotation specification set. The description can be up to 10000 characters long. |
| <CopyableCode code="blockingResources" /> | `array` | Output only. The names of any related resources that are blocking changes to the dataset. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time the dataset is created. |
| <CopyableCode code="dataItemCount" /> | `string` | Output only. The number of data items in the dataset. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the dataset. Maximum of 64 characters. |
| <CopyableCode code="inputConfigs" /> | `array` | Output only. This is populated with the original input configs where ImportData is called. It is available only after the clients import data to this dataset. |
| <CopyableCode code="lastMigrateTime" /> | `string` | Last time that the Dataset is migrated to AI Platform V2. If any of the AnnotatedDataset is migrated, the last_migration_time in Dataset is also updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_datasets_get" /> | `SELECT` | <CopyableCode code="datasetsId, projectsId" /> | Gets dataset by resource name. |
| <CopyableCode code="projects_datasets_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists datasets under a project. Pagination is supported. |
| <CopyableCode code="projects_datasets_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates dataset. If success return a Dataset resource. |
| <CopyableCode code="projects_datasets_delete" /> | `DELETE` | <CopyableCode code="datasetsId, projectsId" /> | Deletes a dataset by resource name. |
| <CopyableCode code="_projects_datasets_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists datasets under a project. Pagination is supported. |
| <CopyableCode code="projects_datasets_export_data" /> | `EXEC` | <CopyableCode code="datasetsId, projectsId" /> | Exports data and annotations from dataset. |
| <CopyableCode code="projects_datasets_import_data" /> | `EXEC` | <CopyableCode code="datasetsId, projectsId" /> | Imports data into dataset based on source locations defined in request. It can be called multiple times for the same dataset. Each dataset can only have one long running operation running on it. For example, no labeling task (also long running operation) can be started while importing is still ongoing. Vice versa. |
