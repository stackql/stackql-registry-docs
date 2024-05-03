---
title: available_service_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - available_service_aliases
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
<tr><td><b>Name</b></td><td><code>available_service_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.available_service_aliases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the service alias. |
| <CopyableCode code="name" /> | `string` | The name of the service alias. |
| <CopyableCode code="resourceName" /> | `string` | The resource name of the service alias. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets all available service aliases for this subscription in this region. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Gets all available service aliases for this resource group in this region. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Gets all available service aliases for this subscription in this region. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Gets all available service aliases for this resource group in this region. |
