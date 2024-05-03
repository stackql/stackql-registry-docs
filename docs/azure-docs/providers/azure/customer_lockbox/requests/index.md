---
title: requests
hide_title: false
hide_table_of_contents: false
keywords:
  - requests
  - customer_lockbox
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
<tr><td><b>Name</b></td><td><code>requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.customer_lockbox.requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Arm resource id of the Lockbox request. |
| <CopyableCode code="name" /> | `string` | The name of the Lockbox request. |
| <CopyableCode code="properties" /> | `object` | The properties that are associated with a lockbox request. |
| <CopyableCode code="type" /> | `string` | The type of the Lockbox request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="requestId, subscriptionId" /> | Get Customer Lockbox request |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the Lockbox requests in the given subscription. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all of the Lockbox requests in the given subscription. |
