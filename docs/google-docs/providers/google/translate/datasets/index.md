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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.translate.datasets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the dataset, in form of `projects/&#123;project-number-or-id&#125;/locations/&#123;location_id&#125;/datasets/&#123;dataset_id&#125;` |
| `testExampleCount` | `integer` | Output only. Number of test examples (sentence pairs). |
| `trainExampleCount` | `integer` | Output only. Number of training examples (sentence pairs). |
| `createTime` | `string` | Output only. Timestamp when this dataset was created. |
| `exampleCount` | `integer` | Output only. The number of examples in the dataset. |
| `targetLanguageCode` | `string` | The BCP-47 language code of the target language. |
| `displayName` | `string` | The name of the dataset to show in the interface. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores (_), and ASCII digits 0-9. |
| `sourceLanguageCode` | `string` | The BCP-47 language code of the source language. |
| `updateTime` | `string` | Output only. Timestamp when this dataset was last updated. |
| `validateExampleCount` | `integer` | Output only. Number of validation examples (sentence pairs). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_datasets_get` | `SELECT` | `datasetsId, locationsId, projectsId` | Gets a Dataset. |
| `projects_locations_datasets_list` | `SELECT` | `locationsId, projectsId` | Lists datasets. |
| `projects_locations_datasets_create` | `INSERT` | `locationsId, projectsId` | Creates a Dataset. |
| `projects_locations_datasets_delete` | `DELETE` | `datasetsId, locationsId, projectsId` | Deletes a dataset and all of its contents. |
| `_projects_locations_datasets_list` | `EXEC` | `locationsId, projectsId` | Lists datasets. |
| `projects_locations_datasets_export_data` | `EXEC` | `datasetsId, locationsId, projectsId` | Exports dataset's data to the provided output location. |
| `projects_locations_datasets_import_data` | `EXEC` | `datasetsId, locationsId, projectsId` | Import sentence pairs into translation Dataset. |
