---
title: network_service_design_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - network_service_design_groups
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>network_service_design_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.network_service_design_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | network service design group properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId" /> | Gets information about the specified networkServiceDesign group. |
| <CopyableCode code="list_by_publisher" /> | `SELECT` | <CopyableCode code="publisherName, resourceGroupName, subscriptionId" /> | Gets information of the network service design groups under a publisher. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId" /> | Creates or updates a network service design group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId" /> | Deletes a specified network service design group. |
| <CopyableCode code="_list_by_publisher" /> | `EXEC` | <CopyableCode code="publisherName, resourceGroupName, subscriptionId" /> | Gets information of the network service design groups under a publisher. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="networkServiceDesignGroupName, publisherName, resourceGroupName, subscriptionId" /> | Updates a network service design groups resource. |
