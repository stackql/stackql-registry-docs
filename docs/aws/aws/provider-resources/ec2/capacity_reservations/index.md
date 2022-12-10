---
title: capacity_reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservations
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
<tr><td><b>Name</b></td><td><code>capacity_reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.capacity_reservations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `instanceType` | `string` | The type of instance for which the Capacity Reservation reserves capacity. |
| `tagSet` | `array` | Any tags assigned to the Capacity Reservation. |
| `endDateType` | `string` | &lt;p&gt;Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;unlimited&lt;/code&gt; - The Capacity Reservation remains active until you explicitly cancel it.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;limited&lt;/code&gt; - The Capacity Reservation expires automatically at a specified date and time.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `createDate` | `string` | The date and time at which the Capacity Reservation was created. |
| `placementGroupArn` | `string` | The Amazon Resource Name (ARN) of the cluster placement group in which the Capacity Reservation was created. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-cpg.html"&gt; Capacity Reservations for cluster placement groups&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;. |
| `instancePlatform` | `string` | The type of operating system for which the Capacity Reservation reserves capacity. |
| `tenancy` | `string` | &lt;p&gt;Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;default&lt;/code&gt; - The Capacity Reservation is created on hardware that is shared with other Amazon Web Services accounts.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;dedicated&lt;/code&gt; - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `startDate` | `string` | The date and time at which the Capacity Reservation was started. |
| `availabilityZone` | `string` | The Availability Zone in which the capacity is reserved. |
| `endDate` | `string` | The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to &lt;code&gt;expired&lt;/code&gt; when it reaches its end date and time. |
| `capacityReservationArn` | `string` | The Amazon Resource Name (ARN) of the Capacity Reservation. |
| `capacityReservationId` | `string` | The ID of the Capacity Reservation. |
| `state` | `string` | &lt;p&gt;The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;active&lt;/code&gt; - The Capacity Reservation is active and the capacity is available for your use.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;expired&lt;/code&gt; - The Capacity Reservation expired automatically at the date and time specified in your request. The reserved capacity is no longer available for your use.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cancelled&lt;/code&gt; - The Capacity Reservation was cancelled. The reserved capacity is no longer available for your use.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;pending&lt;/code&gt; - The Capacity Reservation request was successful but the capacity provisioning is still pending.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;failed&lt;/code&gt; - The Capacity Reservation request has failed. A request might fail due to invalid request parameters, capacity constraints, or instance limit constraints. Failed requests are retained for 60 minutes.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `availableInstanceCount` | `integer` | The remaining capacity. Indicates the number of instances that can be launched in the Capacity Reservation. |
| `availabilityZoneId` | `string` | The Availability Zone ID of the Capacity Reservation. |
| `ephemeralStorage` | `boolean` | Indicates whether the Capacity Reservation supports instances with temporary, block-level storage. |
| `instanceMatchCriteria` | `string` | &lt;p&gt;Indicates the type of instance launches that the Capacity Reservation accepts. The options include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;open&lt;/code&gt; - The Capacity Reservation accepts all instances that have matching attributes (instance type, platform, and Availability Zone). Instances that have matching attributes launch into the Capacity Reservation automatically without specifying any additional parameters.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;targeted&lt;/code&gt; - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `outpostArn` | `string` | The Amazon Resource Name (ARN) of the Outpost on which the Capacity Reservation was created. |
| `capacityReservationFleetId` | `string` | The ID of the Capacity Reservation Fleet to which the Capacity Reservation belongs. Only valid for Capacity Reservations that were created by a Capacity Reservation Fleet. |
| `totalInstanceCount` | `integer` | The total number of instances for which the Capacity Reservation reserves capacity. |
| `ebsOptimized` | `boolean` | Indicates whether the Capacity Reservation supports EBS-optimized instances. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS- optimized instance. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the Capacity Reservation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `capacity_reservations_Describe` | `SELECT` |  | Describes one or more of your Capacity Reservations. The results describe only the Capacity Reservations in the Amazon Web Services Region that you're currently using. |
| `capacity_reservation_Create` | `INSERT` | `InstanceCount, InstancePlatform, InstanceType` | &lt;p&gt;Creates a new Capacity Reservation with the specified attributes.&lt;/p&gt; &lt;p&gt;Capacity Reservations enable you to reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration. This gives you the flexibility to selectively add capacity reservations and still get the Regional RI discounts for that usage. By creating Capacity Reservations, you ensure that you always have access to Amazon EC2 capacity when you need it, for as long as you need it. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html"&gt;Capacity Reservations&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Your request to create a Capacity Reservation could fail if Amazon EC2 does not have sufficient capacity to fulfill the request. If your request fails due to Amazon EC2 capacity constraints, either try again at a later time, try in a different Availability Zone, or request a smaller capacity reservation. If your application is flexible across instance types and sizes, try to create a Capacity Reservation with different instance attributes.&lt;/p&gt; &lt;p&gt;Your request could also fail if the requested quantity exceeds your On-Demand Instance limit for the selected instance type. If your request fails due to limit constraints, increase your On-Demand Instance limit for the required instance type and try again. For more information about increasing your instance limits, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html"&gt;Amazon EC2 Service Quotas&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| `capacity_reservation_Cancel` | `EXEC` | `CapacityReservationId` | &lt;p&gt;Cancels the specified Capacity Reservation, releases the reserved capacity, and changes the Capacity Reservation's state to &lt;code&gt;cancelled&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Instances running in the reserved capacity continue running until you stop them. Stopped instances that target the Capacity Reservation can no longer launch. Modify these instances to either target a different Capacity Reservation, launch On-Demand Instance capacity, or run in any open Capacity Reservation that has matching attributes and sufficient capacity.&lt;/p&gt; |
| `capacity_reservation_Modify` | `EXEC` | `CapacityReservationId` | Modifies a Capacity Reservation's capacity and the conditions under which it is to be released. You cannot change a Capacity Reservation's instance type, EBS optimization, instance store settings, platform, Availability Zone, or instance eligibility. If you need to modify any of these attributes, we recommend that you cancel the Capacity Reservation, and then create a new one with the required attributes. |
