---
title: marketplace_agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_agreements
  - marketplace_ordering
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
<tr><td><b>Name</b></td><td><code>marketplace_agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace_ordering.marketplace_agreements" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | Agreement Terms definition |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="offerId, offerType, planId, publisherId, subscriptionId" /> | Get marketplace terms. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List marketplace agreements in the subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="offerId, offerType, planId, publisherId, subscriptionId" /> | Save marketplace terms. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List marketplace agreements in the subscription. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="offerId, planId, publisherId, subscriptionId" /> | Cancel marketplace terms. |
| <CopyableCode code="sign" /> | `EXEC` | <CopyableCode code="offerId, planId, publisherId, subscriptionId" /> | Sign marketplace terms. |
