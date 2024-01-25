---
title: api_operation_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - api_operation_policy
  - api_management
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
<tr><td><b>Name</b></td><td><code>api_operation_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_operation_policy</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apiId, operationId, policyId, resourceGroupName, serviceName, subscriptionId` | Get the policy configuration at the API Operation level. |
| `list_by_operation` | `SELECT` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Get the list of policy configuration at the API Operation level. |
| `create_or_update` | `INSERT` | `apiId, operationId, policyId, resourceGroupName, serviceName, subscriptionId` | Creates or updates policy configuration for the API Operation level. |
| `delete` | `DELETE` | `If-Match, apiId, operationId, policyId, resourceGroupName, serviceName, subscriptionId` | Deletes the policy configuration at the Api Operation. |
| `_list_by_operation` | `EXEC` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Get the list of policy configuration at the API Operation level. |
