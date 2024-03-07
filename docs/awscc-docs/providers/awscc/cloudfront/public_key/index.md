---
title: public_key
hide_title: false
hide_table_of_contents: false
keywords:
  - public_key
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>public_key</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>public_key</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudfront.public_key</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>public_key_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>public_key</code> resource, the following permissions are required:

### Delete
```json
cloudfront:DeletePublicKey,
cloudfront:GetPublicKey
```

### Read
```json
cloudfront:GetPublicKey
```

### Update
```json
cloudfront:UpdatePublicKey,
cloudfront:GetPublicKey
```


## Example
```sql
SELECT
region,
created_time,
id,
public_key_config
FROM awscc.cloudfront.public_key
WHERE data__Identifier = '&lt;Id&gt;'
```
