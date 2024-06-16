---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - data_migration
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID of the quota object |
| <CopyableCode code="name" /> | `object` | The name of the quota |
| <CopyableCode code="currentValue" /> | `number` | The current value of the quota. If null or missing, the current value cannot be determined in the context of the request. |
| <CopyableCode code="limit" /> | `number` | The maximum value of the quota. If null or missing, the quota has no maximum, in which case it merely tracks usage. |
| <CopyableCode code="unit" /> | `string` | The unit for the quota, such as Count, Bytes, BytesPerSecond, etc. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, location, subscriptionId" /> |
