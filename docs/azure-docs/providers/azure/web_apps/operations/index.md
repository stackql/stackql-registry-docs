---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - web_apps
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.operations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Description for Check if a resource name is available. |
| `GetPublishingUser` | `EXEC` |  | Description for Gets publishing user |
| `GetSourceControl` | `EXEC` | `sourceControlType` | Description for Gets source control token |
| `GetSubscriptionDeploymentLocations` | `EXEC` | `subscriptionId` | Description for Gets list of available geo regions plus ministamps |
| `ListBillingMeters` | `EXEC` | `subscriptionId` | Description for Gets a list of meters for a given location. |
| `ListCustomHostNameSites` | `EXEC` | `subscriptionId` |  |
| `ListGeoRegions` | `EXEC` | `subscriptionId` | Description for Get a list of available geographical regions. |
| `ListPremierAddOnOffers` | `EXEC` | `subscriptionId` | Description for List all premier add-on offers. |
| `ListSiteIdentifiersAssignedToHostName` | `EXEC` | `subscriptionId` | Description for List all apps that are assigned to a hostname. |
| `ListSkus` | `EXEC` | `subscriptionId` | Description for List all SKUs. |
| `ListSourceControls` | `EXEC` |  | Description for Gets the source controls available for Azure websites. |
| `Move` | `EXEC` | `resourceGroupName, subscriptionId` | Description for Move resources between resource groups. |
| `UpdatePublishingUser` | `EXEC` |  | Description for Updates publishing user |
| `UpdateSourceControl` | `EXEC` | `sourceControlType` | Description for Updates source control token |
| `Validate` | `EXEC` | `resourceGroupName, subscriptionId, data__location, data__name, data__properties, data__type` | Description for Validate if a resource can be created. |
| `ValidateMove` | `EXEC` | `resourceGroupName, subscriptionId` | Description for Validate whether a resource can be moved. |
| `VerifyHostingEnvironmentVnet` | `EXEC` | `subscriptionId` | Description for Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules. |
