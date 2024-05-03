---
title: web_apps_perf_mon_counters_slot
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_perf_mon_counters_slot
  - app_service
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
<tr><td><b>Name</b></td><td><code>web_apps_perf_mon_counters_slot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.web_apps_perf_mon_counters_slot" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="code" /> | `string` | The response code. |
| <CopyableCode code="data" /> | `object` | Metric information. |
| <CopyableCode code="message" /> | `string` | The message. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> |
