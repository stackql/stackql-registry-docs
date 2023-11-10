---
title: api_key
hide_title: false
hide_table_of_contents: false
keywords:
  - api_key
  - appsync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>api_key</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>api_key</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appsync.api_key</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>api_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>expires</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
api_key,
description,
api_key_id,
expires,
arn,
api_id
FROM aws.appsync.api_key
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ApiKeyId&gt;'
```
