---
title: workspace_api_operation_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_api_operation_policy
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
<tr><td><b>Name</b></td><td><code>workspace_api_operation_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_api_operation_policy" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, operationId, policyId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Get the policy configuration at the API Operation level. |
| <CopyableCode code="list_by_operation" /> | `SELECT` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Get the list of policy configuration at the API Operation level. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, operationId, policyId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates or updates policy configuration for the API Operation level. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, operationId, policyId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes the policy configuration at the Api Operation. |
| <CopyableCode code="_list_by_operation" /> | `EXEC` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Get the list of policy configuration at the API Operation level. |
