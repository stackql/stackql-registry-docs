---
title: private_store_collection
hide_title: false
hide_table_of_contents: false
keywords:
  - private_store_collection
  - marketplace
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>private_store_collection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace.private_store_collection" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | The collection details |
| <CopyableCode code="systemData" /> | `object` | Read only system data |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="collectionId, privateStoreId" /> | Gets private store collection |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateStoreId" /> | Gets private store collections list |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="collectionId, privateStoreId" /> | Create or update private store collection |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="collectionId, privateStoreId" /> | Delete a collection from the given private store. |
| <CopyableCode code="approve_all_items" /> | `EXEC` | <CopyableCode code="collectionId, privateStoreId" /> | Delete all existing offers from the collection and enable approve all items. |
| <CopyableCode code="disable_approve_all_items" /> | `EXEC` | <CopyableCode code="collectionId, privateStoreId" /> | Disable approve all items for the collection. |
| <CopyableCode code="post" /> | `EXEC` | <CopyableCode code="collectionId, privateStoreId" /> | Delete Private store collection. This is a workaround. |
| <CopyableCode code="transfer_offers" /> | `EXEC` | <CopyableCode code="collectionId, privateStoreId" /> | transferring offers (copy or move) from source collection to target collection(s) |
