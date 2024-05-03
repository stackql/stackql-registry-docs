---
title: activity
hide_title: false
hide_table_of_contents: false
keywords:
  - activity
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
<tr><td><b>Name</b></td><td><code>activity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.activity" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets the name of the activity. |
| <CopyableCode code="properties" /> | `object` | Properties of the activity. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="activityName, automationAccountName, moduleName, resourceGroupName, subscriptionId" /> | Retrieve the activity in the module identified by module name and activity name. |
| <CopyableCode code="list_by_module" /> | `SELECT` | <CopyableCode code="automationAccountName, moduleName, resourceGroupName, subscriptionId" /> | Retrieve a list of activities in the module identified by module name. |
| <CopyableCode code="_list_by_module" /> | `EXEC` | <CopyableCode code="automationAccountName, moduleName, resourceGroupName, subscriptionId" /> | Retrieve a list of activities in the module identified by module name. |
