---
title: dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboards
  - portal
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
<tr><td><b>Name</b></td><td><code>dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.portal.dashboards" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | The shared dashboard properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dashboardName, resourceGroupName, subscriptionId" /> | Gets the Dashboard. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the Dashboards within a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the dashboards within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dashboardName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates a Dashboard. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dashboardName, resourceGroupName, subscriptionId" /> | Deletes the Dashboard. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dashboardName, resourceGroupName, subscriptionId" /> | Updates an existing Dashboard. |
