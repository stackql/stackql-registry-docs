---
title: log_analytics_waf_log_analytics_rankings
hide_title: false
hide_table_of_contents: false
keywords:
  - log_analytics_waf_log_analytics_rankings
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
<tr><td><b>Name</b></td><td><code>log_analytics_waf_log_analytics_rankings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.log_analytics_waf_log_analytics_rankings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="data" /> | `array` |
| <CopyableCode code="dateTimeBegin" /> | `string` |
| <CopyableCode code="dateTimeEnd" /> | `string` |
| <CopyableCode code="groups" /> | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dateTimeBegin, dateTimeEnd, maxRanking, metrics, profileName, rankings, resourceGroupName, subscriptionId" /> |
