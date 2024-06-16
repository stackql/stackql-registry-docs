---
title: data_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - data_stores
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
<tr><td><b>Name</b></td><td><code>data_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_data_manager.data_stores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the object. |
| <CopyableCode code="name" /> | `string` | Name of the object. |
| <CopyableCode code="properties" /> | `object` | Data Store for sources and sinks |
| <CopyableCode code="type" /> | `string` | Type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerName, dataStoreName, resourceGroupName, subscriptionId" /> | This method gets the data store/repository by name. |
| <CopyableCode code="list_by_data_manager" /> | `SELECT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | Gets all the data stores/repositories in the given resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataManagerName, dataStoreName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the data store/repository in the data manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataManagerName, dataStoreName, resourceGroupName, subscriptionId" /> | This method deletes the given data store/repository. |
