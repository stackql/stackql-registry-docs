---
title: host_reservation_purchase_preview
hide_title: false
hide_table_of_contents: false
keywords:
  - host_reservation_purchase_preview
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_reservation_purchase_preview</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.host_reservation_purchase_preview" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="currencyCode" /> | `string` | The currency in which the &lt;code&gt;totalUpfrontPrice&lt;/code&gt; and &lt;code&gt;totalHourlyPrice&lt;/code&gt; amounts are specified. At this time, the only supported currency is &lt;code&gt;USD&lt;/code&gt;. |
| <CopyableCode code="purchase" /> | `array` | The purchase information of the Dedicated Host reservation and the Dedicated Hosts associated with it. |
| <CopyableCode code="totalHourlyPrice" /> | `string` | The potential total hourly price of the reservation per hour. |
| <CopyableCode code="totalUpfrontPrice" /> | `string` | The potential total upfront price. This is billed immediately. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="host_reservation_purchase_preview_Get" /> | `SELECT` | <CopyableCode code="HostIdSet, OfferingId, region" /> |
