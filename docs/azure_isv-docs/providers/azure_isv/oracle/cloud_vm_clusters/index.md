---
title: cloud_vm_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_vm_clusters
  - oracle
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>cloud_vm_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.cloud_vm_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | CloudVmCluster resource model |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId" /> | Get a CloudVmCluster |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List CloudVmCluster resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List CloudVmCluster resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId" /> | Create a CloudVmCluster |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId" /> | Delete a CloudVmCluster |
| <CopyableCode code="add_vms" /> | `EXEC` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId, data__dbServers" /> | Add VMs to the VM Cluster |
| <CopyableCode code="remove_vms" /> | `EXEC` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId, data__dbServers" /> | Remove VMs from the VM Cluster |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId" /> | Update a CloudVmCluster |
