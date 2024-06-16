---
title: workspace_api_operation
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_api_operation
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
<tr><td><b>Name</b></td><td><code>workspace_api_operation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_api_operation" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets the details of the API Operation specified by its identifier. |
| <CopyableCode code="list_by_api" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of the operations for the specified API. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, operationId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates a new operation in the API or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, operationId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes the specified operation in the API. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, apiId, operationId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Updates the details of the operation in the API specified by its identifier. |
