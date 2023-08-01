---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
  - mobile_network
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
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.mobile_network.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Site properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Sites_Get` | `SELECT` | `mobileNetworkName, resourceGroupName, siteName, subscriptionId` | Gets information about the specified mobile network site. |
| `Sites_ListByMobileNetwork` | `SELECT` | `mobileNetworkName, resourceGroupName, subscriptionId` | Lists all sites in the mobile network. |
| `Sites_CreateOrUpdate` | `INSERT` | `mobileNetworkName, resourceGroupName, siteName, subscriptionId` | Creates or updates a mobile network site. |
| `Sites_Delete` | `DELETE` | `mobileNetworkName, resourceGroupName, siteName, subscriptionId` | Deletes the specified mobile network site. |
| `Sites_UpdateTags` | `EXEC` | `mobileNetworkName, resourceGroupName, siteName, subscriptionId` | Updates site tags. |
