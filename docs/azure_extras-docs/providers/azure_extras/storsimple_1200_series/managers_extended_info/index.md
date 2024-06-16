---
title: managers_extended_info
hide_title: false
hide_table_of_contents: false
keywords:
  - managers_extended_info
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
<tr><td><b>Name</b></td><td><code>managers_extended_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.managers_extended_info" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="etag" /> | `string` | ETag of the Resource |
| <CopyableCode code="properties" /> | `object` | Properties of the ManagerExtendedInfo |
| <CopyableCode code="type" /> | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Returns the extended information of the specified manager name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId, data__properties" /> | Creates the extended info of the manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Deletes the extended info of the manager. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, managerName, resourceGroupName, subscriptionId, data__properties" /> | Updates the extended info of the manager. |
