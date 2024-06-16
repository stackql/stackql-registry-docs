---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - hardware_security_modules
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hardware_security_modules.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the Dedicated HSM Resource Provider Operation. |
| <CopyableCode code="display" /> | `object` | The display string. |
| <CopyableCode code="isDataAction" /> | `boolean` | Gets or sets a value indicating whether it is a data plane action |
| <CopyableCode code="origin" /> | `string` | The origin of the operation |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
