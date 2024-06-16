---
title: diagnostic_settings_diagnostic_proactive_log_collection_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic_settings_diagnostic_proactive_log_collection_settings
  - data_box_edge
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
<tr><td><b>Name</b></td><td><code>diagnostic_settings_diagnostic_proactive_log_collection_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.diagnostic_settings_diagnostic_proactive_log_collection_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The object name. |
| <CopyableCode code="properties" /> | `object` | The properties of proactive log collection settings. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Gets the proactive log collection settings of the specified Data Box Edge/Data Box Gateway device. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId, data__properties" /> | Updates the proactive log collection settings on a Data Box Edge/Data Box Gateway device. |
