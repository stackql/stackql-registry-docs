---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - recovery_services_backup
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the Operation. |
| <CopyableCode code="display" /> | `object` | Localized display information of an operation. |
| <CopyableCode code="origin" /> | `string` | The intended executor of the operation;governs the display of the operation in the RBAC UX and the audit logs UX |
| <CopyableCode code="properties" /> | `object` | Class to represent shoebox properties in json client discovery. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version" /> |
