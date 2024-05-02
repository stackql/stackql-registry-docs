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
Used to retrieve a list of <code>deliveries</code> in a region or create a <code>deliveries</code> resource, use <code>delivery</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deliveries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This structure contains information about one delivery in your account.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;A delivery is a connection between a logical delivery source and a logical delivery destination.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;For more information, see &#91;CreateDelivery&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonCloudWatchLogs&#x2F;latest&#x2F;APIReference&#x2F;API_CreateDelivery.html).</td></tr>
<tr><td><b>Id</b></td><td><code>aws.logs.deliveries</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>delivery_id</code></td><td><code>string</code></td><td>The unique ID that identifies this delivery in your account.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
delivery_id
FROM aws.logs.deliveries
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>deliveries</code> resource, the following permissions are required:

### Create
```json
logs:CreateDelivery,
logs:GetDelivery,
logs:DescribeDeliveries,
logs:ListTagsForResource,
logs:TagResource,
logs:GetDeliverySource,
logs:GetDeliveryDestination
```

### List
```json
logs:DescribeDeliveries,
logs:ListTagsForResource
```

