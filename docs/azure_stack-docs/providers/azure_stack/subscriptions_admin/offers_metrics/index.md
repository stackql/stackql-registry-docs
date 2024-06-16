---
title: offers_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - offers_metrics
  - subscriptions_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>offers_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.offers_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endTime" /> | `string` | End time of the metric. |
| <CopyableCode code="metricUnit" /> | `string` | The resource metric unit. |
| <CopyableCode code="metricValues" /> | `array` | List of metric values. |
| <CopyableCode code="startTime" /> | `string` | Start time of the metric. |
| <CopyableCode code="timeGrain" /> | `string` | Timespan of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="offer, resourceGroupName, subscriptionId" /> |
