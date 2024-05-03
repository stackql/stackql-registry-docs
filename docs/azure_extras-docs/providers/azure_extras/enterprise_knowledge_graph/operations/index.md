---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - enterprise_knowledge_graph
  - azure_extras    
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.enterprise_knowledge_graph.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Operation name: &#123;provider&#125;/&#123;resource&#125;/&#123;operation&#125;. |
| <CopyableCode code="display" /> | `object` | The operation supported by EnterpriseKnowledgeGraph Service Management. |
| <CopyableCode code="origin" /> | `string` | The origin of the operation. |
| <CopyableCode code="properties" /> | `object` | Additional properties. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
| <CopyableCode code="_list" /> | `EXEC` |  |
