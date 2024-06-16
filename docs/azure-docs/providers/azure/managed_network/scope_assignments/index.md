---
title: scope_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_assignments
  - managed_network
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
<tr><td><b>Name</b></td><td><code>scope_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network.scope_assignments" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="scope, scopeAssignmentName" /> | Get the specified scope assignment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get the specified scope assignment. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="scope, scopeAssignmentName" /> | Creates a scope assignment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="scope, scopeAssignmentName" /> | Deletes a scope assignment. |
