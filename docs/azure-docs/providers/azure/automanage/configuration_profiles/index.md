---
title: configuration_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profiles
  - automanage
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
<tr><td><b>Name</b></td><td><code>configuration_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automanage.configuration_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Automanage configuration profile properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `configurationProfileName, resourceGroupName, subscriptionId` | Get information about a configuration profile |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve a list of configuration profile within a given resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Retrieve a list of configuration profile within a subscription |
| `create_or_update` | `INSERT` | `configurationProfileName, resourceGroupName, subscriptionId` | Creates a configuration profile |
| `delete` | `DELETE` | `configurationProfileName, resourceGroupName, subscriptionId` | Delete a configuration profile |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieve a list of configuration profile within a given resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Retrieve a list of configuration profile within a subscription |
| `update` | `EXEC` | `configurationProfileName, resourceGroupName, subscriptionId` | Updates a configuration profile |
