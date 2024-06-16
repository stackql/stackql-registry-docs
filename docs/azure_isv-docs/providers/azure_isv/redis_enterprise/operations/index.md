---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - redis_enterprise
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis_enterprise.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation, as per Resource-Based Access Control (RBAC). Examples: "Microsoft.Compute/virtualMachines/write", "Microsoft.Compute/virtualMachines/capture/action" |
| <CopyableCode code="actionType" /> | `string` | Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs. |
| <CopyableCode code="display" /> | `object` | Localized display information for this particular operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | Whether the operation applies to data-plane. This is "true" for data-plane operations and "false" for ARM/control-plane operations. |
| <CopyableCode code="origin" /> | `string` | The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit logs UX. Default value is "user,system" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
