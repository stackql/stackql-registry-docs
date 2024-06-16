---
title: formulas
hide_title: false
hide_table_of_contents: false
keywords:
  - formulas
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>formulas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.formulas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a formula. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Get formula. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, labName, resourceGroupName, subscriptionId" /> | List formulas in a given lab. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId, data__properties" /> | Create or replace an existing formula. This operation can take a while to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Delete formula. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Allows modifying tags of formulas. All other properties will be ignored. |
