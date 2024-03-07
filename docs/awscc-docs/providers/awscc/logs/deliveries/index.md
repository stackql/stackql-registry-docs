---
title: deliveries
hide_title: false
hide_table_of_contents: false
keywords:
  - deliveries
  - logs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>deliveries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deliveries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>deliveries</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.logs.deliveries</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>delivery_id</code></td><td><code>string</code></td><td>The unique ID that identifies this delivery in your account.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>deliveries</code> resource, the following permissions are required:

### Create
<pre>
logs:CreateDelivery,
logs:GetDelivery,
logs:DescribeDeliveries,
logs:ListTagsForResource,
logs:TagResource,
logs:GetDeliverySource,
logs:GetDeliveryDestination</pre>

### List
<pre>
logs:DescribeDeliveries,
logs:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
delivery_id
FROM awscc.logs.deliveries
WHERE region = 'us-east-1'
```
