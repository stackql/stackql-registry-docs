---
title: billing_hub_service_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_hub_service_usage
  - test_base
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
<tr><td><b>Name</b></td><td><code>billing_hub_service_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.billing_hub_service_usage" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="nextRequest" /> | `object` |
| <CopyableCode code="packageUsageEntries" /> | `array` |
| <CopyableCode code="totalCharges" /> | `number` |
| <CopyableCode code="totalUsedBillableHours" /> | `number` |
| <CopyableCode code="totalUsedFreeHours" /> | `number` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName, data__endTimeStamp, data__startTimeStamp" /> |
