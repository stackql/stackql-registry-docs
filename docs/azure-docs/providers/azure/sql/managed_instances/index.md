---
title: managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instances
  - sql
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
<tr><td><b>Name</b></td><td><code>managed_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Azure Active Directory identity configuration for a resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The properties of a managed instance. |
| <CopyableCode code="sku" /> | `object` | An ARM Resource SKU. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all managed instances in the subscription. |
| <CopyableCode code="list_by_instance_pool" /> | `SELECT` | <CopyableCode code="instancePoolName, resourceGroupName, subscriptionId" /> | Gets a list of all managed instances in an instance pool. |
| <CopyableCode code="list_by_managed_instance" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Get top resource consuming queries of a managed instance. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of managed instances in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates a managed instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Deletes a managed instance. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets a list of all managed instances in the subscription. |
| <CopyableCode code="_list_by_instance_pool" /> | `EXEC` | <CopyableCode code="instancePoolName, resourceGroupName, subscriptionId" /> | Gets a list of all managed instances in an instance pool. |
| <CopyableCode code="_list_by_managed_instance" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Get top resource consuming queries of a managed instance. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of managed instances in a resource group. |
| <CopyableCode code="exec_get" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a managed instance. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Failovers a managed instance. |
| <CopyableCode code="refresh_status" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Refresh external governance enablement status. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Starts the managed instance. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Stops the managed instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Updates a managed instance. |
