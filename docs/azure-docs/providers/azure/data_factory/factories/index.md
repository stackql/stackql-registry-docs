---
title: factories
hide_title: false
hide_table_of_contents: false
keywords:
  - factories
  - data_factory
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
<tr><td><b>Name</b></td><td><code>factories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.factories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="eTag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="identity" /> | `object` | Identity properties of the factory resource. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | Factory resource properties. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Gets a factory. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Lists factories under the specified subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Lists factories. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Creates or updates a factory. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Deletes a factory. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | Lists factories under the specified subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Lists factories. |
| <CopyableCode code="configure_factory_repo" /> | `EXEC` | <CopyableCode code="api-version, locationId, subscriptionId" /> | Updates a factory's repo information. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Updates a factory. |
