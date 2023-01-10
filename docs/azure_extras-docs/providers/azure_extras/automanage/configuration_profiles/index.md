---
title: configuration_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profiles
  - automanage
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.automanage.configuration_profiles</code></td></tr>
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
| `ConfigurationProfiles_Get` | `SELECT` | `configurationProfileName, resourceGroupName, subscriptionId` | Get information about a configuration profile |
| `ConfigurationProfiles_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve a list of configuration profile within a given resource group |
| `ConfigurationProfiles_ListBySubscription` | `SELECT` | `subscriptionId` | Retrieve a list of configuration profile within a subscription |
| `ConfigurationProfiles_CreateOrUpdate` | `INSERT` | `configurationProfileName, resourceGroupName, subscriptionId` | Creates a configuration profile |
| `ConfigurationProfiles_Delete` | `DELETE` | `configurationProfileName, resourceGroupName, subscriptionId` | Delete a configuration profile |
| `ConfigurationProfiles_Update` | `EXEC` | `configurationProfileName, resourceGroupName, subscriptionId` | Updates a configuration profile |
