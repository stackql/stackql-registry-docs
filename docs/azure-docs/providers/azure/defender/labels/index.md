---
title: labels
hide_title: false
hide_table_of_contents: false
keywords:
  - labels
  - defender
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
<tr><td><b>Name</b></td><td><code>labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.defender.labels" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Returns a list of labels in the given workspace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labelName, resourceGroupName, subscriptionId, workspaceName" /> | Delete a Label. |
| <CopyableCode code="create_and_update" /> | `EXEC` | <CopyableCode code="labelName, resourceGroupName, subscriptionId, workspaceName" /> | Create or update a Label. |
| <CopyableCode code="get_by_workspace" /> | `EXEC` | <CopyableCode code="labelName, resourceGroupName, subscriptionId, workspaceName" /> | Returns a label in the given workspace. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="labelName, resourceGroupName, subscriptionId, workspaceName" /> | Update a Label. |
