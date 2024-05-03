---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
  - network
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
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Route resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, routeName, routeTableName, subscriptionId" /> | Gets the specified route from a route table. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, routeTableName, subscriptionId" /> | Gets all routes in a route table. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, routeName, routeTableName, subscriptionId" /> | Creates or updates a route in the specified route table. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, routeName, routeTableName, subscriptionId" /> | Deletes the specified route from a route table. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, routeTableName, subscriptionId" /> | Gets all routes in a route table. |
