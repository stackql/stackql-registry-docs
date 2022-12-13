---
title: outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - outputs
  - stream_analytics
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
<tr><td><b>Name</b></td><td><code>outputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.stream_analytics.outputs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `properties` | `object` | The properties that are associated with an output. |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Outputs_Get` | `SELECT` | `jobName, outputName, resourceGroupName, subscriptionId` | Gets details about the specified output. |
| `Outputs_ListByStreamingJob` | `SELECT` | `jobName, resourceGroupName, subscriptionId` | Lists all of the outputs under the specified streaming job. |
| `Outputs_CreateOrReplace` | `INSERT` | `jobName, outputName, resourceGroupName, subscriptionId` | Creates an output or replaces an already existing output under an existing streaming job. |
| `Outputs_Delete` | `DELETE` | `jobName, outputName, resourceGroupName, subscriptionId` | Deletes an output from the streaming job. |
| `Outputs_Test` | `EXEC` | `jobName, outputName, resourceGroupName, subscriptionId` | Tests whether an output’s datasource is reachable and usable by the Azure Stream Analytics service. |
| `Outputs_Update` | `EXEC` | `jobName, outputName, resourceGroupName, subscriptionId` | Updates an existing output under an existing streaming job. This can be used to partially update (ie. update one or two properties) an output without affecting the rest the job or output definition. |
