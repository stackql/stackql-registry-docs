---
title: capacity_reservation_fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservation_fleets
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
<tr><td><b>Name</b></td><td><code>capacity_reservation_fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.capacity_reservation_fleets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `totalFulfilledCapacity` | `number` | The capacity units that have been fulfilled. |
| `createTime` | `string` | The date and time at which the Capacity Reservation Fleet was created. |
| `instanceTypeSpecificationSet` | `array` | Information about the instance types for which to reserve the capacity. |
| `instanceMatchCriteria` | `string` | &lt;p&gt;Indicates the type of instance launches that the Capacity Reservation Fleet accepts. All Capacity Reservations in the Fleet inherit this instance matching criteria.&lt;/p&gt; &lt;p&gt;Currently, Capacity Reservation Fleets support &lt;code&gt;open&lt;/code&gt; instance matching criteria only. This means that instances that have matching attributes (instance type, platform, and Availability Zone) run in the Capacity Reservations automatically. Instances do not need to explicitly target a Capacity Reservation Fleet to use its reserved capacity.&lt;/p&gt; |
| `capacityReservationFleetArn` | `string` | The ARN of the Capacity Reservation Fleet. |
| `allocationStrategy` | `string` | The strategy used by the Capacity Reservation Fleet to determine which of the specified instance types to use. For more information, see For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#allocation-strategy"&gt; Allocation strategy&lt;/a&gt; in the Amazon EC2 User Guide. |
| `totalTargetCapacity` | `integer` | The total number of capacity units for which the Capacity Reservation Fleet reserves capacity. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity"&gt;Total target capacity&lt;/a&gt; in the Amazon EC2 User Guide. |
| `tagSet` | `array` | The tags assigned to the Capacity Reservation Fleet. |
| `capacityReservationFleetId` | `string` | The ID of the Capacity Reservation Fleet. |
| `endDate` | `string` | The date and time at which the Capacity Reservation Fleet expires. |
| `state` | `string` | &lt;p&gt;The state of the Capacity Reservation Fleet. Possible states include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;submitted&lt;/code&gt; - The Capacity Reservation Fleet request has been submitted and Amazon Elastic Compute Cloud is preparing to create the Capacity Reservations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;modifying&lt;/code&gt; - The Capacity Reservation Fleet is being modified. The Fleet remains in this state until the modification is complete.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;active&lt;/code&gt; - The Capacity Reservation Fleet has fulfilled its total target capacity and it is attempting to maintain this capacity. The Fleet remains in this state until it is modified or deleted.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;partially_fulfilled&lt;/code&gt; - The Capacity Reservation Fleet has partially fulfilled its total target capacity. There is insufficient Amazon EC2 to fulfill the total target capacity. The Fleet is attempting to asynchronously fulfill its total target capacity.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;expiring&lt;/code&gt; - The Capacity Reservation Fleet has reach its end date and it is in the process of expiring. One or more of its Capacity reservations might still be active.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;expired&lt;/code&gt; - The Capacity Reservation Fleet has reach its end date. The Fleet and its Capacity Reservations are expired. The Fleet can't create new Capacity Reservations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cancelling&lt;/code&gt; - The Capacity Reservation Fleet is in the process of being cancelled. One or more of its Capacity reservations might still be active.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;cancelled&lt;/code&gt; - The Capacity Reservation Fleet has been manually cancelled. The Fleet and its Capacity Reservations are cancelled and the Fleet can't create new Capacity Reservations.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;failed&lt;/code&gt; - The Capacity Reservation Fleet failed to reserve capacity for the specified instance types.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `tenancy` | `string` | &lt;p&gt;The tenancy of the Capacity Reservation Fleet. Tenancies include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;default&lt;/code&gt; - The Capacity Reservation Fleet is created on hardware that is shared with other Amazon Web Services accounts.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;dedicated&lt;/code&gt; - The Capacity Reservation Fleet is created on single-tenant hardware that is dedicated to a single Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `capacity_reservation_fleets_Describe` | `SELECT` |  | Describes one or more Capacity Reservation Fleets. |
| `capacity_reservation_fleet_Create` | `INSERT` | `InstanceTypeSpecification, TotalTargetCapacity` | Creates a Capacity Reservation Fleet. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-cr-fleets.html#create-crfleet"&gt;Create a Capacity Reservation Fleet&lt;/a&gt; in the Amazon EC2 User Guide. |
| `capacity_reservation_fleet_Modify` | `EXEC` | `CapacityReservationFleetId` | &lt;p&gt;Modifies a Capacity Reservation Fleet.&lt;/p&gt; &lt;p&gt;When you modify the total target capacity of a Capacity Reservation Fleet, the Fleet automatically creates new Capacity Reservations, or modifies or cancels existing Capacity Reservations in the Fleet to meet the new total target capacity. When you modify the end date for the Fleet, the end dates for all of the individual Capacity Reservations in the Fleet are updated accordingly.&lt;/p&gt; |
| `capacity_reservation_fleets_Cancel` | `EXEC` | `CapacityReservationFleetId` | &lt;p&gt;Cancels one or more Capacity Reservation Fleets. When you cancel a Capacity Reservation Fleet, the following happens:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The Capacity Reservation Fleet's status changes to &lt;code&gt;cancelled&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The individual Capacity Reservations in the Fleet are cancelled. Instances running in the Capacity Reservations at the time of cancelling the Fleet continue to run in shared capacity.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Fleet stops creating new Capacity Reservations.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
