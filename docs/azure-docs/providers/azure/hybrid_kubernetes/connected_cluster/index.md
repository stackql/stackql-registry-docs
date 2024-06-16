---
title: connected_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_cluster
  - hybrid_kubernetes
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
<tr><td><b>Name</b></td><td><code>connected_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_kubernetes.connected_cluster" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the connected cluster. |
| <CopyableCode code="kind" /> | `string` | Indicates the kind of Arc connected cluster based on host infrastructure. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the connected cluster. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified connected cluster, including name, identity, properties, and additional cluster details. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | API to enumerate registered connected K8s clusters under a Resource Group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | API to enumerate registered connected K8s clusters under a Subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__identity, data__properties" /> | API to register a new Kubernetes cluster and create a tracked resource in Azure Resource Manager (ARM). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Delete a connected cluster, removing the tracked resource in Azure Resource Manager (ARM). |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | API to update certain properties of the connected cluster resource |
