---
title: partnership
hide_title: false
hide_table_of_contents: false
keywords:
  - partnership
  - b2bi
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>partnership</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partnership</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>partnership</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.b2bi.partnership</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>capabilities</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>email</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>modified_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>partnership_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>partnership_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>phone</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>profile_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>trading_partner_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>partnership</code> resource, the following permissions are required:

### Read
<pre>
b2bi:GetPartnership,
b2bi:ListTagsForResource</pre>

### Update
<pre>
b2bi:TagResource,
b2bi:UntagResource,
b2bi:UpdatePartnership</pre>

### Delete
<pre>
b2bi:DeletePartnership</pre>


## Example
```sql
SELECT
region,
capabilities,
created_at,
email,
modified_at,
name,
partnership_arn,
partnership_id,
phone,
profile_id,
tags,
trading_partner_id
FROM awscc.b2bi.partnership
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;PartnershipId&gt;'
```
