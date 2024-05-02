---
title: metered_product
hide_title: false
hide_table_of_contents: false
keywords:
  - metered_product
  - deadline
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>metered_product</code> resource, use <code>metered_products</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metered_product</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::MeteredProduct Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.deadline.metered_product</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>license_endpoint_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>product_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>family</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vendor</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
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
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
license_endpoint_id,
product_id,
port,
family,
vendor,
arn
FROM aws.deadline.metered_product
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>metered_product</code> resource, the following permissions are required:

### Read
```json
deadline:GetMeteredProduct,
deadline:ListMeteredProducts
```

### Delete
```json
deadline:DeleteMeteredProduct,
deadline:ListMeteredProducts
```

