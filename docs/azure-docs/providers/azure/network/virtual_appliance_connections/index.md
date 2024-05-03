---
title: virtual_appliance_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_appliance_connections
  - network
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
<tr><td><b>Name</b></td><td><code>virtual_appliance_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_appliance_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the NetworkVirtualApplianceConnection subresource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Retrieves the details of specified NVA connection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Lists NetworkVirtualApplianceConnections under the NVA. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionName, networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Creates a connection to Network Virtual Appliance, if it doesn't exist else updates the existing NVA connection' |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Deletes a NVA connection. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Lists NetworkVirtualApplianceConnections under the NVA. |
