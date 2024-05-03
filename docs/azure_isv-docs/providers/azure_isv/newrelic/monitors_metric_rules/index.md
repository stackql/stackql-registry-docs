---
title: monitors_metric_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_metric_rules
  - newrelic
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>monitors_metric_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.newrelic.monitors_metric_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="filteringTags" /> | `array` | List of filtering tags to be used for capturing metrics. |
| <CopyableCode code="sendMetrics" /> | `string` | Indicates whether metrics are being sent. |
| <CopyableCode code="userEmail" /> | `string` | Reusable representation of an email address |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, data__userEmail" /> |
