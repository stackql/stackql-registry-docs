---
title: profiles_enriching_kpis
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles_enriching_kpis
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
<tr><td><b>Name</b></td><td><code>profiles_enriching_kpis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.profiles_enriching_kpis</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `object` | Localized description for the KPI. |
| `aliases` | `array` | The aliases. |
| `calculationWindow` | `string` | The calculation window. |
| `calculationWindowFieldName` | `string` | Name of calculation window field. |
| `displayName` | `object` | Localized display name for the KPI. |
| `entityType` | `string` | The mapping entity type. |
| `entityTypeName` | `string` | The mapping entity name. |
| `expression` | `string` | The computation expression for the KPI. |
| `extracts` | `array` | The KPI extracts. |
| `filter` | `string` | The filter expression for the KPI. |
| `function` | `string` | The computation function for the KPI. |
| `groupBy` | `array` | the group by properties for the KPI. |
| `groupByMetadata` | `array` | The KPI GroupByMetadata. |
| `kpiName` | `string` | The KPI name. |
| `participantProfilesMetadata` | `array` | The participant profiles. |
| `provisioningState` | `string` | Provisioning state. |
| `tenantId` | `string` | The hub name. |
| `thresHolds` | `object` | Defines the KPI Threshold limits. |
| `unit` | `string` | The unit of measurement for the KPI. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `hubName, profileName, resourceGroupName, subscriptionId` |
