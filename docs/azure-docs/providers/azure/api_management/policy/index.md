---
title: policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policy
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
<tr><td><b>Name</b></td><td><code>policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.policy</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `policyId, resourceGroupName, serviceName, subscriptionId` | Get the Global policy definition of the Api Management service. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists all the Global Policy definitions of the Api Management service. |
| `create_or_update` | `INSERT` | `policyId, resourceGroupName, serviceName, subscriptionId` | Creates or updates the global policy configuration of the Api Management service. |
| `delete` | `DELETE` | `If-Match, policyId, resourceGroupName, serviceName, subscriptionId` | Deletes the global policy configuration of the Api Management Service. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists all the Global Policy definitions of the Api Management service. |
