---
title: subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription
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
<tr><td><b>Name</b></td><td><code>subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.subscription.subscription" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="accept_ownership" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Accept subscription ownership. |
| <CopyableCode code="accept_ownership_status" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Accept subscription ownership status. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | The operation to cancel a subscription |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | The operation to enable a subscription |
| <CopyableCode code="rename" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | The operation to rename a subscription |
