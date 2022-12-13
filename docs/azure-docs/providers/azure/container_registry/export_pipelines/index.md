---
title: export_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - export_pipelines
  - container_registry
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
<tr><td><b>Name</b></td><td><code>export_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.export_pipelines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. |
| `identity` | `object` | Managed identity for the resource. |
| `location` | `string` | The location of the export pipeline. |
| `properties` | `object` | The properties of an export pipeline. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExportPipelines_Get` | `SELECT` | `exportPipelineName, registryName, resourceGroupName, subscriptionId` | Gets the properties of the export pipeline. |
| `ExportPipelines_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all export pipelines for the specified container registry. |
| `ExportPipelines_Create` | `INSERT` | `exportPipelineName, registryName, resourceGroupName, subscriptionId` | Creates an export pipeline for a container registry with the specified parameters. |
| `ExportPipelines_Delete` | `DELETE` | `exportPipelineName, registryName, resourceGroupName, subscriptionId` | Deletes an export pipeline from a container registry. |
