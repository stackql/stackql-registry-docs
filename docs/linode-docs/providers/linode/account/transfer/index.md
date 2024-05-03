---
title: transfer
hide_title: false
hide_table_of_contents: false
keywords:
  - transfer
  - account
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
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.transfer" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="billable" /> | `integer` | The amount of your transfer pool that is billable this billing cycle.<br /> |
| <CopyableCode code="quota" /> | `integer` | The amount of network usage allowed this billing cycle.<br /> |
| <CopyableCode code="used" /> | `integer` | The amount of network usage you have used this billing cycle.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getTransfer" /> | `SELECT` |  |
| <CopyableCode code="_getTransfer" /> | `EXEC` |  |
