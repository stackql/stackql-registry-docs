---
title: admin_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - admin_rules
  - network
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
<tr><td><b>Name</b></td><td><code>admin_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.admin_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="kind" /> | `string` | Whether the rule is custom or default. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Gets a network manager security configuration admin rule. |
| <CopyableCode code="list" /> | `SELECT` |  | List all network manager security configuration admin rules. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="data__kind" /> | Creates or updates an admin rule. |
| <CopyableCode code="delete" /> | `DELETE` |  | Deletes an admin rule. |
| <CopyableCode code="_list" /> | `EXEC` |  | List all network manager security configuration admin rules. |
