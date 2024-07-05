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

Creates, updates, deletes or gets a <code>named_query</code> resource or lists <code>named_queries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>named_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::NamedQuery</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.athena.named_queries" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The query name.</td></tr>
<tr><td><CopyableCode code="database" /></td><td><code>string</code></td><td>The database to which the query belongs.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The query description.</td></tr>
<tr><td><CopyableCode code="query_string" /></td><td><code>string</code></td><td>The contents of the query with all query statements.</td></tr>
<tr><td><CopyableCode code="work_group" /></td><td><code>string</code></td><td>The name of the workgroup that contains the named query.</td></tr>
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
    <td><CopyableCode code="Database, QueryString, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>named_queries</code> in a region.
```sql
SELECT
region,
name,
database,
description,
query_string,
work_group,
named_query_id
FROM aws.athena.named_queries
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>named_query</code>.
```sql
SELECT
region,
name,
database,
description,
query_string,
work_group,
named_query_id
FROM aws.athena.named_queries
WHERE region = 'us-east-1' AND data__Identifier = '<NamedQueryId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>named_query</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.athena.named_queries (
 Database,
 QueryString,
 region
)
SELECT 
'{{ Database }}',
 '{{ QueryString }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.athena.named_queries (
 Name,
 Database,
 Description,
 QueryString,
 WorkGroup,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Database }}',
 '{{ Description }}',
 '{{ QueryString }}',
 '{{ WorkGroup }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: named_query
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Database
        value: '{{ Database }}'
      - name: Description
        value: '{{ Description }}'
      - name: QueryString
        value: '{{ QueryString }}'
      - name: WorkGroup
        value: '{{ WorkGroup }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
athena:GetNamedQuery
```

### List
```json
athena:ListNamedQueries
```

### Delete
```json
athena:DeleteNamedQuery
```

