---
title: scheduled_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_instances
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
<tr><td><b>Name</b></td><td><code>scheduled_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.scheduled_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availabilityZone" /> | `string` | The Availability Zone. |
| <CopyableCode code="createDate" /> | `string` | The date when the Scheduled Instance was purchased. |
| <CopyableCode code="hourlyPrice" /> | `string` | The hourly price for a single instance. |
| <CopyableCode code="instanceCount" /> | `integer` | The number of instances. |
| <CopyableCode code="instanceType" /> | `string` | The instance type. |
| <CopyableCode code="networkPlatform" /> | `string` | The network platform (&lt;code&gt;EC2-Classic&lt;/code&gt; or &lt;code&gt;EC2-VPC&lt;/code&gt;). |
| <CopyableCode code="nextSlotStartTime" /> | `string` | The time for the next schedule to start. |
| <CopyableCode code="platform" /> | `string` | The platform (&lt;code&gt;Linux/UNIX&lt;/code&gt; or &lt;code&gt;Windows&lt;/code&gt;). |
| <CopyableCode code="previousSlotEndTime" /> | `string` | The time that the previous schedule ended or will end. |
| <CopyableCode code="recurrence" /> | `object` | Describes the recurring schedule for a Scheduled Instance. |
| <CopyableCode code="scheduledInstanceId" /> | `string` | The Scheduled Instance ID. |
| <CopyableCode code="slotDurationInHours" /> | `integer` | The number of hours in the schedule. |
| <CopyableCode code="termEndDate" /> | `string` | The end date for the Scheduled Instance. |
| <CopyableCode code="termStartDate" /> | `string` | The start date for the Scheduled Instance. |
| <CopyableCode code="totalScheduledInstanceHours" /> | `integer` | The total number of hours for a single instance for the entire term. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="scheduled_instances_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes the specified Scheduled Instances or all your Scheduled Instances. |
| <CopyableCode code="scheduled_instances_Purchase" /> | `EXEC` | <CopyableCode code="PurchaseRequest, region" /> | &lt;p&gt;Purchases the Scheduled Instances with the specified schedule.&lt;/p&gt; &lt;p&gt;Scheduled Instances enable you to purchase Amazon EC2 compute capacity by the hour for a one-year term. Before you can purchase a Scheduled Instance, you must call &lt;a&gt;DescribeScheduledInstanceAvailability&lt;/a&gt; to check for available schedules and obtain a purchase token. After you purchase a Scheduled Instance, you must call &lt;a&gt;RunScheduledInstances&lt;/a&gt; during each scheduled time period.&lt;/p&gt; &lt;p&gt;After you purchase a Scheduled Instance, you can't cancel, modify, or resell your purchase.&lt;/p&gt; |
| <CopyableCode code="scheduled_instances_Run" /> | `EXEC` | <CopyableCode code="LaunchSpecification, ScheduledInstanceId, region" /> | &lt;p&gt;Launches the specified Scheduled Instances.&lt;/p&gt; &lt;p&gt;Before you can launch a Scheduled Instance, you must purchase it and obtain an identifier using &lt;a&gt;PurchaseScheduledInstances&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You must launch a Scheduled Instance during its scheduled time period. You can't stop or reboot a Scheduled Instance, but you can terminate it as needed. If you terminate a Scheduled Instance before the current scheduled time period ends, you can launch it again after a few minutes. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-scheduled-instances.html"&gt;Scheduled Instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
