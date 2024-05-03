---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - purview
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource Id |
| <CopyableCode code="name" /> | `object` | Quota name |
| <CopyableCode code="currentValue" /> | `integer` | Current usage quota value |
| <CopyableCode code="limit" /> | `integer` | Usage quota limit |
| <CopyableCode code="unit" /> | `string` | Quota usage unit. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, location, subscriptionId" /> |
| <CopyableCode code="_get" /> | `EXEC` | <CopyableCode code="api-version, location, subscriptionId" /> |
