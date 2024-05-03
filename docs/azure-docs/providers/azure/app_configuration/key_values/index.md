---
title: key_values
hide_title: false
hide_table_of_contents: false
keywords:
  - key_values
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
<tr><td><b>Name</b></td><td><code>key_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.key_values" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | All key-value properties. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configStoreName, keyValueName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified key-value. NOTE: This operation is intended for use in ARM Template deployments. For all other scenarios involving App Configuration key-values the data plane API should be used instead. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configStoreName, keyValueName, resourceGroupName, subscriptionId" /> | Creates a key-value. NOTE: This operation is intended for use in ARM Template deployments. For all other scenarios involving App Configuration key-values the data plane API should be used instead. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configStoreName, keyValueName, resourceGroupName, subscriptionId" /> | Deletes a key-value. NOTE: This operation is intended for use in ARM Template deployments. For all other scenarios involving App Configuration key-values the data plane API should be used instead. |
