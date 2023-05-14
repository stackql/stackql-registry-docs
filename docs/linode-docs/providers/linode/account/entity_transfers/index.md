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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entity_transfers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.account.entity_transfers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `token` | `string` | The token used to identify and accept or cancel this transfer.<br /> |
| `updated` | `string` | When this transfer was last updated.<br /> |
| `created` | `string` | When this transfer was created.<br /> |
| `entities` | `object` | A collection of the entities to include in this transfer request, separated by type.<br /> |
| `expiry` | `string` | When this transfer expires. Transfers will automatically expire 24 hours after creation.<br /> |
| `is_sender` | `boolean` | If the requesting account created this transfer.<br /> |
| `status` | `string` | The status of the transfer request.<br /><br />`accepted`: The transfer has been accepted by another user and is currently in progress. Transfers can take up to 3 hours to complete.<br /><br />`cancelled`: The transfer has been cancelled by the sender.<br /><br />`completed`: The transfer has completed successfully.<br /><br />`failed`: The transfer has failed after initiation.<br /><br />`pending`: The transfer is ready to be accepted.<br /><br />`stale`: The transfer has exceeded its expiration date. It can no longer be accepted or cancelled.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getEntityTransfer` | `SELECT` | `token` | **DEPRECATED**. Please use [Service Transfer View](/docs/api/account/#service-transfer-view).<br /> |
| `getEntityTransfers` | `SELECT` |  | **DEPRECATED**. Please use [Service Transfers List](/docs/api/account/#service-transfers-list).<br /> |
| `createEntityTransfer` | `INSERT` | `data__entities` | **DEPRECATED**. Please use [Service Transfer Create](/docs/api/account/#service-transfer-create).<br /> |
| `deleteEntityTransfer` | `DELETE` | `token` | **DEPRECATED**. Please use [Service Transfer Cancel](/docs/api/account/#service-transfer-cancel).<br /> |
| `_getEntityTransfer` | `EXEC` | `token` | **DEPRECATED**. Please use [Service Transfer View](/docs/api/account/#service-transfer-view).<br /> |
| `_getEntityTransfers` | `EXEC` |  | **DEPRECATED**. Please use [Service Transfers List](/docs/api/account/#service-transfers-list).<br /> |
| `acceptEntityTransfer` | `EXEC` | `token` | **DEPRECATED**. Please use [Service Transfer Accept](/docs/api/account/#service-transfer-accept).<br /> |
