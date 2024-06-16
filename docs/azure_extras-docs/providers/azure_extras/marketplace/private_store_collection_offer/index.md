---
title: private_store_collection_offer
hide_title: false
hide_table_of_contents: false
keywords:
  - private_store_collection_offer
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
<tr><td><b>Name</b></td><td><code>private_store_collection_offer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace.private_store_collection_offer" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Read only system data |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="collectionId, offerId, privateStoreId" /> | Gets information about a specific offer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="collectionId, privateStoreId" /> | Get a list of all private offers in the given private store and collection |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="collectionId, offerId, privateStoreId" /> | Update or add an offer to a specific collection of the private store. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="collectionId, offerId, privateStoreId" /> | Deletes an offer from the given collection of private store. |
| <CopyableCode code="post" /> | `EXEC` | <CopyableCode code="collectionId, offerId, privateStoreId" /> | Delete Private store offer. This is a workaround. |
| <CopyableCode code="upsert_offer_with_multi_context" /> | `EXEC` | <CopyableCode code="collectionId, offerId, privateStoreId" /> | Upsert an offer with multiple context details. |
