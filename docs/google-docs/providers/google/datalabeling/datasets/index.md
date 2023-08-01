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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalabeling.datasets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `datasets` | `array` | The list of datasets to return. |
| `nextPageToken` | `string` | A token to retrieve next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_datasets_get` | `SELECT` | `datasetsId, projectsId` | Gets dataset by resource name. |
| `projects_datasets_list` | `SELECT` | `projectsId` | Lists datasets under a project. Pagination is supported. |
| `projects_datasets_create` | `INSERT` | `projectsId` | Creates dataset. If success return a Dataset resource. |
| `projects_datasets_delete` | `DELETE` | `datasetsId, projectsId` | Deletes a dataset by resource name. |
| `projects_datasets_export_data` | `EXEC` | `datasetsId, projectsId` | Exports data and annotations from dataset. |
| `projects_datasets_import_data` | `EXEC` | `datasetsId, projectsId` | Imports data into dataset based on source locations defined in request. It can be called multiple times for the same dataset. Each dataset can only have one long running operation running on it. For example, no labeling task (also long running operation) can be started while importing is still ongoing. Vice versa. |
