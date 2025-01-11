---
title: connection_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_aliases
  - workspaces
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

Creates, updates, deletes or gets a <code>connection_alias</code> resource or lists <code>connection_aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::WorkSpaces::ConnectionAlias</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspaces.connection_aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="associations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="alias_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="connection_string" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="connection_alias_state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html"><code>AWS::WorkSpaces::ConnectionAlias</code></a>.

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
    <td><CopyableCode code="ConnectionString, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>connection_alias</code>.
```sql
SELECT
region,
associations,
alias_id,
connection_string,
connection_alias_state,
tags
FROM aws.workspaces.connection_aliases
WHERE region = 'us-east-1' AND data__Identifier = '<AliasId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connection_alias</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.workspaces.connection_aliases (
 ConnectionString,
 region
)
SELECT 
'{{ ConnectionString }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.workspaces.connection_aliases (
 ConnectionString,
 Tags,
 region
)
SELECT 
 '{{ ConnectionString }}',
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
  - name: connection_alias
    props:
      - name: ConnectionString
        value: '{{ ConnectionString }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.workspaces.connection_aliases
WHERE data__Identifier = '<AliasId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>connection_aliases</code> resource, the following permissions are required:

### Create
```json
workspaces:CreateConnectionAlias
```

### Read
```json
workspaces:DescribeConnectionAliases
```

### Delete
```json
workspaces:DeleteConnectionAlias
```
