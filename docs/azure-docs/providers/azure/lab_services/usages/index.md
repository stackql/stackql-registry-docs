---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - lab_services
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified arm resource id. |
| <CopyableCode code="name" /> | `object` | The Usage Names. |
| <CopyableCode code="currentValue" /> | `integer` | The current usage. |
| <CopyableCode code="limit" /> | `integer` | The limit integer. |
| <CopyableCode code="unit" /> | `string` | The unit details. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_location" /> | `SELECT` |  |
| <CopyableCode code="_list_by_location" /> | `EXEC` |  |
