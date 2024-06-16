---
title: monitors_monitored_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_monitored_resources
  - dynatrace
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
<tr><td><b>Name</b></td><td><code>monitors_monitored_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.dynatrace.monitors_monitored_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ARM id of the resource. |
| <CopyableCode code="reasonForLogsStatus" /> | `string` | Reason for why the resource is sending logs (or why it is not sending). |
| <CopyableCode code="reasonForMetricsStatus" /> | `string` | Reason for why the resource is sending metrics (or why it is not sending). |
| <CopyableCode code="sendingLogs" /> | `string` | Indicates whether logs are being sent. |
| <CopyableCode code="sendingMetrics" /> | `string` | Indicates whether metrics are being sent. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |
