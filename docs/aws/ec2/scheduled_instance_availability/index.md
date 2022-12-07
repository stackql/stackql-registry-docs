---
title: scheduled_instance_availability
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_instance_availability
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
<tr><td><b>Name</b></td><td><code>scheduled_instance_availability</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.scheduled_instance_availability</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `hourlyPrice` | `string` | The hourly price for a single instance. |
| `totalScheduledInstanceHours` | `integer` | The total number of hours for a single instance for the entire term. |
| `networkPlatform` | `string` | The network platform (&lt;code&gt;EC2-Classic&lt;/code&gt; or &lt;code&gt;EC2-VPC&lt;/code&gt;). |
| `availabilityZone` | `string` | The Availability Zone. |
| `purchaseToken` | `string` | The purchase token. This token expires in two hours. |
| `availableInstanceCount` | `integer` | The number of available instances. |
| `maxTermDurationInDays` | `integer` | The maximum term. The only possible value is 365 days. |
| `recurrence` | `object` | Describes the recurring schedule for a Scheduled Instance. |
| `instanceType` | `string` | The instance type. You can specify one of the C3, C4, M4, or R3 instance types. |
| `slotDurationInHours` | `integer` | The number of hours in the schedule. |
| `firstSlotStartTime` | `string` | The time period for the first schedule to start. |
| `minTermDurationInDays` | `integer` | The minimum term. The only possible value is 365 days. |
| `platform` | `string` | The platform (&lt;code&gt;Linux/UNIX&lt;/code&gt; or &lt;code&gt;Windows&lt;/code&gt;). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `scheduled_instance_availability_Describe` | `SELECT` | `FirstSlotStartTimeRange, Recurrence` |
