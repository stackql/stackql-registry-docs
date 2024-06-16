---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - search
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation. This name is of the form &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125;. |
| <CopyableCode code="display" /> | `` | The object that describes the operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | Describes if the specified operation is a data plane API operation. Operations where this value is not true are supported directly by the resource provider. |
| <CopyableCode code="origin" /> | `string` | Describes which originating entities are allowed to invoke this operation. |
| <CopyableCode code="properties" /> | `object` | Describes additional properties for this operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
