---
title: watchers_troubleshooting_result
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers_troubleshooting_result
  - network
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
<tr><td><b>Name</b></td><td><code>watchers_troubleshooting_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.watchers_troubleshooting_result" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="code" /> | `string` | The result code of the troubleshooting. |
| <CopyableCode code="endTime" /> | `string` | The end time of the troubleshooting. |
| <CopyableCode code="results" /> | `array` | Information from troubleshooting. |
| <CopyableCode code="startTime" /> | `string` | The start time of the troubleshooting. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId, data__targetResourceId" /> |
