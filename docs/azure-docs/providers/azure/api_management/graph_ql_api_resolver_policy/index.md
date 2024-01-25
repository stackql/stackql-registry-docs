---
title: graph_ql_api_resolver_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - graph_ql_api_resolver_policy
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
<tr><td><b>Name</b></td><td><code>graph_ql_api_resolver_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.graph_ql_api_resolver_policy</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apiId, policyId, resolverId, resourceGroupName, serviceName, subscriptionId` | Get the policy configuration at the GraphQL API Resolver level. |
| `list_by_resolver` | `SELECT` | `apiId, resolverId, resourceGroupName, serviceName, subscriptionId` | Get the list of policy configuration at the GraphQL API Resolver level. |
| `create_or_update` | `INSERT` | `apiId, policyId, resolverId, resourceGroupName, serviceName, subscriptionId` | Creates or updates policy configuration for the GraphQL API Resolver level. |
| `delete` | `DELETE` | `If-Match, apiId, policyId, resolverId, resourceGroupName, serviceName, subscriptionId` | Deletes the policy configuration at the GraphQL Api Resolver. |
| `_list_by_resolver` | `EXEC` | `apiId, resolverId, resourceGroupName, serviceName, subscriptionId` | Get the list of policy configuration at the GraphQL API Resolver level. |
