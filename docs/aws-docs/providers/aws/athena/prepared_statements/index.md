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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>prepared_statements</code> in a region or to create or delete a <code>prepared_statements</code> resource, use <code>prepared_statement</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prepared_statements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::PreparedStatement</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.athena.prepared_statements" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="statement_name" /></td><td><code>string</code></td><td>The name of the prepared statement.</td></tr>
<tr><td><CopyableCode code="work_group" /></td><td><code>string</code></td><td>The name of the workgroup to which the prepared statement belongs.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
statement_name,
work_group
FROM aws.athena.prepared_statements
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "StatementName": "{{ StatementName }}",
 "WorkGroup": "{{ WorkGroup }}",
 "QueryStatement": "{{ QueryStatement }}"
}
>>>
--required properties only
INSERT INTO aws.athena.prepared_statements (
 StatementName,
 WorkGroup,
 QueryStatement,
 region
)
SELECT 
{{ .StatementName }},
 {{ .WorkGroup }},
 {{ .QueryStatement }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "StatementName": "{{ StatementName }}",
 "WorkGroup": "{{ WorkGroup }}",
 "Description": "{{ Description }}",
 "QueryStatement": "{{ QueryStatement }}"
}
>>>
--all properties
INSERT INTO aws.athena.prepared_statements (
 StatementName,
 WorkGroup,
 Description,
 QueryStatement,
 region
)
SELECT 
 {{ .StatementName }},
 {{ .WorkGroup }},
 {{ .Description }},
 {{ .QueryStatement }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.athena.prepared_statements
WHERE data__Identifier = '<StatementName|WorkGroup>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>prepared_statements</code> resource, the following permissions are required:

### Create
```json
athena:CreatePreparedStatement,
athena:GetPreparedStatement
```

### Delete
```json
athena:DeletePreparedStatement,
athena:GetPreparedStatement
```

### List
```json
athena:ListPreparedStatements
```

