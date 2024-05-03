---
title: free_hour_balances
hide_title: false
hide_table_of_contents: false
keywords:
  - free_hour_balances
  - test_base
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>free_hour_balances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.free_hour_balances" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="freeHourBalanceName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Return the Test Base free hour balance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Return the Test Base free hour balances list. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Return the Test Base free hour balances list. |
