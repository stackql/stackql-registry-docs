---
title: license_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - license_profiles
  - hybrid_compute
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
<tr><td><b>Name</b></td><td><code>license_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_compute.license_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describe the properties of a license profile. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `licenseProfileName, machineName, resourceGroupName, subscriptionId` | Retrieves information about the view of a license profile. |
| `list` | `SELECT` | `machineName, resourceGroupName, subscriptionId` | The operation to get all license profiles of a non-Azure machine |
| `create_or_update` | `INSERT` | `licenseProfileName, machineName, resourceGroupName, subscriptionId` | The operation to create or update a license profile. |
| `delete` | `DELETE` | `licenseProfileName, machineName, resourceGroupName, subscriptionId` | The operation to delete a license profile. |
| `_list` | `EXEC` | `machineName, resourceGroupName, subscriptionId` | The operation to get all license profiles of a non-Azure machine |
| `update` | `EXEC` | `licenseProfileName, machineName, resourceGroupName, subscriptionId` | The operation to update a license profile. |
