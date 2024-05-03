---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - data_explorer
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Class representing the Kusto cluster properties. |
| <CopyableCode code="sku" /> | `object` | Azure SKU definition. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | An array represents the availability zones of the cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets a Kusto cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all Kusto clusters within a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Kusto clusters within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__sku" /> | Create or update a Kusto cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deletes a Kusto cluster. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all Kusto clusters within a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Kusto clusters within a resource group. |
| <CopyableCode code="add_language_extensions" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Add a list of language extensions that can run within KQL queries. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__type" /> | Checks that the cluster name is valid and is not already in use. |
| <CopyableCode code="detach_follower_databases" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__attachedDatabaseConfigurationName, data__clusterResourceId" /> | Detaches all followers of a database owned by this cluster. |
| <CopyableCode code="diagnose_virtual_network" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Diagnoses network connectivity status for external resources on which the service is dependent on. |
| <CopyableCode code="migrate" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__clusterResourceId" /> | Migrate data from a Kusto cluster to another cluster. |
| <CopyableCode code="remove_language_extensions" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Remove a list of language extensions that can run within KQL queries. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Starts a Kusto cluster. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Stops a Kusto cluster. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Update a Kusto cluster. |
