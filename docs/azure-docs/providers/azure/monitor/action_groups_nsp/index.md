---
title: action_groups_nsp
hide_title: false
hide_table_of_contents: false
keywords:
  - action_groups_nsp
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
<tr><td><b>Name</b></td><td><code>action_groups_nsp</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.action_groups_nsp" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionGroupName, networkSecurityPerimeterConfigurationName, resourceGroupName, subscriptionId" /> | Gets a specified NSP configuration for specified action group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="actionGroupName, resourceGroupName, subscriptionId" /> | Gets a list of NSP configurations for specified action group. |
