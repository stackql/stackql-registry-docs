---
title: transfer
hide_title: false
hide_table_of_contents: false
keywords:
  - transfer
  - instances
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transfer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.instances.transfer" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="billable" /> | `integer` | The amount of network transfer this Linode has used, in GB, past your monthly quota.<br /> |
| <CopyableCode code="quota" /> | `integer` | The amount of network transfer this Linode adds to your transfer pool, in GB, for the current month's billing cycle.<br /> |
| <CopyableCode code="used" /> | `integer` | The amount of network transfer used by this Linode, in bytes, for the current month's billing cycle.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getLinodeTransfer" /> | `SELECT` | <CopyableCode code="linodeId" /> | Returns a Linode's network transfer pool statistics for the current month.<br /> |
| <CopyableCode code="getLinodeTransferByYearMonth" /> | `SELECT` | <CopyableCode code="linodeId, month, year" /> | Returns a Linode's network transfer statistics for a specific month. The year/month values must be either a date in the past, or the current month.<br /> |
| <CopyableCode code="_getLinodeTransfer" /> | `EXEC` | <CopyableCode code="linodeId" /> | Returns a Linode's network transfer pool statistics for the current month.<br /> |
| <CopyableCode code="_getLinodeTransferByYearMonth" /> | `EXEC` | <CopyableCode code="linodeId, month, year" /> | Returns a Linode's network transfer statistics for a specific month. The year/month values must be either a date in the past, or the current month.<br /> |
