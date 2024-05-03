---
title: workspace_api_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_api_policy
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
<tr><td><b>Name</b></td><td><code>workspace_api_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_api_policy" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, policyId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Get the policy configuration at the API level. |
| <CopyableCode code="list_by_api" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Get the policy configuration at the API level. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, policyId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates or updates policy configuration for the API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, policyId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes the policy configuration at the Api. |
| <CopyableCode code="_list_by_api" /> | `EXEC` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Get the policy configuration at the API level. |
