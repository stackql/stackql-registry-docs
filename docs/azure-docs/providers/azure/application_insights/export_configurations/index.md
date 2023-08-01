---
title: export_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - export_configurations
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
<tr><td><b>Name</b></td><td><code>export_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.export_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `LastSuccessTime` | `string` | The last time data was successfully delivered to the destination storage container for this Continuous Export configuration. |
| `ExportId` | `string` | The unique ID of the export configuration inside an Application Insights component. It is auto generated when the Continuous Export configuration is created. |
| `StorageName` | `string` | The name of the destination storage account. |
| `DestinationStorageSubscriptionId` | `string` | The destination storage account subscription ID. |
| `DestinationType` | `string` | The destination type. |
| `NotificationQueueEnabled` | `string` | Deprecated |
| `DestinationStorageLocationId` | `string` | The destination account location ID. |
| `ContainerName` | `string` | The name of the destination storage container. |
| `ApplicationName` | `string` | The name of the Application Insights component. |
| `DestinationAccountId` | `string` | The name of destination account. |
| `ExportStatus` | `string` | This indicates current Continuous Export configuration status. The possible values are 'Preparing', 'Success', 'Failure'. |
| `IsUserEnabled` | `string` | This will be 'true' if the Continuous Export configuration is enabled, otherwise it will be 'false'. |
| `RecordTypes` | `string` | This comma separated list of document types that will be exported. The possible values include 'Requests', 'Event', 'Exceptions', 'Metrics', 'PageViews', 'PageViewPerformance', 'Rdd', 'PerformanceCounters', 'Availability', 'Messages'. |
| `LastGapTime` | `string` | The last time the Continuous Export configuration started failing. |
| `ResourceGroup` | `string` | The resource group of the Application Insights component. |
| `SubscriptionId` | `string` | The subscription of the Application Insights component. |
| `LastUserUpdate` | `string` | Last time the Continuous Export configuration was updated. |
| `PermanentErrorReason` | `string` | This is the reason the Continuous Export configuration started failing. It can be 'AzureStorageNotFound' or 'AzureStorageAccessDenied'. |
| `InstrumentationKey` | `string` | The instrumentation key of the Application Insights component. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExportConfigurations_Get` | `SELECT` | `exportId, resourceGroupName, resourceName, subscriptionId` | Get the Continuous Export configuration for this export id. |
| `ExportConfigurations_List` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Gets a list of Continuous Export configuration of an Application Insights component. |
| `ExportConfigurations_Create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create a Continuous Export configuration of an Application Insights component. |
| `ExportConfigurations_Delete` | `DELETE` | `exportId, resourceGroupName, resourceName, subscriptionId` | Delete a Continuous Export configuration of an Application Insights component. |
| `ExportConfigurations_Update` | `EXEC` | `exportId, resourceGroupName, resourceName, subscriptionId` | Update the Continuous Export configuration for this export id. |
