---
title: asset_endpoint_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - asset_endpoint_profiles
  - device_registry
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
<tr><td><b>Name</b></td><td><code>asset_endpoint_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.device_registry.asset_endpoint_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | The extended location. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Defines the Asset Endpoint Profile properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `assetEndpointProfileName, resourceGroupName, subscriptionId` | Retrieve a single Asset Endpoint Profile. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all Asset Endpoint Profiles in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all Asset Endpoint Profiles in a subscription. |
| `create_or_replace` | `INSERT` | `assetEndpointProfileName, resourceGroupName, subscriptionId, data__extendedLocation` | Create a new Asset Endpoint Profile or replace an existing Asset Endpoint Profile. |
| `delete` | `DELETE` | `assetEndpointProfileName, resourceGroupName, subscriptionId` | Delete an Asset Endpoint Profile. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all Asset Endpoint Profiles in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all Asset Endpoint Profiles in a subscription. |
| `update` | `EXEC` | `assetEndpointProfileName, resourceGroupName, subscriptionId` | Update specific Asset Endpoint Profile properties. |
