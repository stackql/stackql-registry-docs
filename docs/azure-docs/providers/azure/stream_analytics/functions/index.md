---
title: functions
hide_title: false
hide_table_of_contents: false
keywords:
  - functions
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
<tr><td><b>Name</b></td><td><code>functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.stream_analytics.functions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `properties` | `object` | The properties that are associated with a function. |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `functionName, jobName, resourceGroupName, subscriptionId` | Gets details about the specified function. |
| `list_by_streaming_job` | `SELECT` | `jobName, resourceGroupName, subscriptionId` | Lists all of the functions under the specified streaming job. |
| `create_or_replace` | `INSERT` | `functionName, jobName, resourceGroupName, subscriptionId` | Creates a function or replaces an already existing function under an existing streaming job. |
| `delete` | `DELETE` | `functionName, jobName, resourceGroupName, subscriptionId` | Deletes a function from the streaming job. |
| `_list_by_streaming_job` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Lists all of the functions under the specified streaming job. |
| `retrieve_default_definition` | `EXEC` | `functionName, jobName, resourceGroupName, subscriptionId, data__bindingType` | Retrieves the default definition of a function based on the parameters specified. |
| `test` | `EXEC` | `functionName, jobName, resourceGroupName, subscriptionId` | Tests if the information provided for a function is valid. This can range from testing the connection to the underlying web service behind the function or making sure the function code provided is syntactically correct. |
| `update` | `EXEC` | `functionName, jobName, resourceGroupName, subscriptionId` | Updates an existing function under an existing streaming job. This can be used to partially update (ie. update one or two properties) a function without affecting the rest the job or function definition. |
