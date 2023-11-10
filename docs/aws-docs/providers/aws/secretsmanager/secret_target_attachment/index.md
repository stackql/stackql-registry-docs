---
title: secret_target_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - secret_target_attachment
  - secretsmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>secret_target_attachment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secret_target_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>secret_target_attachment</td></tr>
<tr><td><b>Id</b></td><td><code>aws.secretsmanager.secret_target_attachment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>secret_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
secret_id,
target_type,
target_id
FROM aws.secretsmanager.secret_target_attachment
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
