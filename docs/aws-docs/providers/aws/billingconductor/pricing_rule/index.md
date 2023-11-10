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
<tr><td><b>Description</b></td><td>pricing_rule</td></tr>
<tr><td><b>Id</b></td><td><code>aws.billingconductor.pricing_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Pricing rule ARN</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Pricing rule name</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Pricing rule description</td></tr>
<tr><td><code>scope</code></td><td><code>string</code></td><td>A term used to categorize the granularity of a Pricing Rule.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>One of MARKUP, DISCOUNT or TIERING that describes the behaviour of the pricing rule.</td></tr>
<tr><td><code>modifier_percentage</code></td><td><code>number</code></td><td>Pricing rule modifier percentage</td></tr>
<tr><td><code>service</code></td><td><code>string</code></td><td>The service which a pricing rule is applied on</td></tr>
<tr><td><code>billing_entity</code></td><td><code>string</code></td><td>The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplaces. Supported billing entities are AWS, AWS Marketplace, and AISPL.</td></tr>
<tr><td><code>tiering</code></td><td><code>object</code></td><td>The set of tiering configurations for the pricing rule.</td></tr>
<tr><td><code>usage_type</code></td><td><code>string</code></td><td>The UsageType which a SKU pricing rule is modifying</td></tr>
<tr><td><code>operation</code></td><td><code>string</code></td><td>The Operation which a SKU pricing rule is modifying</td></tr>
<tr><td><code>associated_pricing_plan_count</code></td><td><code>integer</code></td><td>The number of pricing plans associated with pricing rule</td></tr>
<tr><td><code>creation_time</code></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><code>last_modified_time</code></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
name,
description,
scope,
type,
modifier_percentage,
service,
billing_entity,
tiering,
usage_type,
operation,
associated_pricing_plan_count,
creation_time,
last_modified_time,
tags
FROM aws.billingconductor.pricing_rule
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
