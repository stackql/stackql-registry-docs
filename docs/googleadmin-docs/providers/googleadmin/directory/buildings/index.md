---
title: buildings
hide_title: false
hide_table_of_contents: false
keywords:
  - buildings
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buildings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.buildings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A brief description of the building. For example, "Chelsea Market". |
| <CopyableCode code="address" /> | `object` | Public API: Resources.buildings |
| <CopyableCode code="buildingId" /> | `string` | Unique identifier for the building. The maximum length is 100 characters. |
| <CopyableCode code="buildingName" /> | `string` | The building name as seen by users in Calendar. Must be unique for the customer. For example, "NYC-CHEL". The maximum length is 100 characters. |
| <CopyableCode code="coordinates" /> | `object` | Public API: Resources.buildings |
| <CopyableCode code="etags" /> | `string` | ETag of the resource. |
| <CopyableCode code="floorNames" /> | `array` | The display names for all floors in this building. The floors are expected to be sorted in ascending order, from lowest floor to highest floor. For example, ["B2", "B1", "L", "1", "2", "2M", "3", "PH"] Must contain at least one entry. |
| <CopyableCode code="kind" /> | `string` | Kind of resource this is. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildingId, customer" /> | Retrieves a building. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customer" /> | Retrieves a list of buildings for an account. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="customer" /> | Inserts a building. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="buildingId, customer" /> | Deletes a building. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customer" /> | Retrieves a list of buildings for an account. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="buildingId, customer" /> | Patches a building. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="buildingId, customer" /> | Updates a building. |
