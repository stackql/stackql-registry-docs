---
title: marketplace_users_subs_stubbed
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_users_subs_stubbed
  - apps
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>marketplace_users_subs_stubbed</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.apps.marketplace_users_subs_stubbed" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account" /> | `object` |  |
| <CopyableCode code="billing_cycle" /> | `string` |  |
| <CopyableCode code="free_trial_ends_on" /> | `string` |  |
| <CopyableCode code="next_billing_date" /> | `string` |  |
| <CopyableCode code="on_free_trial" /> | `boolean` |  |
| <CopyableCode code="plan" /> | `object` | Marketplace Listing Plan |
| <CopyableCode code="unit_count" /> | `integer` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_subscriptions_for_authenticated_user_stubbed" /> | `SELECT` |  |
