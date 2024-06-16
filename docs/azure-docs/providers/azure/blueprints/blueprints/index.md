---
title: blueprints
hide_title: false
hide_table_of_contents: false
keywords:
  - blueprints
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
<tr><td><b>Name</b></td><td><code>blueprints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.blueprints.blueprints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | String Id used to locate any resource on Azure. |
| <CopyableCode code="name" /> | `string` | Name of this resource. |
| <CopyableCode code="properties" /> | `object` | Schema for blueprint definition properties. |
| <CopyableCode code="type" /> | `string` | Type of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="blueprintName, resourceScope" /> | Get a blueprint definition. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceScope" /> | List blueprint definitions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="blueprintName, resourceScope, data__properties" /> | Create or update a blueprint definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="blueprintName, resourceScope" /> | Delete a blueprint definition. |
