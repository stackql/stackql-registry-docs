---
title: custom_line_items
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_line_items
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
Retrieves a list of <code>custom_line_items</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_line_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>custom_line_items</td></tr>
<tr><td><b>Id</b></td><td><code>aws.billingconductor.custom_line_items</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CustomLineItemChargeDetails</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>BillingGroupArn</code></td><td><code>string</code></td><td>Billing Group ARN</td></tr>
<tr><td><code>BillingPeriodRange</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>ARN</td></tr>
<tr><td><code>CreationTime</code></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><code>LastModifiedTime</code></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
<tr><td><code>AssociationSize</code></td><td><code>integer</code></td><td>Number of source values associated to this custom line item</td></tr>
<tr><td><code>ProductCode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CurrencyCode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.billingconductor.custom_line_items
WHERE region = 'us-east-1'
</pre>
