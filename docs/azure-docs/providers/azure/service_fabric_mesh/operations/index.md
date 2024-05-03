---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - service_fabric_mesh
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_mesh.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation. |
| <CopyableCode code="display" /> | `object` | An operation available at the listed Azure resource provider. |
| <CopyableCode code="nextLink" /> | `string` | The URL to use for getting the next set of results. |
| <CopyableCode code="origin" /> | `string` | Origin result |
| <CopyableCode code="properties" /> | `object` | Properties available for a Microsoft.Web resource provider operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version" /> |
