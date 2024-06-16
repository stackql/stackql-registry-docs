---
title: customer_events
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_events
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
<tr><td><b>Name</b></td><td><code>customer_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.customer_events" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customerEventName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a Test Base CustomerEvent. |
| <CopyableCode code="list_by_test_base_account" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all notification events subscribed under a Test Base Account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="customerEventName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Create or replace a Test Base Customer Event. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customerEventName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Deletes a Test Base Customer Event. |
