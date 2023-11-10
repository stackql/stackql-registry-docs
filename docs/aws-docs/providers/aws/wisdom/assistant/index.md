---
title: assistant
hide_title: false
hide_table_of_contents: false
keywords:
  - assistant
  - wisdom
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>assistant</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assistant</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>assistant</td></tr>
<tr><td><b>Id</b></td><td><code>aws.wisdom.assistant</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>assistant_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>assistant_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>server_side_encryption_configuration</code></td><td><code>object</code></td><td></td></tr>
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
type,
description,
assistant_arn,
assistant_id,
server_side_encryption_configuration,
tags,
name
FROM aws.wisdom.assistant
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AssistantId&gt;'
```
