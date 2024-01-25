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
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | A setting that contains all of the configuration for the automatic scaling of a resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| `type` | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `autoscaleSettingName, resourceGroupName, subscriptionId` | Gets an autoscale setting |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the autoscale settings for a resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists the autoscale settings for a subscription |
| `create_or_update` | `INSERT` | `autoscaleSettingName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an autoscale setting. |
| `delete` | `DELETE` | `autoscaleSettingName, resourceGroupName, subscriptionId` | Deletes and autoscale setting |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists the autoscale settings for a resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists the autoscale settings for a subscription |
| `update` | `EXEC` | `autoscaleSettingName, resourceGroupName, subscriptionId` | Updates an existing AutoscaleSettingsResource. To update other fields use the CreateOrUpdate method. |
