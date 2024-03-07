---
title: prepared_statements
hide_title: false
hide_table_of_contents: false
keywords:
  - prepared_statements
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
Retrieves a list of <code>prepared_statements</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prepared_statements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>prepared_statements</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.athena.prepared_statements</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>statement_name</code></td><td><code>string</code></td><td>The name of the prepared statement.</td></tr>
<tr><td><code>work_group</code></td><td><code>string</code></td><td>The name of the workgroup to which the prepared statement belongs.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
statement_name,
work_group
FROM awscc.athena.prepared_statements
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>prepared_statements</code> resource, the following permissions are required:

### Create
```json
athena:CreatePreparedStatement,
athena:GetPreparedStatement
```

### List
```json
athena:ListPreparedStatements
```

