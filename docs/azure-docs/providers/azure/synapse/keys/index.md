---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - synapse
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.keys" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a workspace key |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Returns a list of keys in a workspace |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="keyName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a workspace key |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keyName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a workspace key |
| <CopyableCode code="_list_by_workspace" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Returns a list of keys in a workspace |
