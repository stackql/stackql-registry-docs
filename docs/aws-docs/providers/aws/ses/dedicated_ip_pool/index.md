---
title: dedicated_ip_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_ip_pool
  - ses
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>dedicated_ip_pool</code> resource, use <code>dedicated_ip_pools</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dedicated_ip_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SES::DedicatedIpPool</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ses.dedicated_ip_pool</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>pool_name</code></td><td><code>string</code></td><td>The name of the dedicated IP pool.</td></tr>
<tr><td><code>scaling_mode</code></td><td><code>string</code></td><td>Specifies whether the dedicated IP pool is managed or not. The default value is STANDARD.</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
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
pool_name,
scaling_mode
FROM aws.ses.dedicated_ip_pool
WHERE data__Identifier = '<PoolName>';
```

## Permissions

To operate on the <code>dedicated_ip_pool</code> resource, the following permissions are required:

### Read
```json
ses:GetDedicatedIpPool,
ses:GetDedicatedIps
```

### Update
```json
ses:PutDedicatedIpPoolScalingAttributes,
ses:GetDedicatedIpPool
```

### Delete
```json
ses:DeleteDedicatedIpPool
```

