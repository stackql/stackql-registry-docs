---
title: metric_alerts_status
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_alerts_status
  - monitor
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
<tr><td><b>Name</b></td><td><code>metric_alerts_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.metric_alerts_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The alert rule arm id. |
| <CopyableCode code="name" /> | `string` | The status name. |
| <CopyableCode code="properties" /> | `object` | An alert status properties. |
| <CopyableCode code="type" /> | `string` | The extended resource type name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId" /> |
| <CopyableCode code="list_by_name" /> | `SELECT` | <CopyableCode code="resourceGroupName, ruleName, statusName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId" /> |
| <CopyableCode code="_list_by_name" /> | `EXEC` | <CopyableCode code="resourceGroupName, ruleName, statusName, subscriptionId" /> |
