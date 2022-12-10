---
title: reserved_instances_listings
hide_title: false
hide_table_of_contents: false
keywords:
  - reserved_instances_listings
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
<tr><td><b>Name</b></td><td><code>reserved_instances_listings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.reserved_instances_listings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `updateDate` | `string` | The last modified timestamp of the listing. |
| `status` | `string` | The status of the Reserved Instance listing. |
| `createDate` | `string` | The time the listing was created. |
| `tagSet` | `array` | Any tags assigned to the resource. |
| `clientToken` | `string` | A unique, case-sensitive key supplied by the client to ensure that the request is idempotent. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html"&gt;Ensuring Idempotency&lt;/a&gt;. |
| `reservedInstancesId` | `string` | The ID of the Reserved Instance. |
| `statusMessage` | `string` | The reason for the current status of the Reserved Instance listing. The response can be blank. |
| `instanceCounts` | `array` | The number of instances in this state. |
| `reservedInstancesListingId` | `string` | The ID of the Reserved Instance listing. |
| `priceSchedules` | `array` | The price of the Reserved Instance listing. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `reserved_instances_listings_Describe` | `SELECT` |  | &lt;p&gt;Describes your account's Reserved Instance listings in the Reserved Instance Marketplace.&lt;/p&gt; &lt;p&gt;The Reserved Instance Marketplace matches sellers who want to resell Reserved Instance capacity that they no longer need with buyers who want to purchase additional capacity. Reserved Instances bought and sold through the Reserved Instance Marketplace work like any other Reserved Instances.&lt;/p&gt; &lt;p&gt;As a seller, you choose to list some or all of your Reserved Instances, and you specify the upfront price to receive for them. Your Reserved Instances are then listed in the Reserved Instance Marketplace and are available for purchase.&lt;/p&gt; &lt;p&gt;As a buyer, you specify the configuration of the Reserved Instance to purchase, and the Marketplace matches what you're searching for with what's available. The Marketplace first sells the lowest priced Reserved Instances to you, and continues to sell available Reserved Instance listings to you until your demand is met. You are charged based on the total price of all of the listings that you purchase.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html"&gt;Reserved Instance Marketplace&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| `reserved_instances_listing_Create` | `INSERT` | `ClientToken, InstanceCount, PriceSchedules, ReservedInstancesId` | &lt;p&gt;Creates a listing for Amazon EC2 Standard Reserved Instances to be sold in the Reserved Instance Marketplace. You can submit one Standard Reserved Instance listing at a time. To get a list of your Standard Reserved Instances, you can use the &lt;a&gt;DescribeReservedInstances&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only Standard Reserved Instances can be sold in the Reserved Instance Marketplace. Convertible Reserved Instances cannot be sold.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;The Reserved Instance Marketplace matches sellers who want to resell Standard Reserved Instance capacity that they no longer need with buyers who want to purchase additional capacity. Reserved Instances bought and sold through the Reserved Instance Marketplace work like any other Reserved Instances.&lt;/p&gt; &lt;p&gt;To sell your Standard Reserved Instances, you must first register as a seller in the Reserved Instance Marketplace. After completing the registration process, you can create a Reserved Instance Marketplace listing of some or all of your Standard Reserved Instances, and specify the upfront price to receive for them. Your Standard Reserved Instance listings then become available for purchase. To view the details of your Standard Reserved Instance listing, you can use the &lt;a&gt;DescribeReservedInstancesListings&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html"&gt;Reserved Instance Marketplace&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| `reserved_instances_listing_Cancel` | `EXEC` | `ReservedInstancesListingId` | &lt;p&gt;Cancels the specified Reserved Instance listing in the Reserved Instance Marketplace.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html"&gt;Reserved Instance Marketplace&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
