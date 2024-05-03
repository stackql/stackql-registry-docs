---
title: component_feature_capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - component_feature_capabilities
  - application_insights
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
<tr><td><b>Name</b></td><td><code>component_feature_capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.component_feature_capabilities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="AnalyticsIntegration" /> | `boolean` | Reserved, not used now. |
| <CopyableCode code="ApiAccessLevel" /> | `string` | Reserved, not used now. |
| <CopyableCode code="ApplicationMap" /> | `boolean` | Reserved, not used now. |
| <CopyableCode code="BurstThrottlePolicy" /> | `string` | Reserved, not used now. |
| <CopyableCode code="DailyCap" /> | `number` | Daily data volume cap in GB. |
| <CopyableCode code="DailyCapResetTime" /> | `number` | Daily data volume cap UTC reset hour. |
| <CopyableCode code="LiveStreamMetrics" /> | `boolean` | Reserved, not used now. |
| <CopyableCode code="MetadataClass" /> | `string` | Reserved, not used now. |
| <CopyableCode code="MultipleStepWebTest" /> | `boolean` | Whether allow to use multiple steps web test feature. |
| <CopyableCode code="OpenSchema" /> | `boolean` | Reserved, not used now. |
| <CopyableCode code="PowerBIIntegration" /> | `boolean` | Reserved, not used now. |
| <CopyableCode code="ProactiveDetection" /> | `boolean` | Reserved, not used now. |
| <CopyableCode code="SupportExportData" /> | `boolean` | Whether allow to use continuous export feature. |
| <CopyableCode code="ThrottleRate" /> | `number` | Reserved, not used now. |
| <CopyableCode code="TrackingType" /> | `string` | The application insights component used tracking type. |
| <CopyableCode code="WorkItemIntegration" /> | `boolean` | Whether allow to use work item integration feature. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |
