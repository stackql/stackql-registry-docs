---
title: access_control_records
hide_title: false
hide_table_of_contents: false
keywords:
  - access_control_records
  - storsimple_1200_series
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
<tr><td><b>Name</b></td><td><code>access_control_records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.access_control_records" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | Properties of access control record |
| <CopyableCode code="type" /> | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessControlRecordName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified access control record name. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the access control records in a manager. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accessControlRecordName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or Updates an access control record. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessControlRecordName, managerName, resourceGroupName, subscriptionId" /> | Deletes the access control record. |
