---
title: exports
hide_title: false
hide_table_of_contents: false
keywords:
  - exports
  - cost_management
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
<tr><td><b>Name</b></td><td><code>exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.exports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="eTag" /> | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (either system assigned, or none) |
| <CopyableCode code="location" /> | `string` | The location of the Export's managed identity. Only required when utilizing managed identity. |
| <CopyableCode code="properties" /> | `object` | The properties of the export. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="exportName, scope" /> | The operation to get the export for the defined scope by export name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | The operation to list all exports at the given scope. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="exportName, scope" /> | The operation to create or update a export. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="exportName, scope" /> | The operation to delete a export. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="scope" /> | The operation to list all exports at the given scope. |
| <CopyableCode code="execute" /> | `EXEC` | <CopyableCode code="exportName, scope" /> | The operation to run an export. |
