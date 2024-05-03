---
title: dsc_node
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_node
  - automation
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
<tr><td><b>Name</b></td><td><code>dsc_node</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.dsc_node" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, nodeId, resourceGroupName, subscriptionId" /> | Retrieve the dsc node identified by node id. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of dsc nodes. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, nodeId, resourceGroupName, subscriptionId" /> | Delete the dsc node identified by node id. |
| <CopyableCode code="_list_by_automation_account" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of dsc nodes. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="automationAccountName, nodeId, resourceGroupName, subscriptionId" /> | Update the dsc node. |
