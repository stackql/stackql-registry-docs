---
title: access_review_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_instances
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
<tr><td><b>Name</b></td><td><code>access_review_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review instance id. |
| <CopyableCode code="name" /> | `string` | The access review instance name. |
| <CopyableCode code="properties" /> | `object` | Access Review Instance properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scheduleDefinitionId, subscriptionId" /> | Get access review instances |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="id, scheduleDefinitionId, subscriptionId" /> | Update access review instance. |
| <CopyableCode code="get_by_id" /> | `EXEC` | <CopyableCode code="id, scheduleDefinitionId, subscriptionId" /> | Get access review instances |
