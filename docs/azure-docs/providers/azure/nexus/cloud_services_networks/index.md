---
title: cloud_services_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_services_networks
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
<tr><td><b>Name</b></td><td><code>cloud_services_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.cloud_services_networks" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudServicesNetworkName, resourceGroupName, subscriptionId" /> | Get properties of the provided cloud services network. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of cloud services networks in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of cloud services networks in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudServicesNetworkName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a new cloud services network or update the properties of the existing cloud services network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudServicesNetworkName, resourceGroupName, subscriptionId" /> | Delete the provided cloud services network. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="cloudServicesNetworkName, resourceGroupName, subscriptionId" /> | Update properties of the provided cloud services network, or update the tags associated with it. Properties and tag updates can be done independently. |
