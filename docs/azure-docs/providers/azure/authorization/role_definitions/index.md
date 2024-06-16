---
title: role_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - role_definitions
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
<tr><td><b>Name</b></td><td><code>role_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The role definition ID. |
| <CopyableCode code="name" /> | `string` | The role definition name. |
| <CopyableCode code="properties" /> | `object` | Role definition properties. |
| <CopyableCode code="type" /> | `string` | The role definition type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="roleDefinitionId, scope" /> | Get role definition by ID (GUID). |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get all role definitions that are applicable at scope and above. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="roleDefinitionId, scope" /> | Creates or updates a role definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="roleDefinitionId, scope" /> | Deletes a role definition. |
