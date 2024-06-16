---
title: configuration_stores_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_stores_keys
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
<tr><td><b>Name</b></td><td><code>configuration_stores_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.configuration_stores_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The key ID. |
| <CopyableCode code="name" /> | `string` | A name for the key describing its usage. |
| <CopyableCode code="connectionString" /> | `string` | A connection string that can be used by supporting clients for authentication. |
| <CopyableCode code="lastModified" /> | `string` | The last time any of the key's properties were modified. |
| <CopyableCode code="readOnly" /> | `boolean` | Whether this key can only be used for read operations. |
| <CopyableCode code="value" /> | `string` | The value of the key that is used for authentication purposes. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> |
