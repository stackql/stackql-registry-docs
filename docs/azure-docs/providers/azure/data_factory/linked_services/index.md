---
title: linked_services
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_services
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
<tr><td><b>Name</b></td><td><code>linked_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.linked_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="properties" /> | `object` | The nested object which contains the information and credential which can be used to connect with related store or compute resource. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, factoryName, linkedServiceName, resourceGroupName, subscriptionId" /> | Gets a linked service. |
| <CopyableCode code="list_by_factory" /> | `SELECT` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Lists linked services. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, factoryName, linkedServiceName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a linked service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, factoryName, linkedServiceName, resourceGroupName, subscriptionId" /> | Deletes a linked service. |
