---
title: query_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - query_definitions
  - logs
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

Creates, updates, deletes or gets a <code>query_definition</code> resource or lists <code>query_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>query_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The resource schema for AWSLogs QueryDefinition</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.query_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the saved query definition</td></tr>
<tr><td><CopyableCode code="query_string" /></td><td><code>string</code></td><td>The query string to use for this definition</td></tr>
<tr><td><CopyableCode code="log_group_names" /></td><td><code>array</code></td><td>Optionally define specific log groups as part of your query definition</td></tr>
<tr><td><CopyableCode code="query_definition_id" /></td><td><code>string</code></td><td>Unique identifier of a query definition</td></tr>
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
    <td><CopyableCode code="Name, QueryString, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
Gets all <code>query_definitions</code> in a region.
```sql
SELECT
region,
name,
query_string,
log_group_names,
query_definition_id
FROM aws.logs.query_definitions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>query_definition</code>.
```sql
SELECT
region,
name,
query_string,
log_group_names,
query_definition_id
FROM aws.logs.query_definitions
WHERE region = 'us-east-1' AND data__Identifier = '<QueryDefinitionId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>query_definition</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.logs.query_definitions (
 Name,
 QueryString,
 region
)
SELECT 
'{{ Name }}',
 '{{ QueryString }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.logs.query_definitions (
 Name,
 QueryString,
 LogGroupNames,
 region
)
SELECT 
 '{{ Name }}',
 '{{ QueryString }}',
 '{{ LogGroupNames }}',
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
  - name: query_definition
    props:
      - name: Name
        value: '{{ Name }}'
      - name: QueryString
        value: '{{ QueryString }}'
      - name: LogGroupNames
        value:
          - '{{ LogGroupNames[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.logs.query_definitions
WHERE data__Identifier = '<QueryDefinitionId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>query_definitions</code> resource, the following permissions are required:

### Create
```json
logs:PutQueryDefinition
```

### Read
```json
logs:DescribeQueryDefinitions
```

### Update
```json
logs:PutQueryDefinition
```

### Delete
```json
logs:DeleteQueryDefinition
```

### List
```json
logs:DescribeQueryDefinitions
```

