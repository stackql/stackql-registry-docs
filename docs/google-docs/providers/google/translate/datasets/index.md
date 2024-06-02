---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
  - translate
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
<tr><td><b>Id</b></td><td><CopyableCode code="translate.datasets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the dataset, in form of `projects/&#123;project-number-or-id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this dataset was created. |
| <CopyableCode code="displayName" /> | `string` | The name of the dataset to show in the interface. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores (_), and ASCII digits 0-9. |
| <CopyableCode code="exampleCount" /> | `integer` | Output only. The number of examples in the dataset. |
| <CopyableCode code="sourceLanguageCode" /> | `string` | The BCP-47 language code of the source language. |
| <CopyableCode code="targetLanguageCode" /> | `string` | The BCP-47 language code of the target language. |
| <CopyableCode code="testExampleCount" /> | `integer` | Output only. Number of test examples (sentence pairs). |
| <CopyableCode code="trainExampleCount" /> | `integer` | Output only. Number of training examples (sentence pairs). |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this dataset was last updated. |
| <CopyableCode code="validateExampleCount" /> | `integer` | Output only. Number of validation examples (sentence pairs). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_datasets_get" /> | `SELECT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Gets a Dataset. |
| <CopyableCode code="projects_locations_datasets_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists datasets. |
| <CopyableCode code="projects_locations_datasets_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Dataset. |
| <CopyableCode code="projects_locations_datasets_delete" /> | `DELETE` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Deletes a dataset and all of its contents. |
| <CopyableCode code="_projects_locations_datasets_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists datasets. |
| <CopyableCode code="projects_locations_datasets_export_data" /> | `EXEC` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Exports dataset's data to the provided output location. |
| <CopyableCode code="projects_locations_datasets_import_data" /> | `EXEC` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Import sentence pairs into translation Dataset. |
