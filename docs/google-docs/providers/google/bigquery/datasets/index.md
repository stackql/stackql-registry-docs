---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
  - bigquery
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
<tr><td><b>Id</b></td><td><code>google.bigquery.datasets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The fully-qualified, unique, opaque ID of the dataset. |
| `kind` | `string` | The resource type. This property always returns the value "bigquery#dataset". |
| `labels` | `object` | The labels associated with this dataset. You can use these to organize and group your datasets. |
| `location` | `string` | The geographic location where the data resides. |
| `datasetReference` | `object` |  |
| `friendlyName` | `string` | A descriptive name for the dataset, if one exists. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `datasetId, projectId` | Returns the dataset specified by datasetID. |
| `list` | `SELECT` | `projectId` | Lists all datasets in the specified project to which you have been granted the READER dataset role. |
| `insert` | `INSERT` | `projectId` | Creates a new empty dataset. |
| `delete` | `DELETE` | `datasetId, projectId` | Deletes the dataset specified by the datasetId value. Before you can delete a dataset, you must delete all its tables, either manually or by specifying deleteContents. Immediately after deletion, you can create another dataset with the same name. |
| `_list` | `EXEC` | `projectId` | Lists all datasets in the specified project to which you have been granted the READER dataset role. |
| `patch` | `EXEC` | `datasetId, projectId` | Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource. This method supports patch semantics. |
| `update` | `EXEC` | `datasetId, projectId` | Updates information in an existing dataset. The update method replaces the entire dataset resource, whereas the patch method only replaces fields that are provided in the submitted dataset resource. |
