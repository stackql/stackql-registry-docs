---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.clusters" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get properties of the provided cluster. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of clusters in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of clusters in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new cluster or update the properties of the cluster if it exists. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Delete the provided cluster. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of clusters in the provided resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get a list of clusters in the provided subscription. |
| <CopyableCode code="deploy" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deploy the cluster using the rack configuration provided during creation. |
| <CopyableCode code="scan_runtime" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Triggers the execution of a runtime protection scan to detect and remediate detected issues, in accordance with the cluster configuration. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Patch the properties of the provided cluster, or update the tags associated with the cluster. Properties and tag updates can be done independently. |
