---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
  - app_configuration
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.private_link_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a private link resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configStoreName, groupName, resourceGroupName, subscriptionId" /> | Gets a private link resource that need to be created for a configuration store. |
| <CopyableCode code="list_by_configuration_store" /> | `SELECT` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Gets the private link resources that need to be created for a configuration store. |
| <CopyableCode code="_list_by_configuration_store" /> | `EXEC` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Gets the private link resources that need to be created for a configuration store. |
