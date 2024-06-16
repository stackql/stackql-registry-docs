---
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
  - lab_services
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
<tr><td><b>Name</b></td><td><code>schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.schedules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Schedule resource properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Returns the properties of a lab Schedule. |
| <CopyableCode code="list_by_lab" /> | `SELECT` |  | Returns a list of all schedules for a lab. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="data__properties" /> | Operation to create or update a lab schedule. |
| <CopyableCode code="delete" /> | `DELETE` |  | Operation to delete a schedule resource. |
| <CopyableCode code="update" /> | `EXEC` |  | Operation to update a lab schedule. |
