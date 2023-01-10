---
title: recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - recommendations
  - advisor
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.advisor.recommendations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | The properties of the recommendation. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Recommendations_Get` | `SELECT` | `recommendationId, resourceUri` | Obtains details of a cached recommendation. |
| `Recommendations_List` | `SELECT` | `subscriptionId` | Obtains cached recommendations for a subscription. The recommendations are generated or computed by invoking generateRecommendations. |
| `Recommendations_Generate` | `EXEC` | `subscriptionId` | Initiates the recommendation generation or computation process for a subscription. This operation is asynchronous. The generated recommendations are stored in a cache in the Advisor service. |
| `Recommendations_GetGenerateStatus` | `EXEC` | `operationId, subscriptionId` | Retrieves the status of the recommendation computation or generation process. Invoke this API after calling the generation recommendation. The URI of this API is returned in the Location field of the response header. |
