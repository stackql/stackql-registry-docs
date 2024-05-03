---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
  - iot_hub
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
<tr><td><b>Name</b></td><td><code>private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.private_link_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | The properties for a group information object |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, groupId, resourceGroupName, resourceName, subscriptionId" /> | Get the specified private link resource for the given IotHub |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | List private link resources for the given IotHub |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | List private link resources for the given IotHub |
