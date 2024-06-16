---
title: statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - statistics
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
<tr><td><b>Name</b></td><td><code>statistics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.statistics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the id. |
| <CopyableCode code="counterProperty" /> | `string` | Gets the property value of the statistic. |
| <CopyableCode code="counterValue" /> | `integer` | Gets the value of the statistic. |
| <CopyableCode code="endTime" /> | `string` | Gets the endTime of the statistic. |
| <CopyableCode code="startTime" /> | `string` | Gets the startTime of the statistic. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> |
