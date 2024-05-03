---
title: workspace_group
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_group
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
<tr><td><b>Name</b></td><td><code>workspace_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_group" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets the details of the group specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of groups defined within a workspace in a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates or Updates a group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, groupId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes specific group of the workspace in an API Management service instance. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of groups defined within a workspace in a service instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, groupId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Updates the details of the group specified by its identifier. |
