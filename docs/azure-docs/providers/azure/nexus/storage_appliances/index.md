---
title: storage_appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_appliances
  - nexus
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
<tr><td><b>Name</b></td><td><code>storage_appliances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.storage_appliances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageApplianceName, subscriptionId" /> | Get properties of the provided storage appliance. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of storage appliances in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of storage appliances in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, storageApplianceName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new storage appliance or update the properties of the existing one.<br />All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, storageApplianceName, subscriptionId" /> | Delete the provided storage appliance.<br />All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| <CopyableCode code="disable_remote_vendor_management" /> | `EXEC` | <CopyableCode code="resourceGroupName, storageApplianceName, subscriptionId" /> | Disable remote vendor management of the provided storage appliance. |
| <CopyableCode code="enable_remote_vendor_management" /> | `EXEC` | <CopyableCode code="resourceGroupName, storageApplianceName, subscriptionId" /> | Enable remote vendor management of the provided storage appliance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, storageApplianceName, subscriptionId" /> | Update properties of the provided storage appliance, or update tags associated with the storage appliance Properties and tag updates can be done independently. |
