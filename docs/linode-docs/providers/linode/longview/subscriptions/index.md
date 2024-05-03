---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - longview
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
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.longview.subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique ID of this Subscription tier.<br /> |
| <CopyableCode code="clients_included" /> | `integer` | The number of Longview Clients that may be created with this Subscription tier.<br /> |
| <CopyableCode code="label" /> | `string` | A display name for this Subscription tier.<br /> |
| <CopyableCode code="price" /> | `object` | Pricing information about this Subscription tier.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getLongviewSubscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the Longview plan details as a single `LongviewSubscription` object for the provided subscription ID. This is a public endpoint and requires no authentication.<br /> |
| <CopyableCode code="getLongviewSubscriptions" /> | `SELECT` |  | Returns a paginated list of available Longview Subscriptions. This is a public endpoint and requires no authentication.<br /> |
| <CopyableCode code="_getLongviewSubscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get the Longview plan details as a single `LongviewSubscription` object for the provided subscription ID. This is a public endpoint and requires no authentication.<br /> |
| <CopyableCode code="_getLongviewSubscriptions" /> | `EXEC` |  | Returns a paginated list of available Longview Subscriptions. This is a public endpoint and requires no authentication.<br /> |
