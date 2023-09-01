---
title: data_items
hide_title: false
hide_table_of_contents: false
keywords:
  - data_items
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
<tr><td><b>Name</b></td><td><code>data_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalabeling.data_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the data item, in format of: projects/&#123;project_id&#125;/datasets/&#123;dataset_id&#125;/dataItems/&#123;data_item_id&#125; |
| `imagePayload` | `object` | Container of information about an image. |
| `textPayload` | `object` | Container of information about a piece of text. |
| `videoPayload` | `object` | Container of information of a video. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_datasets_annotated_datasets_data_items_get` | `SELECT` | `annotatedDatasetsId, dataItemsId, datasetsId, projectsId` | Gets a data item in a dataset by resource name. This API can be called after data are imported into dataset. |
| `projects_datasets_annotated_datasets_data_items_list` | `SELECT` | `annotatedDatasetsId, datasetsId, projectsId` | Lists data items in a dataset. This API can be called after data are imported into dataset. Pagination is supported. |
| `projects_datasets_data_items_get` | `SELECT` | `dataItemsId, datasetsId, projectsId` | Gets a data item in a dataset by resource name. This API can be called after data are imported into dataset. |
| `projects_datasets_data_items_list` | `SELECT` | `datasetsId, projectsId` | Lists data items in a dataset. This API can be called after data are imported into dataset. Pagination is supported. |
| `_projects_datasets_annotated_datasets_data_items_list` | `EXEC` | `annotatedDatasetsId, datasetsId, projectsId` | Lists data items in a dataset. This API can be called after data are imported into dataset. Pagination is supported. |
| `_projects_datasets_data_items_list` | `EXEC` | `datasetsId, projectsId` | Lists data items in a dataset. This API can be called after data are imported into dataset. Pagination is supported. |
