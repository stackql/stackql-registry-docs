---
title: flow_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_logs
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
<tr><td><b>Name</b></td><td><code>flow_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.flow_logs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `deliverLogsPermissionArn` | `string` | The ARN of the IAM role that posts logs to CloudWatch Logs. |
| `maxAggregationInterval` | `integer` | &lt;p&gt;The maximum interval of time, in seconds, during which a flow of packets is captured and aggregated into a flow log record.&lt;/p&gt; &lt;p&gt;When a network interface is attached to a &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances"&gt;Nitro-based instance&lt;/a&gt;, the aggregation interval is always 60 seconds (1 minute) or less, regardless of the specified value.&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;60&lt;/code&gt; \| &lt;code&gt;600&lt;/code&gt; &lt;/p&gt; |
| `resourceId` | `string` | The ID of the resource on which the flow log was created. |
| `tagSet` | `array` | The tags for the flow log. |
| `flowLogId` | `string` | The flow log ID. |
| `logDestinationType` | `string` | The type of destination to which the flow log data is published. Flow log data can be published to CloudWatch Logs or Amazon S3. |
| `logDestination` | `string` | The destination to which the flow log data is published. Flow log data can be published to an CloudWatch Logs log group or an Amazon S3 bucket. If the flow log publishes to CloudWatch Logs, this element indicates the Amazon Resource Name (ARN) of the CloudWatch Logs log group to which the data is published. If the flow log publishes to Amazon S3, this element indicates the ARN of the Amazon S3 bucket to which the data is published. |
| `flowLogStatus` | `string` | The status of the flow log (&lt;code&gt;ACTIVE&lt;/code&gt;). |
| `logFormat` | `string` | The format of the flow log record. |
| `logGroupName` | `string` | The name of the flow log group. |
| `creationTime` | `string` | The date and time the flow log was created. |
| `deliverLogsStatus` | `string` | The status of the logs delivery (&lt;code&gt;SUCCESS&lt;/code&gt; \| &lt;code&gt;FAILED&lt;/code&gt;). |
| `destinationOptions` | `object` | Describes the destination options for a flow log. |
| `trafficType` | `string` | The type of traffic captured for the flow log. |
| `deliverLogsErrorMessage` | `string` | Information about the error that occurred. &lt;code&gt;Rate limited&lt;/code&gt; indicates that CloudWatch Logs throttling has been applied for one or more network interfaces, or that you've reached the limit on the number of log groups that you can create. &lt;code&gt;Access error&lt;/code&gt; indicates that the IAM role associated with the flow log does not have sufficient permissions to publish to CloudWatch Logs. &lt;code&gt;Unknown error&lt;/code&gt; indicates an internal error. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `flow_logs_Describe` | `SELECT` |  | Describes one or more flow logs. To view the information in your flow logs (the log streams for the network interfaces), you must use the CloudWatch Logs console or the CloudWatch Logs API. |
| `flow_logs_Create` | `INSERT` | `ResourceId, ResourceType, TrafficType` | &lt;p&gt;Creates one or more flow logs to capture information about IP traffic for a specific network interface, subnet, or VPC. &lt;/p&gt; &lt;p&gt;Flow log data for a monitored network interface is recorded as flow log records, which are log events consisting of fields that describe the traffic flow. For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-log-records"&gt;Flow log records&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;When publishing to CloudWatch Logs, flow log records are published to a log group, and each network interface has a unique log stream in the log group. When publishing to Amazon S3, flow log records for all of the monitored network interfaces are published to a single log file object that is stored in the specified bucket.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html"&gt;VPC Flow Logs&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `flow_logs_Delete` | `DELETE` | `FlowLogId` | Deletes one or more flow logs. |
