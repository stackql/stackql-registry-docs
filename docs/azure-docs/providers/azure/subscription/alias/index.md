---
title: alias
hide_title: false
hide_table_of_contents: false
keywords:
  - alias
  - subscription
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
<tr><td><b>Name</b></td><td><code>alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.subscription.alias" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ID for the alias resource. |
| <CopyableCode code="name" /> | `string` | Alias ID. |
| <CopyableCode code="properties" /> | `object` | Put subscription creation result properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type, Microsoft.Subscription/aliases. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="aliasName" /> | Get Alias Subscription. |
| <CopyableCode code="list" /> | `SELECT` |  | List Alias Subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="aliasName" /> | Create Alias Subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="aliasName" /> | Delete Alias. |
