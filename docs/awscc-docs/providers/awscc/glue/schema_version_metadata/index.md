---
title: schema_version_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_version_metadata
  - glue
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>schema_version_metadata</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_version_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>schema_version_metadata</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.glue.schema_version_metadata</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>schema_version_id</code></td><td><code>string</code></td><td>Represents the version ID associated with the schema version.</td></tr>
<tr><td><code>key</code></td><td><code>string</code></td><td>Metadata key</td></tr>
<tr><td><code>value</code></td><td><code>string</code></td><td>Metadata value</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>schema_version_metadata</code> resource, the following permissions are required:

### Read
<pre>
glue:querySchemaVersionMetadata</pre>

### Delete
<pre>
glue:removeSchemaVersionMetadata</pre>


## Example
```sql
SELECT
region,
schema_version_id,
key,
value
FROM awscc.glue.schema_version_metadata
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;SchemaVersionId&gt;'
AND data__Identifier = '&lt;Key&gt;'
AND data__Identifier = '&lt;Value&gt;'
```
