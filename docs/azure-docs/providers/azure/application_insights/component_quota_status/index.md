---
title: component_quota_status
hide_title: false
hide_table_of_contents: false
keywords:
  - component_quota_status
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
<tr><td><b>Name</b></td><td><code>component_quota_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.component_quota_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `AppId` | `string` | The Application ID for the Application Insights component. |
| `ExpirationTime` | `string` | Date and time when the daily data volume cap will be reset, and data ingestion will resume. |
| `ShouldBeThrottled` | `boolean` | The daily data volume cap is met, and data ingestion will be stopped. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ComponentQuotaStatus_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
