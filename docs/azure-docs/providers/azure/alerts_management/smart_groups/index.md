---
title: smart_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - smart_groups
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
<tr><td><b>Name</b></td><td><code>smart_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.alerts_management.smart_groups" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="change_state" /> | `EXEC` | <CopyableCode code="api-version, newState, smartGroupId, subscriptionId" /> | Change the state of a Smart Group. |
| <CopyableCode code="get_by_id" /> | `EXEC` | <CopyableCode code="api-version, smartGroupId, subscriptionId" /> | Get information related to a specific Smart Group. |
