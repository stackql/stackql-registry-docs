---
title: storage_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_quotas
  - storage_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>storage_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.storage_admin.storage_quotas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | Storage quota properties. |
| <CopyableCode code="type" /> | `string` | Resource Type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, quotaName, subscriptionId" /> | Returns the specified storage quota. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Returns a list of storage quotas at the given location. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="location, quotaName, subscriptionId" /> | Create or update an existing storage quota. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="location, quotaName, subscriptionId" /> | Delete an existing quota |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Returns a list of storage quotas at the given location. |
