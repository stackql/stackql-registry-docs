---
title: collection_offers_by_context
hide_title: false
hide_table_of_contents: false
keywords:
  - collection_offers_by_context
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
<tr><td><b>Name</b></td><td><code>collection_offers_by_context</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace.collection_offers_by_context" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextLink" /> | `string` | URL to get the next set of offer list per context results if there are any. |
| <CopyableCode code="value" /> | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_contexts" /> | `SELECT` | <CopyableCode code="collectionId, privateStoreId" /> |
