---
title: import_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - import_pipelines
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
<tr><td><b>Name</b></td><td><code>import_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.import_pipelines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed identity for the resource. |
| `location` | `string` | The location of the import pipeline. |
| `properties` | `object` | The properties of an import pipeline. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `importPipelineName, registryName, resourceGroupName, subscriptionId` | Gets the properties of the import pipeline. |
| `list` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all import pipelines for the specified container registry. |
| `create` | `INSERT` | `importPipelineName, registryName, resourceGroupName, subscriptionId` | Creates an import pipeline for a container registry with the specified parameters. |
| `delete` | `DELETE` | `importPipelineName, registryName, resourceGroupName, subscriptionId` | Deletes an import pipeline from a container registry. |
| `_list` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Lists all import pipelines for the specified container registry. |
