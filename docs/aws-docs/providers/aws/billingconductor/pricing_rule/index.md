---
title: pricing_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - pricing_rule
  - billingconductor
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>pricing_rule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pricing_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.billingconductor.pricing_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Pricing rule ARN</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Pricing rule name</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>Pricing rule description</td></tr>
<tr><td><code>Scope</code></td><td><code>string</code></td><td>A term used to categorize the granularity of a Pricing Rule.</td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td>One of MARKUP, DISCOUNT or TIERING that describes the behaviour of the pricing rule.</td></tr>
<tr><td><code>ModifierPercentage</code></td><td><code>number</code></td><td>Pricing rule modifier percentage</td></tr>
<tr><td><code>Service</code></td><td><code>string</code></td><td>The service which a pricing rule is applied on</td></tr>
<tr><td><code>BillingEntity</code></td><td><code>string</code></td><td>The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplaces. Supported billing entities are AWS, AWS Marketplace, and AISPL.</td></tr>
<tr><td><code>Tiering</code></td><td><code>object</code></td><td>The set of tiering configurations for the pricing rule.</td></tr>
<tr><td><code>UsageType</code></td><td><code>string</code></td><td>The UsageType which a SKU pricing rule is modifying</td></tr>
<tr><td><code>Operation</code></td><td><code>string</code></td><td>The Operation which a SKU pricing rule is modifying</td></tr>
<tr><td><code>AssociatedPricingPlanCount</code></td><td><code>integer</code></td><td>The number of pricing plans associated with pricing rule</td></tr>
<tr><td><code>CreationTime</code></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><code>LastModifiedTime</code></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.billingconductor.pricing_rule
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Arn&gt;'
</pre>
