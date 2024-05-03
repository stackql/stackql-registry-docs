---
title: shoppers
hide_title: false
hide_table_of_contents: false
keywords:
  - shoppers
  - shoppers
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shoppers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="godaddy.shoppers.shoppers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="email" /> | `string` |
| <CopyableCode code="externalId" /> | `integer` |
| <CopyableCode code="marketId" /> | `string` |
| <CopyableCode code="nameFirst" /> | `string` |
| <CopyableCode code="nameLast" /> | `string` |
| <CopyableCode code="shopperId" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="shopper_id" /> | Get details for the specified Shopper |
| <CopyableCode code="create_subaccount" /> | `INSERT` | <CopyableCode code="data__email, data__nameFirst, data__nameLast, data__password" /> | Create a Subaccount owned by the authenticated Reseller |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="shopper_id" /> | Update details for the specified Shopper |
