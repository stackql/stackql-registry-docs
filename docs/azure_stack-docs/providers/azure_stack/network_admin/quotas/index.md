---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
  - network_admin
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
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.network_admin.quotas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Region location of resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a quota. |
| <CopyableCode code="tags" /> | `object` | List of key value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceName, subscriptionId" /> | Get a quota by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List all quotas. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="location, resourceName, subscriptionId" /> | Create or update a quota. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="location, resourceName, subscriptionId" /> | Delete a quota by name. |
