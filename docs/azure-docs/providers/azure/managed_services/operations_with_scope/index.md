---
title: operations_with_scope
hide_title: false
hide_table_of_contents: false
keywords:
  - operations_with_scope
  - managed_services
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
<tr><td><b>Name</b></td><td><code>operations_with_scope</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_services.operations_with_scope" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The operation name with the format: &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125; |
| <CopyableCode code="display" /> | `` | The object that represents the operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="scope" /> |
