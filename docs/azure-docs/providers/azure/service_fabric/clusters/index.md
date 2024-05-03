---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - service_fabric
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource identifier. |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="etag" /> | `string` | Azure resource etag. |
| <CopyableCode code="location" /> | `string` | Azure resource location. |
| <CopyableCode code="properties" /> | `object` | Describes the cluster resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Azure resource tags. |
| <CopyableCode code="type" /> | `string` | Azure resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, clusterName, resourceGroupName, subscriptionId" /> | Get a Service Fabric cluster resource created or in the process of being created in the specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Gets all Service Fabric cluster resources created or in the process of being created in the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Gets all Service Fabric cluster resources created or in the process of being created in the resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, clusterName, resourceGroupName, subscriptionId" /> | Create or update a Service Fabric cluster resource with the specified name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, clusterName, resourceGroupName, subscriptionId" /> | Delete a Service Fabric cluster resource with the specified name. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | Gets all Service Fabric cluster resources created or in the process of being created in the subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Gets all Service Fabric cluster resources created or in the process of being created in the resource group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, clusterName, resourceGroupName, subscriptionId" /> | Update the configuration of a Service Fabric cluster resource with the specified name. |
