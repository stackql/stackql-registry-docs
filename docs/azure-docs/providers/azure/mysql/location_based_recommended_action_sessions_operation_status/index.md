---
title: location_based_recommended_action_sessions_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - location_based_recommended_action_sessions_operation_status
  - mysql
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
<tr><td><b>Name</b></td><td><code>location_based_recommended_action_sessions_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.location_based_recommended_action_sessions_operation_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Operation identifier. |
| `startTime` | `string` | Operation start time. |
| `status` | `string` | Operation status. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `LocationBasedRecommendedActionSessionsOperationStatus_Get` | `SELECT` | `locationName, operationId, subscriptionId` |
