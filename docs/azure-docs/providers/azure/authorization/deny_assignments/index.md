---
title: deny_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - deny_assignments
  - authorization
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
<tr><td><b>Name</b></td><td><code>deny_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.deny_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The deny assignment ID. |
| <CopyableCode code="name" /> | `string` | The deny assignment name. |
| <CopyableCode code="properties" /> | `object` | Deny assignment properties. |
| <CopyableCode code="type" /> | `string` | The deny assignment type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="denyAssignmentId, scope" /> | Get the specified deny assignment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all deny assignments for the subscription. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets all deny assignments for the subscription. |
| <CopyableCode code="get_by_id" /> | `EXEC` | <CopyableCode code="denyAssignmentId" /> | Gets a deny assignment by ID. |
