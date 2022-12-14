---
title: inputs
hide_title: false
hide_table_of_contents: false
keywords:
  - inputs
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
<tr><td><b>Name</b></td><td><code>inputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.stream_analytics.inputs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `type` | `string` | Resource type |
| `properties` | `object` | The properties that are associated with an input. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Inputs_Get` | `SELECT` | `inputName, jobName, resourceGroupName, subscriptionId` | Gets details about the specified input. |
| `Inputs_ListByStreamingJob` | `SELECT` | `jobName, resourceGroupName, subscriptionId` | Lists all of the inputs under the specified streaming job. |
| `Inputs_CreateOrReplace` | `INSERT` | `inputName, jobName, resourceGroupName, subscriptionId` | Creates an input or replaces an already existing input under an existing streaming job. |
| `Inputs_Delete` | `DELETE` | `inputName, jobName, resourceGroupName, subscriptionId` | Deletes an input from the streaming job. |
| `Inputs_Test` | `EXEC` | `inputName, jobName, resourceGroupName, subscriptionId` | Tests whether an input’s datasource is reachable and usable by the Azure Stream Analytics service. |
| `Inputs_Update` | `EXEC` | `inputName, jobName, resourceGroupName, subscriptionId` | Updates an existing input under an existing streaming job. This can be used to partially update (ie. update one or two properties) an input without affecting the rest the job or input definition. |
