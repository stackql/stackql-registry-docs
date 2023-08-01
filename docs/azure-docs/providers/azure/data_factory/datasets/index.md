---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
  - data_factory
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.datasets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `etag` | `string` | Etag identifies change in the resource. |
| `properties` | `object` | The Azure Data Factory nested object which identifies data within different data stores, such as tables, files, folders, and documents. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Datasets_Get` | `SELECT` | `api-version, datasetName, factoryName, resourceGroupName, subscriptionId` | Gets a dataset. |
| `Datasets_ListByFactory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists datasets. |
| `Datasets_CreateOrUpdate` | `INSERT` | `api-version, datasetName, factoryName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a dataset. |
| `Datasets_Delete` | `DELETE` | `api-version, datasetName, factoryName, resourceGroupName, subscriptionId` | Deletes a dataset. |
