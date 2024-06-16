---
title: cluster_managers
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_managers
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
<tr><td><b>Name</b></td><td><code>cluster_managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.cluster_managers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterManagerName, resourceGroupName, subscriptionId" /> | Get the properties of the provided cluster manager. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of cluster managers in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of cluster managers in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterManagerName, resourceGroupName, subscriptionId, data__properties" /> | Create a new cluster manager or update properties of the cluster manager if it exists. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterManagerName, resourceGroupName, subscriptionId" /> | Delete the provided cluster manager. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterManagerName, resourceGroupName, subscriptionId" /> | Patch properties of the provided cluster manager, or update the tags assigned to the cluster manager. Properties and tag updates can be done independently. |
