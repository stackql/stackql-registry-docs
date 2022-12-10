---
title: instance_status
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_status
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
<tr><td><b>Name</b></td><td><code>instance_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.instance_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `availabilityZone` | `string` | The Availability Zone of the instance. |
| `eventsSet` | `array` | Any scheduled events associated with the instance. |
| `instanceId` | `string` | The ID of the instance. |
| `instanceState` | `object` | Describes the current state of an instance. |
| `instanceStatus` | `object` | Describes the status of an instance. |
| `outpostArn` | `string` | The Amazon Resource Name (ARN) of the Outpost. |
| `systemStatus` | `object` | Describes the status of an instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `instance_status_Describe` | `SELECT` |  | &lt;p&gt;Describes the status of the specified instances or all of your instances. By default, only running instances are described, unless you specifically indicate to return the status of all instances.&lt;/p&gt; &lt;p&gt;Instance status includes the following components:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Status checks&lt;/b&gt; - Amazon EC2 performs status checks on running EC2 instances to identify hardware and software issues. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html"&gt;Status checks for your instances&lt;/a&gt; and &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstances.html"&gt;Troubleshoot instances with failed status checks&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Scheduled events&lt;/b&gt; - Amazon EC2 can schedule events (such as reboot, stop, or terminate) for your instances related to hardware issues, software updates, or system maintenance. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html"&gt;Scheduled events for your instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Instance state&lt;/b&gt; - You can manage your instances from the moment you launch them through their termination. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html"&gt;Instance lifecycle&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `instance_status_Report` | `EXEC` | `InstanceId, ReasonCode, Status` | &lt;p&gt;Submits feedback about the status of an instance. The instance must be in the &lt;code&gt;running&lt;/code&gt; state. If your experience with the instance differs from the instance status returned by &lt;a&gt;DescribeInstanceStatus&lt;/a&gt;, use &lt;a&gt;ReportInstanceStatus&lt;/a&gt; to report your experience with the instance. Amazon EC2 collects this information to improve the accuracy of status checks.&lt;/p&gt; &lt;p&gt;Use of this action does not change the value returned by &lt;a&gt;DescribeInstanceStatus&lt;/a&gt;.&lt;/p&gt; |
