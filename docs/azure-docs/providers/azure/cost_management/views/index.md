---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
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
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.views" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="eTag" /> | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| <CopyableCode code="properties" /> | `object` | The properties of the view. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="viewName" /> | Gets the view by view name. |
| <CopyableCode code="list" /> | `SELECT` |  | Lists all views by tenant and object. |
| <CopyableCode code="list_by_scope" /> | `SELECT` | <CopyableCode code="scope" /> | Lists all views at the given scope. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="viewName" /> | The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="viewName" /> | The operation to delete a view. |
| <CopyableCode code="delete_by_scope" /> | `DELETE` | <CopyableCode code="scope, viewName" /> | The operation to delete a view. |
| <CopyableCode code="create_or_update_by_scope" /> | `EXEC` | <CopyableCode code="scope, viewName" /> | The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |
| <CopyableCode code="get_by_scope" /> | `EXEC` | <CopyableCode code="scope, viewName" /> | Gets the view for the defined scope by view name. |
