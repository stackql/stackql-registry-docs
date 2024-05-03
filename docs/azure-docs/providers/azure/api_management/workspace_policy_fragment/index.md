---
title: workspace_policy_fragment
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_policy_fragment
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
<tr><td><b>Name</b></td><td><code>workspace_policy_fragment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_policy_fragment" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets a policy fragment. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets all policy fragments defined within a workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="id, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates or updates a policy fragment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, id, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes a policy fragment. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets all policy fragments defined within a workspace. |
