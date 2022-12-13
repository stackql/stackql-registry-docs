---
title: autoscale_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - autoscale_settings
  - monitor
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
<tr><td><b>Name</b></td><td><code>autoscale_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.autoscale_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | A setting that contains all of the configuration for the automatic scaling of a resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AutoscaleSettings_Get` | `SELECT` | `autoscaleSettingName, resourceGroupName, subscriptionId` | Gets an autoscale setting |
| `AutoscaleSettings_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the autoscale settings for a resource group |
| `AutoscaleSettings_ListBySubscription` | `SELECT` | `subscriptionId` | Lists the autoscale settings for a subscription |
| `AutoscaleSettings_CreateOrUpdate` | `INSERT` | `autoscaleSettingName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an autoscale setting. |
| `AutoscaleSettings_Delete` | `DELETE` | `autoscaleSettingName, resourceGroupName, subscriptionId` | Deletes and autoscale setting |
| `AutoscaleSettings_Update` | `EXEC` | `autoscaleSettingName, resourceGroupName, subscriptionId` | Updates an existing AutoscaleSettingsResource. To update other fields use the CreateOrUpdate method. |
