---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - infrastructure_insights_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.infrastructure_insights_admin.alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The Azure Region where the resource lives |
| <CopyableCode code="properties" /> | `object` | Contains alert data. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertName, location, resourceGroupName, subscriptionId" /> | Returns the requested an alert. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns the list of all alerts in a given region. |
| <CopyableCode code="close" /> | `EXEC` | <CopyableCode code="alertName, location, resourceGroupName, subscriptionId, user" /> | Closes the given alert. |
| <CopyableCode code="repair" /> | `EXEC` | <CopyableCode code="alertName, location, resourceGroupName, subscriptionId" /> | Repairs an alert. |
