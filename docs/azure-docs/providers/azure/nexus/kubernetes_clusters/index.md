---
title: kubernetes_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - kubernetes_clusters
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
<tr><td><b>Name</b></td><td><code>kubernetes_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.kubernetes_clusters" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="kubernetesClusterName, resourceGroupName, subscriptionId" /> | Get properties of the provided the Kubernetes cluster. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of Kubernetes clusters in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of Kubernetes clusters in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="kubernetesClusterName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new Kubernetes cluster or update the properties of the existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="kubernetesClusterName, resourceGroupName, subscriptionId" /> | Delete the provided Kubernetes cluster. |
| <CopyableCode code="restart_node" /> | `EXEC` | <CopyableCode code="kubernetesClusterName, resourceGroupName, subscriptionId, data__nodeName" /> | Restart a targeted node of a Kubernetes cluster. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="kubernetesClusterName, resourceGroupName, subscriptionId" /> | Patch the properties of the provided Kubernetes cluster, or update the tags associated with the Kubernetes cluster. Properties and tag updates can be done independently. |
