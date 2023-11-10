---
title: api_cache
hide_title: false
hide_table_of_contents: false
keywords:
  - api_cache
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
Gets an individual <code>api_cache</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_cache</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>api_cache</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appsync.api_cache</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>transit_encryption_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>at_rest_encryption_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>api_caching_behavior</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ttl</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
type,
transit_encryption_enabled,
at_rest_encryption_enabled,
id,
api_id,
api_caching_behavior,
ttl
FROM aws.appsync.api_cache
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
