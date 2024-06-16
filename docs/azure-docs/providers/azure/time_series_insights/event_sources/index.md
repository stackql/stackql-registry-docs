---
title: event_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - event_sources
  - time_series_insights
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
<tr><td><b>Name</b></td><td><code>event_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.time_series_insights.event_sources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | The kind of the event source. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, eventSourceName, resourceGroupName, subscriptionId" /> | Gets the event source with the specified name in the specified environment. |
| <CopyableCode code="list_by_environment" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Lists all the available event sources associated with the subscription and within the specified resource group and environment. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, eventSourceName, resourceGroupName, subscriptionId, data__kind" /> | Create or update an event source under the specified environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, eventSourceName, resourceGroupName, subscriptionId" /> | Deletes the event source with the specified name in the specified subscription, resource group, and environment |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="environmentName, eventSourceName, resourceGroupName, subscriptionId, data__kind" /> | Updates the event source with the specified name in the specified subscription, resource group, and environment. |
