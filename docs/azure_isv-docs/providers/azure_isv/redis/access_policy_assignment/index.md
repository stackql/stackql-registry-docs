---
title: access_policy_assignment
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policy_assignment
  - redis
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
<tr><td><b>Name</b></td><td><code>access_policy_assignment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis.access_policy_assignment" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessPolicyAssignmentName, cacheName, resourceGroupName, subscriptionId" /> | Gets the list of assignments for an access policy of a redis cache |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Gets the list of access policy assignments associated with this redis cache |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessPolicyAssignmentName, cacheName, resourceGroupName, subscriptionId" /> | Deletes the access policy assignment from a redis cache |
| <CopyableCode code="create_update" /> | `EXEC` | <CopyableCode code="accessPolicyAssignmentName, cacheName, resourceGroupName, subscriptionId" /> | Adds the access policy assignment to the specified users |
