---
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
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
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.fleets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activityStatus" /> | `string` | The progress of the EC2 Fleet. If there is an error, the status is &lt;code&gt;error&lt;/code&gt;. After all requests are placed, the status is &lt;code&gt;pending_fulfillment&lt;/code&gt;. If the size of the EC2 Fleet is equal to or greater than its target capacity, the status is &lt;code&gt;fulfilled&lt;/code&gt;. If the size of the EC2 Fleet is decreased, the status is &lt;code&gt;pending_termination&lt;/code&gt; while instances are terminating. |
| <CopyableCode code="clientToken" /> | `string` | &lt;p&gt;Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html"&gt;Ensuring idempotency&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Constraints: Maximum 64 ASCII characters&lt;/p&gt; |
| <CopyableCode code="context" /> | `string` | Reserved. |
| <CopyableCode code="createTime" /> | `string` | The creation date and time of the EC2 Fleet. |
| <CopyableCode code="errorSet" /> | `array` | Information about the instances that could not be launched by the fleet. Valid only when &lt;b&gt;Type&lt;/b&gt; is set to &lt;code&gt;instant&lt;/code&gt;. |
| <CopyableCode code="excessCapacityTerminationPolicy" /> | `string` | Indicates whether running instances should be terminated if the target capacity of the EC2 Fleet is decreased below the current size of the EC2 Fleet. |
| <CopyableCode code="fleetId" /> | `string` | The ID of the EC2 Fleet. |
| <CopyableCode code="fleetInstanceSet" /> | `array` | Information about the instances that were launched by the fleet. Valid only when &lt;b&gt;Type&lt;/b&gt; is set to &lt;code&gt;instant&lt;/code&gt;. |
| <CopyableCode code="fleetState" /> | `string` | The state of the EC2 Fleet. |
| <CopyableCode code="fulfilledCapacity" /> | `number` | The number of units fulfilled by this request compared to the set target capacity. |
| <CopyableCode code="fulfilledOnDemandCapacity" /> | `number` | The number of units fulfilled by this request compared to the set target On-Demand capacity. |
| <CopyableCode code="launchTemplateConfigs" /> | `array` | The launch template and overrides. |
| <CopyableCode code="onDemandOptions" /> | `object` | Describes the configuration of On-Demand Instances in an EC2 Fleet. |
| <CopyableCode code="replaceUnhealthyInstances" /> | `boolean` | Indicates whether EC2 Fleet should replace unhealthy Spot Instances. Supported only for fleets of type &lt;code&gt;maintain&lt;/code&gt;. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html#ec2-fleet-health-checks"&gt;EC2 Fleet health checks&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;. |
| <CopyableCode code="spotOptions" /> | `object` | Describes the configuration of Spot Instances in an EC2 Fleet. |
| <CopyableCode code="tagSet" /> | `array` | The tags for an EC2 Fleet resource. |
| <CopyableCode code="targetCapacitySpecification" /> | `object` | &lt;p&gt;The number of units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is &lt;code&gt;maintain&lt;/code&gt;, you can specify a target capacity of 0 and add capacity later.&lt;/p&gt; &lt;p&gt;You can use the On-Demand Instance &lt;code&gt;MaxTotalPrice&lt;/code&gt; parameter, the Spot Instance &lt;code&gt;MaxTotalPrice&lt;/code&gt;, or both to ensure that your fleet cost does not exceed your budget. If you set a maximum price per hour for the On-Demand Instances and Spot Instances in your request, EC2 Fleet will launch instances until it reaches the maximum amount that you're willing to pay. When the maximum amount you're willing to pay is reached, the fleet stops launching instances even if it hasn’t met the target capacity. The &lt;code&gt;MaxTotalPrice&lt;/code&gt; parameters are located in &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_OnDemandOptions.html"&gt;OnDemandOptions&lt;/a&gt; and &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotOptions"&gt;SpotOptions&lt;/a&gt;.&lt;/p&gt; |
| <CopyableCode code="terminateInstancesWithExpiration" /> | `boolean` | Indicates whether running instances should be terminated when the EC2 Fleet expires.  |
| <CopyableCode code="type" /> | `string` | The type of request. Indicates whether the EC2 Fleet only &lt;code&gt;requests&lt;/code&gt; the target capacity, or also attempts to &lt;code&gt;maintain&lt;/code&gt; it. If you request a certain target capacity, EC2 Fleet only places the required requests; it does not attempt to replenish instances if capacity is diminished, and it does not submit requests in alternative capacity pools if capacity is unavailable. To maintain a certain target capacity, EC2 Fleet places the required requests to meet this target capacity. It also automatically replenishes any interrupted Spot Instances. Default: &lt;code&gt;maintain&lt;/code&gt;. |
| <CopyableCode code="validFrom" /> | `string` | The start date and time of the request, in UTC format (for example, &lt;i&gt;YYYY&lt;/i&gt;-&lt;i&gt;MM&lt;/i&gt;-&lt;i&gt;DD&lt;/i&gt;T&lt;i&gt;HH&lt;/i&gt;:&lt;i&gt;MM&lt;/i&gt;:&lt;i&gt;SS&lt;/i&gt;Z). The default is to start fulfilling the request immediately.  |
| <CopyableCode code="validUntil" /> | `string` | The end date and time of the request, in UTC format (for example, &lt;i&gt;YYYY&lt;/i&gt;-&lt;i&gt;MM&lt;/i&gt;-&lt;i&gt;DD&lt;/i&gt;T&lt;i&gt;HH&lt;/i&gt;:&lt;i&gt;MM&lt;/i&gt;:&lt;i&gt;SS&lt;/i&gt;Z). At this point, no new instance requests are placed or able to fulfill the request. The default end date is 7 days from the current date.  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fleets_Describe" /> | `SELECT` | <CopyableCode code="region" /> | &lt;p&gt;Describes the specified EC2 Fleets or all of your EC2 Fleets.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html#monitor-ec2-fleet"&gt;Monitor your EC2 Fleet&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="fleet_Create" /> | `INSERT` | <CopyableCode code="LaunchTemplateConfigs, TargetCapacitySpecification, region" /> | &lt;p&gt;Launches an EC2 Fleet.&lt;/p&gt; &lt;p&gt;You can create a single EC2 Fleet that includes multiple launch specifications that vary by instance type, AMI, Availability Zone, or subnet.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html"&gt;EC2 Fleet&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="fleets_Delete" /> | `DELETE` | <CopyableCode code="FleetId, TerminateInstances, region" /> | &lt;p&gt;Deletes the specified EC2 Fleet.&lt;/p&gt; &lt;p&gt;After you delete an EC2 Fleet, it launches no new instances.&lt;/p&gt; &lt;p&gt;You must specify whether a deleted EC2 Fleet should also terminate its instances. If you choose to terminate the instances, the EC2 Fleet enters the &lt;code&gt;deleted_terminating&lt;/code&gt; state. Otherwise, the EC2 Fleet enters the &lt;code&gt;deleted_running&lt;/code&gt; state, and the instances continue to run until they are interrupted or you terminate them manually.&lt;/p&gt; &lt;p&gt;For &lt;code&gt;instant&lt;/code&gt; fleets, EC2 Fleet must terminate the instances when the fleet is deleted. A deleted &lt;code&gt;instant&lt;/code&gt; fleet with running instances is not supported.&lt;/p&gt; &lt;p class="title"&gt; &lt;b&gt;Restrictions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can delete up to 25 &lt;code&gt;instant&lt;/code&gt; fleets in a single request. If you exceed this number, no &lt;code&gt;instant&lt;/code&gt; fleets are deleted and an error is returned. There is no restriction on the number of fleets of type &lt;code&gt;maintain&lt;/code&gt; or &lt;code&gt;request&lt;/code&gt; that can be deleted in a single request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Up to 1000 instances can be terminated in a single request to delete &lt;code&gt;instant&lt;/code&gt; fleets.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html#delete-fleet"&gt;Delete an EC2 Fleet&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="fleet_Modify" /> | `EXEC` | <CopyableCode code="FleetId, region" /> | &lt;p&gt;Modifies the specified EC2 Fleet.&lt;/p&gt; &lt;p&gt;You can only modify an EC2 Fleet request of type &lt;code&gt;maintain&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;While the EC2 Fleet is being modified, it is in the &lt;code&gt;modifying&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt;To scale up your EC2 Fleet, increase its target capacity. The EC2 Fleet launches the additional Spot Instances according to the allocation strategy for the EC2 Fleet request. If the allocation strategy is &lt;code&gt;lowest-price&lt;/code&gt;, the EC2 Fleet launches instances using the Spot Instance pool with the lowest price. If the allocation strategy is &lt;code&gt;diversified&lt;/code&gt;, the EC2 Fleet distributes the instances across the Spot Instance pools. If the allocation strategy is &lt;code&gt;capacity-optimized&lt;/code&gt;, EC2 Fleet launches instances from Spot Instance pools with optimal capacity for the number of instances that are launching.&lt;/p&gt; &lt;p&gt;To scale down your EC2 Fleet, decrease its target capacity. First, the EC2 Fleet cancels any open requests that exceed the new target capacity. You can request that the EC2 Fleet terminate Spot Instances until the size of the fleet no longer exceeds the new target capacity. If the allocation strategy is &lt;code&gt;lowest-price&lt;/code&gt;, the EC2 Fleet terminates the instances with the highest price per unit. If the allocation strategy is &lt;code&gt;capacity-optimized&lt;/code&gt;, the EC2 Fleet terminates the instances in the Spot Instance pools that have the least available Spot Instance capacity. If the allocation strategy is &lt;code&gt;diversified&lt;/code&gt;, the EC2 Fleet terminates instances across the Spot Instance pools. Alternatively, you can request that the EC2 Fleet keep the fleet at its current size, but not replace any Spot Instances that are interrupted or that you terminate manually.&lt;/p&gt; &lt;p&gt;If you are finished with your EC2 Fleet for now, but will use it again later, you can set the target capacity to 0.&lt;/p&gt; |
