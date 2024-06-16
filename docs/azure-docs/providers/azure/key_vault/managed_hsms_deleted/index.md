---
title: managed_hsms_deleted
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_hsms_deleted
  - key_vault
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
<tr><td><b>Name</b></td><td><code>managed_hsms_deleted</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.managed_hsms_deleted" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Azure Resource Manager resource ID for the deleted managed HSM Pool. |
| <CopyableCode code="name" /> | `string` | The name of the managed HSM Pool. |
| <CopyableCode code="properties" /> | `object` | Properties of the deleted managed HSM. |
| <CopyableCode code="type" /> | `string` | The resource type of the managed HSM Pool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, name, subscriptionId" /> | Gets the specified deleted managed HSM. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The List operation gets information about the deleted managed HSMs associated with the subscription. |
