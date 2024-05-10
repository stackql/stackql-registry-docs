---
title: named_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - named_queries
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


Used to retrieve a list of <code>named_queries</code> in a region or to create or delete a <code>named_queries</code> resource, use <code>named_query</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>named_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::NamedQuery</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.athena.named_queries" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="named_query_id" /></td><td><code>string</code></td><td>The unique ID of the query.</td></tr>
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
named_query_id
FROM aws.athena.named_queries
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
 "Database": "{{ Database }}",
 "QueryString": "{{ QueryString }}"
}
>>>
--required properties only
INSERT INTO aws.athena.named_queries (
 Database,
 QueryString,
 region
)
SELECT 
{{ Database }},
 {{ QueryString }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Database": "{{ Database }}",
 "Description": "{{ Description }}",
 "QueryString": "{{ QueryString }}",
 "WorkGroup": "{{ WorkGroup }}"
}
>>>
--all properties
INSERT INTO aws.athena.named_queries (
 Name,
 Database,
 Description,
 QueryString,
 WorkGroup,
 region
)
SELECT 
 {{ Name }},
 {{ Database }},
 {{ Description }},
 {{ QueryString }},
 {{ WorkGroup }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.athena.named_queries
WHERE data__Identifier = '<NamedQueryId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>named_queries</code> resource, the following permissions are required:

### Create
```json
athena:CreateNamedQuery
```

### List
```json
athena:ListNamedQueries
```

### Delete
```json
athena:DeleteNamedQuery
```

