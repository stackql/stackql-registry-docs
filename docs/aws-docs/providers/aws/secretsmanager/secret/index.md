---
title: secret
hide_title: false
hide_table_of_contents: false
keywords:
  - secret
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
Gets an individual <code>secret</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secret</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>secret</td></tr>
<tr><td><b>Id</b></td><td><code>aws.secretsmanager.secret</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>secret_string</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>generate_secret_string</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>replica_regions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
kms_key_id,
secret_string,
generate_secret_string,
replica_regions,
id,
tags,
name
FROM aws.secretsmanager.secret
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
