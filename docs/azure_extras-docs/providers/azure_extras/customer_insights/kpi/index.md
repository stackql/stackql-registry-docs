---
title: kpi
hide_title: false
hide_table_of_contents: false
keywords:
  - kpi
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
<tr><td><b>Name</b></td><td><code>kpi</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.kpi" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | Defines the KPI Threshold limits. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, kpiName, resourceGroupName, subscriptionId" /> | Gets a KPI in the hub. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all the KPIs in the specified hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, kpiName, resourceGroupName, subscriptionId" /> | Creates a KPI or updates an existing KPI in the hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, kpiName, resourceGroupName, subscriptionId" /> | Deletes a KPI in the hub. |
| <CopyableCode code="_list_by_hub" /> | `EXEC` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all the KPIs in the specified hub. |
| <CopyableCode code="reprocess" /> | `EXEC` | <CopyableCode code="hubName, kpiName, resourceGroupName, subscriptionId" /> | Reprocesses the Kpi values of the specified KPI. |
