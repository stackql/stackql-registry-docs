---
title: graph_ql_api_resolver
hide_title: false
hide_table_of_contents: false
keywords:
  - graph_ql_api_resolver
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
<tr><td><b>Name</b></td><td><code>graph_ql_api_resolver</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.graph_ql_api_resolver</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apiId, resolverId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the GraphQL API Resolver specified by its identifier. |
| `list_by_api` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the resolvers for the specified GraphQL API. |
| `create_or_update` | `INSERT` | `apiId, resolverId, resourceGroupName, serviceName, subscriptionId` | Creates a new resolver in the GraphQL API or updates an existing one. |
| `delete` | `DELETE` | `If-Match, apiId, resolverId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified resolver in the GraphQL API. |
| `_list_by_api` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the resolvers for the specified GraphQL API. |
| `update` | `EXEC` | `If-Match, apiId, resolverId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the resolver in the GraphQL API specified by its identifier. |
