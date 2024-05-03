---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - data_box_edge
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
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.devices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The object name. |
| <CopyableCode code="etag" /> | `string` | The etag for the devices. |
| <CopyableCode code="identity" /> | `object` | Msi identity details of the resource |
| <CopyableCode code="kind" /> | `string` | The kind of the device. |
| <CopyableCode code="location" /> | `string` | The location of the device. This is a supported and registered Azure geographical region (for example, West US, East US, or Southeast Asia). The geographical region of a device cannot be changed once it is created, but if an identical geographical region is specified on update, the request will succeed. |
| <CopyableCode code="properties" /> | `object` | The properties of the Data Box Edge/Gateway device. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The list of tags that describe the device. These tags can be used to view and group this device (across resource groups). |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Gets the properties of the Data Box Edge/Data Box Gateway device. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the Data Box Edge/Data Box Gateway devices in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the Data Box Edge/Data Box Gateway devices in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates a Data Box Edge/Data Box Gateway resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Deletes the Data Box Edge/Data Box Gateway device. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the Data Box Edge/Data Box Gateway devices in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets all the Data Box Edge/Data Box Gateway devices in a subscription. |
| <CopyableCode code="download_updates" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="generate_certificate" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Generates certificate for activation key. |
| <CopyableCode code="install_updates" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="scan_for_updates" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Modifies a Data Box Edge/Data Box Gateway resource. |
| <CopyableCode code="upload_certificate" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId, data__properties" /> | Uploads registration certificate for the device. |
