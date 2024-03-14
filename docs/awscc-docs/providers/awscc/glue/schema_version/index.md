---
title: schema_version
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_version
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
Gets an individual <code>schema_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>schema_version</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.glue.schema_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>schema</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>schema_definition</code></td><td><code>string</code></td><td>Complete definition of the schema in plain-text.</td></tr>
<tr><td><code>version_id</code></td><td><code>string</code></td><td>Represents the version ID associated with the schema version.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
schema,
schema_definition,
version_id
FROM awscc.glue.schema_version
WHERE data__Identifier = '<VersionId>';
```

## Permissions

To operate on the <code>schema_version</code> resource, the following permissions are required:

### Read
```json
glue:GetSchemaVersion
```

### Delete
```json
glue:DeleteSchemaVersions,
glue:GetSchemaVersion
```

