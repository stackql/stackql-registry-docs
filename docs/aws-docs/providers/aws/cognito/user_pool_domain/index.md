---
title: user_pool_domain
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_domain
  - cognito
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>user_pool_domain</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_pool_domain</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cognito.user_pool_domain</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cloud_front_distribution</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_pool_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>custom_domain_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
cloud_front_distribution,
user_pool_id,
id,
domain,
custom_domain_config
FROM aws.cognito.user_pool_domain
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
