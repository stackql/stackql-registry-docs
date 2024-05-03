---
title: dsc_node_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - dsc_node_configuration
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
<tr><td><b>Name</b></td><td><code>dsc_node_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.dsc_node_configuration" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, nodeConfigurationName, resourceGroupName, subscriptionId" /> | Retrieve the Dsc node configurations by node configuration. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of dsc node configurations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, nodeConfigurationName, resourceGroupName, subscriptionId" /> | Create the node configuration identified by node configuration name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, nodeConfigurationName, resourceGroupName, subscriptionId" /> | Delete the Dsc node configurations by node configuration. |
| <CopyableCode code="_list_by_automation_account" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of dsc node configurations. |
