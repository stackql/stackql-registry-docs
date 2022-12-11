---
title: subnet_cidr_reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_cidr_reservations
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_cidr_reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.subnet_cidr_reservations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `subnetIpv4CidrReservationSet` | `array` | Information about the IPv4 subnet CIDR reservations. |
| `subnetIpv6CidrReservationSet` | `array` | Information about the IPv6 subnet CIDR reservations. |
| `nextToken` | `string` | The token to use to retrieve the next page of results. This value is &lt;code&gt;null&lt;/code&gt; when there are no more results to return. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `subnet_cidr_reservations_Get` | `SELECT` | `SubnetId` | Gets information about the subnet CIDR reservations. |
| `subnet_cidr_reservation_Create` | `INSERT` | `Cidr, ReservationType, SubnetId` | Creates a subnet CIDR reservation. For information about subnet CIDR reservations, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html"&gt;Subnet CIDR reservations&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;. |
| `subnet_cidr_reservation_Delete` | `DELETE` | `SubnetCidrReservationId` | Deletes a subnet CIDR reservation. |
