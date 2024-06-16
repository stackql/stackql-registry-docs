---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
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
<tr><td><b>Name</b></td><td><code>pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a Pool |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Gets a machine pool |
| <CopyableCode code="list_by_project" /> | `SELECT` |  | Lists pools for a project |
| <CopyableCode code="create_or_update" /> | `INSERT` |  | Creates or updates a machine pool |
| <CopyableCode code="delete" /> | `DELETE` |  | Deletes a machine pool |
| <CopyableCode code="run_health_checks" /> | `EXEC` | <CopyableCode code="poolName, projectName, resourceGroupName, subscriptionId" /> | Triggers a refresh of the pool status. |
| <CopyableCode code="update" /> | `EXEC` |  | Partially updates a machine pool |
