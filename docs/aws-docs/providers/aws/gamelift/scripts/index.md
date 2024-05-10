---
title: scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - scripts
  - gamelift
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


Used to retrieve a list of <code>scripts</code> in a region or to create or delete a <code>scripts</code> resource, use <code>script</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scripts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::Script resource creates a new script record for your Realtime Servers script. Realtime scripts are JavaScript that provide configuration settings and optional custom game logic for your game. The script is deployed when you create a Realtime Servers fleet to host your game sessions. Script logic is executed during an active game session.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.scripts" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>A unique identifier for the Realtime script</td></tr>
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
id
FROM aws.gamelift.scripts
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>script</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- script.iql (required properties only)
INSERT INTO aws.gamelift.scripts (
 StorageLocation,
 region
)
SELECT 
'{{ StorageLocation }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- script.iql (all properties)
INSERT INTO aws.gamelift.scripts (
 Name,
 StorageLocation,
 Version,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ StorageLocation }}',
 '{{ Version }}',
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
  - name: script
    props:
      - name: Name
        value: '{{ Name }}'
      - name: StorageLocation
        value:
          Bucket: '{{ Bucket }}'
          Key: '{{ Key }}'
          ObjectVersion: '{{ ObjectVersion }}'
          RoleArn: '{{ RoleArn }}'
      - name: Version
        value: '{{ Version }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.gamelift.scripts
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>scripts</code> resource, the following permissions are required:

### Create
```json
gamelift:CreateScript,
gamelift:ListTagsForResource,
gamelift:TagResource,
gamelift:DescribeScript,
iam:PassRole
```

### Delete
```json
gamelift:DeleteScript
```

### List
```json
gamelift:ListScripts,
gamelift:DescribeScript
```

