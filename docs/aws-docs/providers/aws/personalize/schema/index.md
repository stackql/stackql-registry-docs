---
title: schema
hide_title: false
hide_table_of_contents: false
keywords:
  - schema
  - personalize
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
<tr><td><b>Id</b></td><td><code>aws.personalize.schema</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name for the schema.</td></tr>
<tr><td><code>schema_arn</code></td><td><code>string</code></td><td>Arn for the schema.</td></tr>
<tr><td><code>schema</code></td><td><code>string</code></td><td>A schema in Avro JSON format.</td></tr>
<tr><td><code>domain</code></td><td><code>string</code></td><td>The domain of a Domain dataset group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
schema_arn,
schema,
domain
FROM aws.personalize.schema
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;SchemaArn&gt;'
```
