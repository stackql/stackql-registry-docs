---
title: transformations
hide_title: false
hide_table_of_contents: false
keywords:
  - transformations
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
<tr><td><b>Name</b></td><td><code>transformations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.stream_analytics.transformations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `type` | `string` | Resource type |
| `properties` | `object` | The properties that are associated with a transformation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Transformations_Get` | `SELECT` | `jobName, resourceGroupName, subscriptionId, transformationName` | Gets details about the specified transformation. |
| `Transformations_CreateOrReplace` | `INSERT` | `jobName, resourceGroupName, subscriptionId, transformationName` | Creates a transformation or replaces an already existing transformation under an existing streaming job. |
| `Transformations_Update` | `EXEC` | `jobName, resourceGroupName, subscriptionId, transformationName` | Updates an existing transformation under an existing streaming job. This can be used to partially update (ie. update one or two properties) a transformation without affecting the rest the job or transformation definition. |
