---
title: sub_account_monitored_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - sub_account_monitored_resources
  - logz
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
<tr><td><b>Name</b></td><td><code>sub_account_monitored_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.logz.sub_account_monitored_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ARM id of the resource. |
| <CopyableCode code="reasonForLogsStatus" /> | `string` | Reason for why the resource is sending logs (or why it is not sending). |
| <CopyableCode code="reasonForMetricsStatus" /> | `string` | Reason for why the resource is sending metrics (or why it is not sending). |
| <CopyableCode code="sendingLogs" /> | `boolean` | Flag indicating if resource is sending logs to Logz. |
| <CopyableCode code="sendingMetrics" /> | `boolean` | Flag indicating if resource is sending metrics to Logz. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subAccountName, subscriptionId" /> |
