---
title: subnet_cidr_reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_cidr_reservations
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
<tr><td><b>Name</b></td><td><code>subnet_cidr_reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.subnet_cidr_reservations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextToken" /> | `string` | The token to use to retrieve the next page of results. This value is &lt;code&gt;null&lt;/code&gt; when there are no more results to return. |
| <CopyableCode code="subnetIpv4CidrReservationSet" /> | `array` | Information about the IPv4 subnet CIDR reservations. |
| <CopyableCode code="subnetIpv6CidrReservationSet" /> | `array` | Information about the IPv6 subnet CIDR reservations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="subnet_cidr_reservations_Get" /> | `SELECT` | <CopyableCode code="SubnetId, region" /> | Gets information about the subnet CIDR reservations. |
| <CopyableCode code="subnet_cidr_reservation_Create" /> | `INSERT` | <CopyableCode code="Cidr, ReservationType, SubnetId, region" /> | Creates a subnet CIDR reservation. For information about subnet CIDR reservations, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html"&gt;Subnet CIDR reservations&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;. |
| <CopyableCode code="subnet_cidr_reservation_Delete" /> | `DELETE` | <CopyableCode code="SubnetCidrReservationId, region" /> | Deletes a subnet CIDR reservation. |
