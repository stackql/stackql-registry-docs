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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles_enriching_kpis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.profiles_enriching_kpis" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `object` | Localized description for the KPI. |
| <CopyableCode code="aliases" /> | `array` | The aliases. |
| <CopyableCode code="calculationWindow" /> | `string` | The calculation window. |
| <CopyableCode code="calculationWindowFieldName" /> | `string` | Name of calculation window field. |
| <CopyableCode code="displayName" /> | `object` | Localized display name for the KPI. |
| <CopyableCode code="entityType" /> | `string` | The mapping entity type. |
| <CopyableCode code="entityTypeName" /> | `string` | The mapping entity name. |
| <CopyableCode code="expression" /> | `string` | The computation expression for the KPI. |
| <CopyableCode code="extracts" /> | `array` | The KPI extracts. |
| <CopyableCode code="filter" /> | `string` | The filter expression for the KPI. |
| <CopyableCode code="function" /> | `string` | The computation function for the KPI. |
| <CopyableCode code="groupBy" /> | `array` | the group by properties for the KPI. |
| <CopyableCode code="groupByMetadata" /> | `array` | The KPI GroupByMetadata. |
| <CopyableCode code="kpiName" /> | `string` | The KPI name. |
| <CopyableCode code="participantProfilesMetadata" /> | `array` | The participant profiles. |
| <CopyableCode code="provisioningState" /> | `string` | Provisioning state. |
| <CopyableCode code="tenantId" /> | `string` | The hub name. |
| <CopyableCode code="thresHolds" /> | `object` | Defines the KPI Threshold limits. |
| <CopyableCode code="unit" /> | `string` | The unit of measurement for the KPI. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, profileName, resourceGroupName, subscriptionId" /> |
