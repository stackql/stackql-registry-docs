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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asset_endpoint_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_registry.asset_endpoint_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the Asset Endpoint Profile properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assetEndpointProfileName, resourceGroupName, subscriptionId" /> | Retrieve a single Asset Endpoint Profile. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all Asset Endpoint Profiles in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all Asset Endpoint Profiles in a subscription. |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="assetEndpointProfileName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a new Asset Endpoint Profile or replace an existing Asset Endpoint Profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assetEndpointProfileName, resourceGroupName, subscriptionId" /> | Delete an Asset Endpoint Profile. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all Asset Endpoint Profiles in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List all Asset Endpoint Profiles in a subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="assetEndpointProfileName, resourceGroupName, subscriptionId" /> | Update specific Asset Endpoint Profile properties. |
