---
title: public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - public_keys
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
<tr><td><b>Name</b></td><td><code>public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_data_manager.public_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the object. |
| <CopyableCode code="name" /> | `string` | Name of the object. |
| <CopyableCode code="properties" /> | `object` | PublicKey Properties |
| <CopyableCode code="type" /> | `string` | Type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerName, publicKeyName, resourceGroupName, subscriptionId" /> | This method gets the public keys. |
| <CopyableCode code="list_by_data_manager" /> | `SELECT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | This method gets the list view of public keys, however it will only have one element. |
