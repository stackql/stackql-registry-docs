---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - storage_pool
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_pool.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation being performed on this particular object |
| <CopyableCode code="actionType" /> | `string` | Indicates the action type. |
| <CopyableCode code="display" /> | `object` | Metadata about an operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | Indicates whether the operation applies to data-plane. |
| <CopyableCode code="origin" /> | `string` | The intended executor of the operation; governs the display of the operation in the RBAC UX and the audit logs UX. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
| <CopyableCode code="_list" /> | `EXEC` |  |
