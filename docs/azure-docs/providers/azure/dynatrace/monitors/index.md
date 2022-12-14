---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - dynatrace
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
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dynatrace.monitors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | The properties of the managed service identities assigned to this resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties specific to the monitor resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Monitors_Get` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `Monitors_ListBySubscriptionId` | `SELECT` | `subscriptionId` |
| `Monitors_CreateOrUpdate` | `INSERT` | `monitorName, resourceGroupName, subscriptionId, data__properties` |
| `Monitors_Delete` | `DELETE` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_GetAccountCredentials` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_GetSSODetails` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_GetVMHostPayload` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_ListAppServices` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_ListHosts` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_ListLinkableEnvironments` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_ListMonitoredResources` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitors_Update` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
