---
title: web_apps_network_traces_slot_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_network_traces_slot_v2
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
<tr><td><b>Name</b></td><td><code>web_apps_network_traces_slot_v2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.web_apps_network_traces_slot_v2" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="message" /> | `string` | Detailed message of a network trace operation, e.g. error message in case of failure. |
| <CopyableCode code="path" /> | `string` | Local file path for the captured network trace file. |
| <CopyableCode code="status" /> | `string` | Current status of the network trace operation, same as Operation.Status (InProgress/Succeeded/Failed). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, operationId, resourceGroupName, slot, subscriptionId" /> |
