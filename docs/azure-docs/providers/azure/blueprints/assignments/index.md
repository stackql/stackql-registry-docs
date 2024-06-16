---
title: assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - assignments
  - blueprints
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
<tr><td><b>Name</b></td><td><code>assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.blueprints.assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed identity generic object. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Detailed properties for a blueprint assignment. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assignmentName, resourceScope" /> | Get a blueprint assignment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceScope" /> | List blueprint assignments within a subscription or a management group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="assignmentName, resourceScope, data__identity, data__properties" /> | Create or update a blueprint assignment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assignmentName, resourceScope" /> | Delete a blueprint assignment. |
| <CopyableCode code="who_is_blueprint" /> | `EXEC` | <CopyableCode code="assignmentName, resourceScope" /> | Get Blueprints service SPN objectId |
