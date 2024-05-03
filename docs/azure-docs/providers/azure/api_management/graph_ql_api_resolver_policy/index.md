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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graph_ql_api_resolver_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.graph_ql_api_resolver_policy" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, policyId, resolverId, resourceGroupName, serviceName, subscriptionId" /> | Get the policy configuration at the GraphQL API Resolver level. |
| <CopyableCode code="list_by_resolver" /> | `SELECT` | <CopyableCode code="apiId, resolverId, resourceGroupName, serviceName, subscriptionId" /> | Get the list of policy configuration at the GraphQL API Resolver level. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, policyId, resolverId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates policy configuration for the GraphQL API Resolver level. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, policyId, resolverId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the policy configuration at the GraphQL Api Resolver. |
| <CopyableCode code="_list_by_resolver" /> | `EXEC` | <CopyableCode code="apiId, resolverId, resourceGroupName, serviceName, subscriptionId" /> | Get the list of policy configuration at the GraphQL API Resolver level. |
