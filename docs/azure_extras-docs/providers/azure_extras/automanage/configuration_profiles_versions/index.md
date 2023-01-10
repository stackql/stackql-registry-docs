---
title: configuration_profiles_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profiles_versions
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
<tr><td><b>Name</b></td><td><code>configuration_profiles_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automanage.configuration_profiles_versions</code></td></tr>
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
| `ConfigurationProfilesVersions_Get` | `SELECT` | `configurationProfileName, resourceGroupName, subscriptionId, versionName` | Get information about a configuration profile version |
| `ConfigurationProfilesVersions_CreateOrUpdate` | `INSERT` | `configurationProfileName, resourceGroupName, subscriptionId, versionName` | Creates a configuration profile version |
| `ConfigurationProfilesVersions_Delete` | `DELETE` | `configurationProfileName, resourceGroupName, subscriptionId, versionName` | Delete a configuration profile version |
| `ConfigurationProfilesVersions_ListChildResources` | `EXEC` | `configurationProfileName, resourceGroupName, subscriptionId` | Retrieve a list of configuration profile version for a configuration profile  |
