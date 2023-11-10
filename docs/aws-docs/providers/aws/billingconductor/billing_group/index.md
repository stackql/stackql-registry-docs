---
title: billing_group
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_group
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
Gets an individual <code>billing_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>billing_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.billingconductor.billing_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Billing Group ARN</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>primary_account_id</code></td><td><code>string</code></td><td>This account will act as a virtual payer account of the billing group</td></tr>
<tr><td><code>computation_preference</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>account_grouping</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>size</code></td><td><code>integer</code></td><td>Number of accounts in the billing group</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status_reason</code></td><td><code>string</code></td><td></td></tr>
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
primary_account_id,
computation_preference,
account_grouping,
size,
status,
status_reason,
creation_time,
last_modified_time,
tags
FROM aws.billingconductor.billing_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
