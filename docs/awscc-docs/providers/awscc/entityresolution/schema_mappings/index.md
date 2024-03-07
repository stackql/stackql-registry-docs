---
title: schema_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_mappings
  - entityresolution
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>schema_mappings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>schema_mappings</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.entityresolution.schema_mappings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>schema_name</code></td><td><code>undefined</code></td><td>The name of the SchemaMapping</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>schema_mappings</code> resource, the following permissions are required:

### Create
<pre>
entityresolution:CreateSchemaMapping,
entityresolution:GetSchemaMapping,
entityresolution:TagResource</pre>

### List
<pre>
entityresolution:ListSchemaMappings</pre>


## Example
```sql
SELECT
region,
schema_name
FROM awscc.entityresolution.schema_mappings
WHERE region = 'us-east-1'
```
