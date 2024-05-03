---
title: status
hide_title: false
hide_table_of_contents: false
keywords:
  - status
  - account
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.account.status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountActivated" /> | `boolean` | If the account is activated or not |
| <CopyableCode code="applicationUse" /> | `string` | The current usage of the application. |
| <CopyableCode code="canUpdatePlan" /> | `boolean` | If the plan can be updated by the given user |
| <CopyableCode code="planExpirationDays" /> | `integer` | The number of days in which the plan will expire |
| <CopyableCode code="planType" /> | `string` | Whether the account is `Free`/`Trial`/`Paid` |
| <CopyableCode code="pricingModel" /> | `string` | Whether the account is `cloudflex` or `credits` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getStatus" /> | `SELECT` | <CopyableCode code="region" /> |
