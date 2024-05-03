---
title: entity_transfers
hide_title: false
hide_table_of_contents: false
keywords:
  - entity_transfers
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
<tr><td><b>Name</b></td><td><code>entity_transfers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.entity_transfers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created" /> | `string` | When this transfer was created.<br /> |
| <CopyableCode code="entities" /> | `object` | A collection of the entities to include in this transfer request, separated by type.<br /> |
| <CopyableCode code="expiry" /> | `string` | When this transfer expires. Transfers will automatically expire 24 hours after creation.<br /> |
| <CopyableCode code="is_sender" /> | `boolean` | If the requesting account created this transfer.<br /> |
| <CopyableCode code="status" /> | `string` | The status of the transfer request.<br /><br />`accepted`: The transfer has been accepted by another user and is currently in progress. Transfers can take up to 3 hours to complete.<br /><br />`cancelled`: The transfer has been cancelled by the sender.<br /><br />`completed`: The transfer has completed successfully.<br /><br />`failed`: The transfer has failed after initiation.<br /><br />`pending`: The transfer is ready to be accepted.<br /><br />`stale`: The transfer has exceeded its expiration date. It can no longer be accepted or cancelled.<br /> |
| <CopyableCode code="token" /> | `string` | The token used to identify and accept or cancel this transfer.<br /> |
| <CopyableCode code="updated" /> | `string` | When this transfer was last updated.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getEntityTransfer" /> | `SELECT` | <CopyableCode code="token" /> | **DEPRECATED**. Please use [Service Transfer View](/docs/api/account/#service-transfer-view).<br /> |
| <CopyableCode code="getEntityTransfers" /> | `SELECT` |  | **DEPRECATED**. Please use [Service Transfers List](/docs/api/account/#service-transfers-list).<br /> |
| <CopyableCode code="createEntityTransfer" /> | `INSERT` | <CopyableCode code="data__entities" /> | **DEPRECATED**. Please use [Service Transfer Create](/docs/api/account/#service-transfer-create).<br /> |
| <CopyableCode code="deleteEntityTransfer" /> | `DELETE` | <CopyableCode code="token" /> | **DEPRECATED**. Please use [Service Transfer Cancel](/docs/api/account/#service-transfer-cancel).<br /> |
| <CopyableCode code="_getEntityTransfer" /> | `EXEC` | <CopyableCode code="token" /> | **DEPRECATED**. Please use [Service Transfer View](/docs/api/account/#service-transfer-view).<br /> |
| <CopyableCode code="_getEntityTransfers" /> | `EXEC` |  | **DEPRECATED**. Please use [Service Transfers List](/docs/api/account/#service-transfers-list).<br /> |
| <CopyableCode code="acceptEntityTransfer" /> | `EXEC` | <CopyableCode code="token" /> | **DEPRECATED**. Please use [Service Transfer Accept](/docs/api/account/#service-transfer-accept).<br /> |
