---
title: log_analytics_log_analytics_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - log_analytics_log_analytics_metrics
  - cdn
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
<tr><td><b>Name</b></td><td><code>log_analytics_log_analytics_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.log_analytics_log_analytics_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="dateTimeBegin" /> | `string` |
| <CopyableCode code="dateTimeEnd" /> | `string` |
| <CopyableCode code="granularity" /> | `string` |
| <CopyableCode code="series" /> | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customDomains, dateTimeBegin, dateTimeEnd, granularity, metrics, profileName, protocols, resourceGroupName, subscriptionId" /> |
