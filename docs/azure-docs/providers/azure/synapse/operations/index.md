---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - synapse
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Operation name |
| <CopyableCode code="display" /> | `object` | Description of an available operation |
| <CopyableCode code="isDataAction" /> | `string` | Whether this operation is a data action |
| <CopyableCode code="origin" /> | `string` | Operation origin |
| <CopyableCode code="properties" /> | `object` | What is this? |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` |  | Get all available operations |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Check whether a workspace name is available |
