---
title: user_pool_resource_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_resource_servers
  - cognito
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

Creates, updates, deletes or gets an <code>user_pool_resource_server</code> resource or lists <code>user_pool_resource_servers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_resource_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolResourceServer</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_resource_servers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="scopes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolresourceserver.html"><code>AWS::Cognito::UserPoolResourceServer</code></a>.

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
    <td><CopyableCode code="UserPoolId, Identifier, Name, region" /></td>
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
Gets all <code>user_pool_resource_servers</code> in a region.
```sql
SELECT
region,
user_pool_id,
identifier,
name,
scopes
FROM aws.cognito.user_pool_resource_servers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>user_pool_resource_server</code>.
```sql
SELECT
region,
user_pool_id,
identifier,
name,
scopes
FROM aws.cognito.user_pool_resource_servers
WHERE region = 'us-east-1' AND data__Identifier = '<UserPoolId>|<Identifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_pool_resource_server</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cognito.user_pool_resource_servers (
 UserPoolId,
 Identifier,
 Name,
 region
)
SELECT 
'{{ UserPoolId }}',
 '{{ Identifier }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cognito.user_pool_resource_servers (
 UserPoolId,
 Identifier,
 Name,
 Scopes,
 region
)
SELECT 
 '{{ UserPoolId }}',
 '{{ Identifier }}',
 '{{ Name }}',
 '{{ Scopes }}',
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
  - name: user_pool_resource_server
    props:
      - name: UserPoolId
        value: '{{ UserPoolId }}'
      - name: Identifier
        value: '{{ Identifier }}'
      - name: Name
        value: '{{ Name }}'
      - name: Scopes
        value:
          - ScopeDescription: '{{ ScopeDescription }}'
            ScopeName: '{{ ScopeName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cognito.user_pool_resource_servers
WHERE data__Identifier = '<UserPoolId|Identifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_pool_resource_servers</code> resource, the following permissions are required:

### Create
```json
cognito-idp:CreateResourceServer
```

### Read
```json
cognito-idp:DescribeResourceServer
```

### Update
```json
cognito-idp:UpdateResourceServer
```

### Delete
```json
cognito-idp:DeleteResourceServer
```

### List
```json
cognito-idp:ListResourceServers
```
