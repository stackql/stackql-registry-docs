---
title: rules_engines
hide_title: false
hide_table_of_contents: false
keywords:
  - rules_engines
  - front_door
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
<tr><td><b>Name</b></td><td><code>rules_engines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.front_door.rules_engines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties required to create a Rules Engine Configuration. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="frontDoorName, resourceGroupName, rulesEngineName, subscriptionId" /> | Gets a Rules Engine Configuration with the specified name within the specified Front Door. |
| <CopyableCode code="list_by_front_door" /> | `SELECT` | <CopyableCode code="frontDoorName, resourceGroupName, subscriptionId" /> | Lists all of the Rules Engine Configurations within a Front Door. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="frontDoorName, resourceGroupName, rulesEngineName, subscriptionId" /> | Creates a new Rules Engine Configuration with the specified name within the specified Front Door. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="frontDoorName, resourceGroupName, rulesEngineName, subscriptionId" /> | Deletes an existing Rules Engine Configuration with the specified parameters. |
| <CopyableCode code="_list_by_front_door" /> | `EXEC` | <CopyableCode code="frontDoorName, resourceGroupName, subscriptionId" /> | Lists all of the Rules Engine Configurations within a Front Door. |
