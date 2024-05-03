---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
  - customer_insights
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.views" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The view in Customer 360 web application. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId, userId, viewName" /> | Gets a view in the hub. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId, userId" /> | Gets all available views for given user in the specified hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId, viewName" /> | Creates a view or updates an existing view in the hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, resourceGroupName, subscriptionId, userId, viewName" /> | Deletes a view in the specified hub. |
| <CopyableCode code="_list_by_hub" /> | `EXEC` | <CopyableCode code="hubName, resourceGroupName, subscriptionId, userId" /> | Gets all available views for given user in the specified hub. |
