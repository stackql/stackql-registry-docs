---
title: host_reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - host_reservations
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.host_reservations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tagSet` | `array` | Any tags assigned to the Dedicated Host Reservation. |
| `hourlyPrice` | `string` | The hourly price of the reservation. |
| `currencyCode` | `string` | The currency in which the &lt;code&gt;upfrontPrice&lt;/code&gt; and &lt;code&gt;hourlyPrice&lt;/code&gt; amounts are specified. At this time, the only supported currency is &lt;code&gt;USD&lt;/code&gt;. |
| `start` | `string` | The date and time that the reservation started. |
| `hostReservationId` | `string` | The ID of the reservation that specifies the associated Dedicated Hosts. |
| `duration` | `integer` | The length of the reservation's term, specified in seconds. Can be &lt;code&gt;31536000 (1 year)&lt;/code&gt; \| &lt;code&gt;94608000 (3 years)&lt;/code&gt;. |
| `hostIdSet` | `array` | The IDs of the Dedicated Hosts associated with the reservation. |
| `end` | `string` | The date and time that the reservation ends. |
| `paymentOption` | `string` | The payment option selected for this reservation. |
| `offeringId` | `string` | The ID of the reservation. This remains the same regardless of which Dedicated Hosts are associated with it. |
| `state` | `string` | The state of the reservation. |
| `upfrontPrice` | `string` | The upfront price of the reservation. |
| `instanceFamily` | `string` | The instance family of the Dedicated Host Reservation. The instance family on the Dedicated Host must be the same in order for it to benefit from the reservation. |
| `count` | `integer` | The number of Dedicated Hosts the reservation is associated with. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `host_reservations_Describe` | `SELECT` | `region` | Describes reservations that are associated with Dedicated Hosts in your account. |
| `host_reservation_Purchase` | `EXEC` | `HostIdSet, OfferingId, region` | Purchase a reservation with configurations that match those of your Dedicated Host. You must have active Dedicated Hosts in your account before you purchase a reservation. This action results in the specified reservation being purchased and charged to your account. |
