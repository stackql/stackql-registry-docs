---
title: action_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - action_requests
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
<tr><td><b>Name</b></td><td><code>action_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.action_requests" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionRequestName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Get the action request under the specified test base account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | List all action requests under the specified test base account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="actionRequestName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Delete (revoke) an action request. Only requests in review can be deleted. |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="actionRequestName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Create (submit) an action request. |
