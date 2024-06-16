---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - vmware
  - azure_isv    
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the operation being performed on this object |
| <CopyableCode code="display" /> | `` | Contains the localized display information for this operation |
| <CopyableCode code="isDataAction" /> | `boolean` | Gets or sets a value indicating whether the operation is a data action or not |
| <CopyableCode code="origin" /> | `string` | Origin of the operation |
| <CopyableCode code="properties" /> | `object` | Extra Operation properties |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
