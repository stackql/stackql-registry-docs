---
title: prepared_statement
hide_title: false
hide_table_of_contents: false
keywords:
  - prepared_statement
  - athena
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>prepared_statement</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prepared_statement</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>prepared_statement</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.athena.prepared_statement</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>statement_name</code></td><td><code>string</code></td><td>The name of the prepared statement.</td></tr>
<tr><td><code>work_group</code></td><td><code>string</code></td><td>The name of the workgroup to which the prepared statement belongs.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the prepared statement.</td></tr>
<tr><td><code>query_statement</code></td><td><code>string</code></td><td>The query string for the prepared statement.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
statement_name,
work_group,
description,
query_statement
FROM awscc.athena.prepared_statement
WHERE data__Identifier = '<StatementName>|<WorkGroup>';
```

## Permissions

To operate on the <code>prepared_statement</code> resource, the following permissions are required:

### Read
```json
athena:GetPreparedStatement
```

### Update
```json
athena:UpdatePreparedStatement
```

### Delete
```json
athena:DeletePreparedStatement,
athena:GetPreparedStatement
```

