---
title: asc_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - asc_usages
  - storage_cache
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
<tr><td><b>Name</b></td><td><code>asc_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.asc_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | Naming information for this resource type. |
| <CopyableCode code="currentValue" /> | `integer` | The current usage of this resource. |
| <CopyableCode code="limit" /> | `integer` | The limit (quota) for this resource. |
| <CopyableCode code="unit" /> | `string` | Unit that the limit and usages are expressed in, such as 'Count'. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> |
