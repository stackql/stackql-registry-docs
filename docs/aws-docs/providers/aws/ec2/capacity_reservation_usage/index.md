---
title: capacity_reservation_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservation_usage
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
<tr><td><b>Name</b></td><td><code>capacity_reservation_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.capacity_reservation_usage</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `availableInstanceCount` | `integer` | The remaining capacity. Indicates the number of instances that can be launched in the Capacity Reservation. |
| `capacityReservationId` | `string` | The ID of the Capacity Reservation. |
| `instanceType` | `string` | The type of instance for which the Capacity Reservation reserves capacity. |
| `instanceUsageSet` | `array` | Information about the Capacity Reservation usage. |
| `nextToken` | `string` | The token to use to retrieve the next page of results. This value is &lt;code&gt;null&lt;/code&gt; when there are no more results to return. |
| `state` | `string` | &lt;p&gt;The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;active&lt;/code&gt; - The Capacity Reservation is active and the capacity is available for your use.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;expired&lt;/code&gt; - The Capacity Reservation expired automatically at the date and time specified in your request. The reserved capacity is no longer available for your use.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cancelled&lt;/code&gt; - The Capacity Reservation was cancelled. The reserved capacity is no longer available for your use.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;pending&lt;/code&gt; - The Capacity Reservation request was successful but the capacity provisioning is still pending.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;failed&lt;/code&gt; - The Capacity Reservation request has failed. A request might fail due to invalid request parameters, capacity constraints, or instance limit constraints. Failed requests are retained for 60 minutes.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `totalInstanceCount` | `integer` | The number of instances for which the Capacity Reservation reserves capacity. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `capacity_reservation_usage_Get` | `SELECT` | `CapacityReservationId` |
