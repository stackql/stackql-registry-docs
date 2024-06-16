---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - iot_central
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_central.apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (either system assigned, or none) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of an IoT Central application. |
| <CopyableCode code="sku" /> | `object` | Information about the SKU of the IoT Central application. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Get the metadata of an IoT Central application. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Get all the IoT Central Applications in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Get all IoT Central Applications in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId, data__sku" /> | Create or update the metadata of an IoT Central application. The usual pattern to modify a property is to retrieve the IoT Central application metadata and security metadata, and then combine them with the modified values in a new body to update the IoT Central application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Delete an IoT Central application. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId, data__name" /> | Check if an IoT Central application name is available. |
| <CopyableCode code="check_subdomain_availability" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId, data__name" /> | Check if an IoT Central application subdomain is available. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Update the metadata of an IoT Central application. |
