---
title: kusto_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pools
  - synapse
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
<tr><td><b>Name</b></td><td><code>kusto_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Class representing the Kusto pool properties. |
| <CopyableCode code="sku" /> | `object` | Azure SKU definition. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a Kusto pool. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List all Kusto pools |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__sku" /> | Create or update a Kusto pool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a Kusto pool. |
| <CopyableCode code="_list_by_workspace" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List all Kusto pools |
| <CopyableCode code="add_language_extensions" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Add a list of language extensions that can run within KQL queries. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__type" /> | Checks that the kusto pool name is valid and is not already in use. |
| <CopyableCode code="detach_follower_databases" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__attachedDatabaseConfigurationName, data__clusterResourceId" /> | Detaches all followers of a database owned by this Kusto Pool. |
| <CopyableCode code="remove_language_extensions" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Remove a list of language extensions that can run within KQL queries. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Starts a Kusto pool. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Stops a Kusto pool. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Update a Kusto Kusto Pool. |
