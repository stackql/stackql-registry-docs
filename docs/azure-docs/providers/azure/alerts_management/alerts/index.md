---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - alerts_management
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.alerts_management.alerts" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="change_state" /> | `EXEC` | <CopyableCode code="alertId, newState, scope" /> | Change the state of an alert. |
| <CopyableCode code="get_by_id" /> | `EXEC` | <CopyableCode code="alertId, scope" /> | Get information related to a specific alert |
| <CopyableCode code="meta_data" /> | `EXEC` | <CopyableCode code="identifier" /> | List alerts meta data information based on value of identifier parameter. |
