---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - cdn
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125; |
| <CopyableCode code="display" /> | `` | The object that represents the operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | Indicates whether the operation is a data action |
| <CopyableCode code="origin" /> | `string` | The origin of operations. |
| <CopyableCode code="properties" /> | `object` | Properties of operation, include metric specifications. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
