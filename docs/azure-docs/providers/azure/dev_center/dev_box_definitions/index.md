---
title: dev_box_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_box_definitions
  - dev_center
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
<tr><td><b>Name</b></td><td><code>dev_box_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.dev_box_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a Dev Box definition. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Gets a Dev Box definition |
| <CopyableCode code="list_by_dev_center" /> | `SELECT` |  | List Dev Box definitions for a devcenter. |
| <CopyableCode code="list_by_project" /> | `SELECT` |  | List Dev Box definitions configured for a project. |
| <CopyableCode code="create_or_update" /> | `INSERT` |  | Creates or updates a Dev Box definition. |
| <CopyableCode code="delete" /> | `DELETE` |  | Deletes a Dev Box definition |
| <CopyableCode code="get_by_project" /> | `EXEC` |  | Gets a Dev Box definition configured for a project |
| <CopyableCode code="update" /> | `EXEC` |  | Partially updates a Dev Box definition. |
