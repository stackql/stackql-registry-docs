---
title: pricing_plan
hide_title: false
hide_table_of_contents: false
keywords:
  - pricing_plan
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
Gets an individual <code>pricing_plan</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pricing_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.billingconductor.pricing_plan</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Pricing Plan ARN</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PricingRuleArns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Size</code></td><td><code>integer</code></td><td>Number of associated pricing rules</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CreationTime</code></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><code>LastModifiedTime</code></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.billingconductor.pricing_plan
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Arn&gt;'
</pre>
