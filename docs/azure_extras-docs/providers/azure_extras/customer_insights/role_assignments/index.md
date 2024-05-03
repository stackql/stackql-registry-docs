---
title: role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments
  - customer_insights
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>role_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.role_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The Role Assignment definition. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assignmentName, hubName, resourceGroupName, subscriptionId" /> | Gets the role assignment in the hub. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all the role assignments for the specified hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="assignmentName, hubName, resourceGroupName, subscriptionId" /> | Creates or updates a role assignment in the hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assignmentName, hubName, resourceGroupName, subscriptionId" /> | Deletes the role assignment in the hub. |
| <CopyableCode code="_list_by_hub" /> | `EXEC` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all the role assignments for the specified hub. |
