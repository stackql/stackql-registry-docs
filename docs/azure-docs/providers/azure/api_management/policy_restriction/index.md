---
title: policy_restriction
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_restriction
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
<tr><td><b>Name</b></td><td><code>policy_restriction</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.policy_restriction</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `policyRestrictionId, resourceGroupName, serviceName, subscriptionId` | Get the policy restriction of the Api Management service. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Gets all policy restrictions of API Management services. |
| `create_or_update` | `INSERT` | `policyRestrictionId, resourceGroupName, serviceName, subscriptionId` | Creates or updates the policy restriction configuration of the Api Management service. |
| `delete` | `DELETE` | `policyRestrictionId, resourceGroupName, serviceName, subscriptionId` | Deletes the policy restriction configuration of the Api Management Service. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Gets all policy restrictions of API Management services. |
| `update` | `EXEC` | `If-Match, policyRestrictionId, resourceGroupName, serviceName, subscriptionId` | Updates the policy restriction configuration of the Api Management service. |
