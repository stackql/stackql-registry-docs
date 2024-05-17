---
title: host_reservation_offerings
hide_title: false
hide_table_of_contents: false
keywords:
  - host_reservation_offerings
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
<tr><td><b>Name</b></td><td><code>host_reservation_offerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.host_reservation_offerings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="currencyCode" /> | `string` | The currency of the offering. |
| <CopyableCode code="duration" /> | `integer` | The duration of the offering (in seconds). |
| <CopyableCode code="hourlyPrice" /> | `string` | The hourly price of the offering. |
| <CopyableCode code="instanceFamily" /> | `string` | The instance family of the offering. |
| <CopyableCode code="offeringId" /> | `string` | The ID of the offering. |
| <CopyableCode code="paymentOption" /> | `string` | The available payment option. |
| <CopyableCode code="upfrontPrice" /> | `string` | The upfront price of the offering. Does not apply to No Upfront offerings. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="host_reservation_offerings_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
