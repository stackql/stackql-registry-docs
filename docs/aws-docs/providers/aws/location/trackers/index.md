---
title: trackers
hide_title: false
hide_table_of_contents: false
keywords:
  - trackers
  - location
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>trackers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trackers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.location.trackers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CreateTime</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PricingPlan</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>PricingPlanDataSource</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PositionFiltering</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>TrackerArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>TrackerName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>UpdateTime</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.location.trackers
WHERE region = 'us-east-1'
```
