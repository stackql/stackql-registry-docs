---
title: reserved_instances_offerings
hide_title: false
hide_table_of_contents: false
keywords:
  - reserved_instances_offerings
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
<tr><td><b>Name</b></td><td><code>reserved_instances_offerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.reserved_instances_offerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `recurringCharges` | `array` | The recurring charge tag assigned to the resource. |
| `offeringClass` | `string` | If &lt;code&gt;convertible&lt;/code&gt; it can be exchanged for Reserved Instances of the same or higher monetary value, with different configurations. If &lt;code&gt;standard&lt;/code&gt;, it is not possible to perform an exchange. |
| `offeringType` | `string` | The Reserved Instance offering type. |
| `instanceType` | `string` | The instance type on which the Reserved Instance can be used. |
| `fixedPrice` | `number` | The purchase price of the Reserved Instance. |
| `productDescription` | `string` | The Reserved Instance product platform description. |
| `currencyCode` | `string` | The currency of the Reserved Instance offering you are purchasing. It's specified using ISO 4217 standard currency codes. At this time, the only supported currency is &lt;code&gt;USD&lt;/code&gt;. |
| `duration` | `integer` | The duration of the Reserved Instance, in seconds. |
| `availabilityZone` | `string` | The Availability Zone in which the Reserved Instance can be used. |
| `scope` | `string` | Whether the Reserved Instance is applied to instances in a Region or an Availability Zone. |
| `instanceTenancy` | `string` | The tenancy of the instance. |
| `reservedInstancesOfferingId` | `string` | The ID of the Reserved Instance offering. This is the offering ID used in &lt;a&gt;GetReservedInstancesExchangeQuote&lt;/a&gt; to confirm that an exchange can be made. |
| `pricingDetailsSet` | `array` | The pricing details of the Reserved Instance offering. |
| `marketplace` | `boolean` | Indicates whether the offering is available through the Reserved Instance Marketplace (resale) or Amazon Web Services. If it's a Reserved Instance Marketplace offering, this is &lt;code&gt;true&lt;/code&gt;. |
| `usagePrice` | `number` | The usage price of the Reserved Instance, per hour. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `reserved_instances_offerings_Describe` | `SELECT` |  | &lt;p&gt;Describes Reserved Instance offerings that are available for purchase. With Reserved Instances, you purchase the right to launch instances for a period of time. During that time period, you do not receive insufficient capacity errors, and you pay a lower usage rate than the rate charged for On-Demand instances for the actual time used.&lt;/p&gt; &lt;p&gt;If you have listed your own Reserved Instances for sale in the Reserved Instance Marketplace, they will be excluded from these results. This is to ensure that you do not purchase your own Reserved Instances.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html"&gt;Reserved Instance Marketplace&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| `reserved_instances_offering_Purchase` | `EXEC` | `InstanceCount, ReservedInstancesOfferingId` | &lt;p&gt;Purchases a Reserved Instance for use with your account. With Reserved Instances, you pay a lower hourly rate compared to On-Demand instance pricing.&lt;/p&gt; &lt;p&gt;Use &lt;a&gt;DescribeReservedInstancesOfferings&lt;/a&gt; to get a list of Reserved Instance offerings that match your specifications. After you've purchased a Reserved Instance, you can check for your new Reserved Instance with &lt;a&gt;DescribeReservedInstances&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To queue a purchase for a future date and time, specify a purchase time. If you do not specify a purchase time, the default is the current time.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-on-demand-reserved-instances.html"&gt;Reserved Instances&lt;/a&gt; and &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html"&gt;Reserved Instance Marketplace&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
