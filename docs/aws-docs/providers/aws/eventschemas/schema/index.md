---
title: schema
hide_title: false
hide_table_of_contents: false
keywords:
  - schema
  - eventschemas
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>schema</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>schema</td></tr>
<tr><td><b>Id</b></td><td><code>aws.eventschemas.schema</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schema_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>content</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>registry_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schema_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schema_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
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
schema_version,
content,
registry_name,
id,
schema_arn,
schema_name,
tags
FROM aws.eventschemas.schema
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
