---
title: spot_fleet_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - spot_fleet_requests
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
<tr><td><b>Name</b></td><td><code>spot_fleet_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.spot_fleet_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `activityStatus` | `string` | The progress of the Spot Fleet request. If there is an error, the status is &lt;code&gt;error&lt;/code&gt;. After all requests are placed, the status is &lt;code&gt;pending_fulfillment&lt;/code&gt;. If the size of the fleet is equal to or greater than its target capacity, the status is &lt;code&gt;fulfilled&lt;/code&gt;. If the size of the fleet is decreased, the status is &lt;code&gt;pending_termination&lt;/code&gt; while Spot Instances are terminating. |
| `createTime` | `string` | The creation date and time of the request. |
| `spotFleetRequestConfig` | `object` | Describes the configuration of a Spot Fleet request. |
| `spotFleetRequestId` | `string` | The ID of the Spot Fleet request. |
| `spotFleetRequestState` | `string` | The state of the Spot Fleet request. |
| `tagSet` | `array` | The tags for a Spot Fleet resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `spot_fleet_requests_Describe` | `SELECT` |  | &lt;p&gt;Describes your Spot Fleet requests.&lt;/p&gt; &lt;p&gt;Spot Fleet requests are deleted 48 hours after they are canceled and their instances are terminated.&lt;/p&gt; |
| `spot_fleet_request_Modify` | `EXEC` | `SpotFleetRequestId` | &lt;p&gt;Modifies the specified Spot Fleet request.&lt;/p&gt; &lt;p&gt;You can only modify a Spot Fleet request of type &lt;code&gt;maintain&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;While the Spot Fleet request is being modified, it is in the &lt;code&gt;modifying&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt;To scale up your Spot Fleet, increase its target capacity. The Spot Fleet launches the additional Spot Instances according to the allocation strategy for the Spot Fleet request. If the allocation strategy is &lt;code&gt;lowestPrice&lt;/code&gt;, the Spot Fleet launches instances using the Spot Instance pool with the lowest price. If the allocation strategy is &lt;code&gt;diversified&lt;/code&gt;, the Spot Fleet distributes the instances across the Spot Instance pools. If the allocation strategy is &lt;code&gt;capacityOptimized&lt;/code&gt;, Spot Fleet launches instances from Spot Instance pools with optimal capacity for the number of instances that are launching.&lt;/p&gt; &lt;p&gt;To scale down your Spot Fleet, decrease its target capacity. First, the Spot Fleet cancels any open requests that exceed the new target capacity. You can request that the Spot Fleet terminate Spot Instances until the size of the fleet no longer exceeds the new target capacity. If the allocation strategy is &lt;code&gt;lowestPrice&lt;/code&gt;, the Spot Fleet terminates the instances with the highest price per unit. If the allocation strategy is &lt;code&gt;capacityOptimized&lt;/code&gt;, the Spot Fleet terminates the instances in the Spot Instance pools that have the least available Spot Instance capacity. If the allocation strategy is &lt;code&gt;diversified&lt;/code&gt;, the Spot Fleet terminates instances across the Spot Instance pools. Alternatively, you can request that the Spot Fleet keep the fleet at its current size, but not replace any Spot Instances that are interrupted or that you terminate manually.&lt;/p&gt; &lt;p&gt;If you are finished with your Spot Fleet for now, but will use it again later, you can set the target capacity to 0.&lt;/p&gt; |
| `spot_fleet_requests_Cancel` | `EXEC` | `SpotFleetRequestId, TerminateInstances` | &lt;p&gt;Cancels the specified Spot Fleet requests.&lt;/p&gt; &lt;p&gt;After you cancel a Spot Fleet request, the Spot Fleet launches no new Spot Instances. You must specify whether the Spot Fleet should also terminate its Spot Instances. If you terminate the instances, the Spot Fleet request enters the &lt;code&gt;cancelled_terminating&lt;/code&gt; state. Otherwise, the Spot Fleet request enters the &lt;code&gt;cancelled_running&lt;/code&gt; state and the instances continue to run until they are interrupted or you terminate them manually.&lt;/p&gt; |
