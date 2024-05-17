---
title: reserved_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - reserved_instances
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
<tr><td><b>Name</b></td><td><code>reserved_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.reserved_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availabilityZone" /> | `string` | The Availability Zone in which the Reserved Instance can be used. |
| <CopyableCode code="currencyCode" /> | `string` | The currency of the Reserved Instance. It's specified using ISO 4217 standard currency codes. At this time, the only supported currency is &lt;code&gt;USD&lt;/code&gt;. |
| <CopyableCode code="duration" /> | `integer` | The duration of the Reserved Instance, in seconds. |
| <CopyableCode code="end" /> | `string` | The time when the Reserved Instance expires. |
| <CopyableCode code="fixedPrice" /> | `number` | The purchase price of the Reserved Instance. |
| <CopyableCode code="instanceCount" /> | `integer` | The number of reservations purchased. |
| <CopyableCode code="instanceTenancy" /> | `string` | The tenancy of the instance. |
| <CopyableCode code="instanceType" /> | `string` | The instance type on which the Reserved Instance can be used. |
| <CopyableCode code="offeringClass" /> | `string` | The offering class of the Reserved Instance. |
| <CopyableCode code="offeringType" /> | `string` | The Reserved Instance offering type. |
| <CopyableCode code="productDescription" /> | `string` | The Reserved Instance product platform description. |
| <CopyableCode code="recurringCharges" /> | `array` | The recurring charge tag assigned to the resource. |
| <CopyableCode code="reservedInstancesId" /> | `string` | The ID of the Reserved Instance. |
| <CopyableCode code="scope" /> | `string` | The scope of the Reserved Instance. |
| <CopyableCode code="start" /> | `string` | The date and time the Reserved Instance started. |
| <CopyableCode code="state" /> | `string` | The state of the Reserved Instance purchase. |
| <CopyableCode code="tagSet" /> | `array` | Any tags assigned to the resource. |
| <CopyableCode code="usagePrice" /> | `number` | The usage price of the Reserved Instance, per hour. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="reserved_instances_Describe" /> | `SELECT` | <CopyableCode code="region" /> | &lt;p&gt;Describes one or more of the Reserved Instances that you purchased.&lt;/p&gt; &lt;p&gt;For more information about Reserved Instances, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-on-demand-reserved-instances.html"&gt;Reserved Instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="reserved_instances_Modify" /> | `EXEC` | <CopyableCode code="ReservedInstancesConfigurationSetItemType, ReservedInstancesId, region" /> | &lt;p&gt;Modifies the Availability Zone, instance count, instance type, or network platform (EC2-Classic or EC2-VPC) of your Reserved Instances. The Reserved Instances to be modified must be identical, except for Availability Zone, network platform, and instance type.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-modifying.html"&gt;Modifying Reserved Instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
