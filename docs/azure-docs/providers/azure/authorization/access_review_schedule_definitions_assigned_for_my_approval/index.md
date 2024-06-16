---
title: access_review_schedule_definitions_assigned_for_my_approval
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_schedule_definitions_assigned_for_my_approval
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
<tr><td><b>Name</b></td><td><code>access_review_schedule_definitions_assigned_for_my_approval</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.access_review_schedule_definitions_assigned_for_my_approval" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The access review schedule definition id. |
| <CopyableCode code="name" /> | `string` | The access review schedule definition unique id. |
| <CopyableCode code="properties" /> | `object` | Access Review. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
