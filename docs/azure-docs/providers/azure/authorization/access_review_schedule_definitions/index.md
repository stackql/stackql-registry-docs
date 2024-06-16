---
title: access_review_schedule_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_schedule_definitions
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
<tr><td><b>Name</b></td><td><code>access_review_schedule_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_schedule_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review schedule definition id. |
| <CopyableCode code="name" /> | `string` | The access review schedule definition unique id. |
| <CopyableCode code="properties" /> | `object` | Access Review. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get access review schedule definitions |
| <CopyableCode code="delete_by_id" /> | `DELETE` | <CopyableCode code="scheduleDefinitionId, subscriptionId" /> | Delete access review schedule definition |
| <CopyableCode code="create_or_update_by_id" /> | `EXEC` | <CopyableCode code="scheduleDefinitionId, subscriptionId" /> | Create or Update access review schedule definition. |
| <CopyableCode code="get_by_id" /> | `EXEC` | <CopyableCode code="scheduleDefinitionId, subscriptionId" /> | Get single access review definition |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="scheduleDefinitionId, subscriptionId" /> | Stop access review definition |
