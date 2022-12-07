---
title: spot_instance_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - spot_instance_requests
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
<tr><td><b>Name</b></td><td><code>spot_instance_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.spot_instance_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `validFrom` | `string` | The start date of the request, in UTC format (for example, &lt;i&gt;YYYY&lt;/i&gt;-&lt;i&gt;MM&lt;/i&gt;-&lt;i&gt;DD&lt;/i&gt;T&lt;i&gt;HH&lt;/i&gt;:&lt;i&gt;MM&lt;/i&gt;:&lt;i&gt;SS&lt;/i&gt;Z). The request becomes active at this date and time. |
| `launchSpecification` | `object` | Describes the launch specification for an instance. |
| `status` | `object` | Describes the status of a Spot Instance request. |
| `availabilityZoneGroup` | `string` | The Availability Zone group. If you specify the same Availability Zone group for all Spot Instance requests, all Spot Instances are launched in the same Availability Zone. |
| `launchGroup` | `string` | The instance launch group. Launch groups are Spot Instances that launch together and terminate together. |
| `instanceInterruptionBehavior` | `string` | The behavior when a Spot Instance is interrupted. |
| `spotPrice` | `string` | The maximum price per hour that you are willing to pay for a Spot Instance. |
| `instanceId` | `string` | The instance ID, if an instance has been launched to fulfill the Spot Instance request. |
| `blockDurationMinutes` | `integer` | Deprecated. |
| `validUntil` | `string` | &lt;p&gt;The end date of the request, in UTC format (&lt;i&gt;YYYY&lt;/i&gt;-&lt;i&gt;MM&lt;/i&gt;-&lt;i&gt;DD&lt;/i&gt;T&lt;i&gt;HH&lt;/i&gt;:&lt;i&gt;MM&lt;/i&gt;:&lt;i&gt;SS&lt;/i&gt;Z).&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For a persistent request, the request remains active until the &lt;code&gt;validUntil&lt;/code&gt; date and time is reached. Otherwise, the request remains active until you cancel it. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For a one-time request, the request remains active until all instances launch, the request is canceled, or the &lt;code&gt;validUntil&lt;/code&gt; date and time is reached. By default, the request is valid for 7 days from the date the request was created.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `state` | `string` | The state of the Spot Instance request. Spot request status information helps track your Spot Instance requests. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-status.html"&gt;Spot request status&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide for Linux Instances&lt;/i&gt;. |
| `fault` | `object` | Describes a Spot Instance state change. |
| `type` | `string` | The Spot Instance request type. |
| `spotInstanceRequestId` | `string` | The ID of the Spot Instance request. |
| `tagSet` | `array` | Any tags assigned to the resource. |
| `productDescription` | `string` | The product description associated with the Spot Instance. |
| `createTime` | `string` | The date and time when the Spot Instance request was created, in UTC format (for example, &lt;i&gt;YYYY&lt;/i&gt;-&lt;i&gt;MM&lt;/i&gt;-&lt;i&gt;DD&lt;/i&gt;T&lt;i&gt;HH&lt;/i&gt;:&lt;i&gt;MM&lt;/i&gt;:&lt;i&gt;SS&lt;/i&gt;Z). |
| `launchedAvailabilityZone` | `string` | The Availability Zone in which the request is launched. |
| `actualBlockHourlyPrice` | `string` | Deprecated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `spot_instance_requests_Describe` | `SELECT` |  | &lt;p&gt;Describes the specified Spot Instance requests.&lt;/p&gt; &lt;p&gt;You can use &lt;code&gt;DescribeSpotInstanceRequests&lt;/code&gt; to find a running Spot Instance by examining the response. If the status of the Spot Instance is &lt;code&gt;fulfilled&lt;/code&gt;, the instance ID appears in the response and contains the identifier of the instance. Alternatively, you can use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances"&gt;DescribeInstances&lt;/a&gt; with a filter to look for instances where the instance lifecycle is &lt;code&gt;spot&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;We recommend that you set &lt;code&gt;MaxResults&lt;/code&gt; to a value between 5 and 1000 to limit the number of results returned. This paginates the output, which makes the list more manageable and returns the results faster. If the list of results exceeds your &lt;code&gt;MaxResults&lt;/code&gt; value, then that number of results is returned along with a &lt;code&gt;NextToken&lt;/code&gt; value that can be passed to a subsequent &lt;code&gt;DescribeSpotInstanceRequests&lt;/code&gt; request to retrieve the remaining results.&lt;/p&gt; &lt;p&gt;Spot Instance requests are deleted four hours after they are canceled and their instances are terminated.&lt;/p&gt; |
| `spot_instance_requests_Cancel` | `EXEC` | `SpotInstanceRequestId` | &lt;p&gt;Cancels one or more Spot Instance requests.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Canceling a Spot Instance request does not terminate running Spot Instances associated with the request.&lt;/p&gt; &lt;/important&gt; |
