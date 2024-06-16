---
title: data_managers
hide_title: false
hide_table_of_contents: false
keywords:
  - data_managers
  - hybrid_data_manager
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
<tr><td><b>Name</b></td><td><code>data_managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_data_manager.data_managers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Resource Id. |
| <CopyableCode code="name" /> | `string` | The Resource Name. |
| <CopyableCode code="etag" /> | `string` | Etag of the Resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. This will be one of the supported and registered Azure Geo Regions (e.g. West US, East<br />US, Southeast Asia, etc.). The geo region of a resource cannot be changed once it is created, but if an identical geo<br />region is specified on update the request will succeed. |
| <CopyableCode code="sku" /> | `object` | The sku type. |
| <CopyableCode code="tags" /> | `object` | The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource<br />(across resource groups). |
| <CopyableCode code="type" /> | `string` | The Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | Gets information about the specified data manager resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the data manager resources available under the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the data manager resources available under the given resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | Creates a new data manager resource with the specified parameters. Existing resources cannot be updated with this API<br />and should instead be updated with the Update data manager resource API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | Deletes a data manager resource in Microsoft Azure. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | Updates the properties of an existing data manager resource. |
