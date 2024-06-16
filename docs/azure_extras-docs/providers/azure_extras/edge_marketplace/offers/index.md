---
title: offers
hide_title: false
hide_table_of_contents: false
keywords:
  - offers
  - edge_marketplace
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
<tr><td><b>Name</b></td><td><code>offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edge_marketplace.offers" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="offerId, resourceUri" /> | Get a Offer |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List Offer resources by parent |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Offer resources by subscription |
| <CopyableCode code="generate_access_token" /> | `EXEC` | <CopyableCode code="offerId, resourceUri, data__edgeMarketPlaceRegion" /> | A long-running resource action. |
