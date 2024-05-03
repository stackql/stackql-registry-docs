---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - customer_lockbox
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.customer_lockbox.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Gets or sets action name |
| <CopyableCode code="display" /> | `object` | Contains the localized display information for this particular operation / action. |
| <CopyableCode code="isDataAction" /> | `string` | Gets or sets a value indicating whether it is a data plane action |
| <CopyableCode code="origin" /> | `string` | Gets or sets origin |
| <CopyableCode code="properties" /> | `string` | Gets or sets properties |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
| <CopyableCode code="_list" /> | `EXEC` |  |
