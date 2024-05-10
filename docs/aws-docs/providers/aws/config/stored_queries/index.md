---
title: stored_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - stored_queries
  - config
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


Used to retrieve a list of <code>stored_queries</code> in a region or to create or delete a <code>stored_queries</code> resource, use <code>stored_query</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stored_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Config::StoredQuery</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.stored_queries" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="query_name" /></td><td><code>string</code></td><td></td></tr>
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
query_name
FROM aws.config.stored_queries
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>stored_query</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- stored_query.iql (required properties only)
INSERT INTO aws.config.stored_queries (
 QueryName,
 QueryExpression,
 region
)
SELECT 
'{{ QueryName }}',
 '{{ QueryExpression }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- stored_query.iql (all properties)
INSERT INTO aws.config.stored_queries (
 QueryName,
 QueryDescription,
 QueryExpression,
 Tags,
 region
)
SELECT 
 '{{ QueryName }}',
 '{{ QueryDescription }}',
 '{{ QueryExpression }}',
 '{{ Tags }}',
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
  - name: stored_query
    props:
      - name: QueryName
        value: '{{ QueryName }}'
      - name: QueryDescription
        value: '{{ QueryDescription }}'
      - name: QueryExpression
        value: '{{ QueryExpression }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.config.stored_queries
WHERE data__Identifier = '<QueryName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>stored_queries</code> resource, the following permissions are required:

### Create
```json
config:PutStoredQuery,
config:GetStoredQuery,
config:TagResource
```

### Delete
```json
config:DeleteStoredQuery,
config:UntagResource
```

### List
```json
config:ListStoredQueries
```

