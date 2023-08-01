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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_feature_capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.component_feature_capabilities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `WorkItemIntegration` | `boolean` | Whether allow to use work item integration feature. |
| `TrackingType` | `string` | The application insights component used tracking type. |
| `DailyCapResetTime` | `number` | Daily data volume cap UTC reset hour. |
| `AnalyticsIntegration` | `boolean` | Reserved, not used now. |
| `MetadataClass` | `string` | Reserved, not used now. |
| `ApplicationMap` | `boolean` | Reserved, not used now. |
| `DailyCap` | `number` | Daily data volume cap in GB. |
| `ThrottleRate` | `number` | Reserved, not used now. |
| `ProactiveDetection` | `boolean` | Reserved, not used now. |
| `LiveStreamMetrics` | `boolean` | Reserved, not used now. |
| `BurstThrottlePolicy` | `string` | Reserved, not used now. |
| `PowerBIIntegration` | `boolean` | Reserved, not used now. |
| `ApiAccessLevel` | `string` | Reserved, not used now. |
| `OpenSchema` | `boolean` | Reserved, not used now. |
| `MultipleStepWebTest` | `boolean` | Whether allow to use multiple steps web test feature. |
| `SupportExportData` | `boolean` | Whether allow to use continuous export feature. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ComponentFeatureCapabilities_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
