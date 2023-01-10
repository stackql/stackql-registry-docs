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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kpi</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.kpi</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | Defines the KPI Threshold limits. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Kpi_Get` | `SELECT` | `hubName, kpiName, resourceGroupName, subscriptionId` | Gets a KPI in the hub. |
| `Kpi_ListByHub` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets all the KPIs in the specified hub. |
| `Kpi_CreateOrUpdate` | `INSERT` | `hubName, kpiName, resourceGroupName, subscriptionId` | Creates a KPI or updates an existing KPI in the hub. |
| `Kpi_Delete` | `DELETE` | `hubName, kpiName, resourceGroupName, subscriptionId` | Deletes a KPI in the hub. |
| `Kpi_Reprocess` | `EXEC` | `hubName, kpiName, resourceGroupName, subscriptionId` | Reprocesses the Kpi values of the specified KPI. |
