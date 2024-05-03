---
title: workspace_group_user
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_group_user
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
<tr><td><b>Name</b></td><td><code>workspace_group_user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_group_user" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of user entities associated with the group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="groupId, resourceGroupName, serviceName, subscriptionId, userId, workspaceId" /> | Add existing user to existing group |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupId, resourceGroupName, serviceName, subscriptionId, userId, workspaceId" /> | Remove existing user from existing group. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="groupId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of user entities associated with the group. |
| <CopyableCode code="check_entity_exists" /> | `EXEC` | <CopyableCode code="groupId, resourceGroupName, serviceName, subscriptionId, userId, workspaceId" /> | Checks that user entity specified by identifier is associated with the group entity. |
