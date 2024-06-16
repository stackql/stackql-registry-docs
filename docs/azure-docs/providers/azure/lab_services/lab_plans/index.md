---
title: lab_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - lab_plans
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
<tr><td><b>Name</b></td><td><code>lab_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.lab_plans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Lab plan resource properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Retrieves the properties of a Lab Plan. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` |  | Returns a list of all lab plans for a subscription and resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` |  | Returns a list of all lab plans within a subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="data__properties" /> | Operation to create or update a Lab Plan resource. |
| <CopyableCode code="delete" /> | `DELETE` |  | Operation to delete a Lab Plan resource. Deleting a lab plan does not delete labs associated with a lab plan, nor does it delete shared images added to a gallery via the lab plan permission container. |
| <CopyableCode code="save_image" /> | `EXEC` |  | Saves an image from a lab VM to the attached shared image gallery. |
| <CopyableCode code="update" /> | `EXEC` |  | Operation to update a Lab Plan resource. |
