---
title: user_pool_users
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_users
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

Creates, updates, deletes or gets an <code>user_pool_user</code> resource or lists <code>user_pool_users</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolUser</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_users" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="desired_delivery_mediums" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="force_alias_creation" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="user_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="message_action" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="username" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="validation_data" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="client_metadata" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="UserPoolId, region" /></td>
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
Gets all <code>user_pool_users</code> in a region.
```sql
SELECT
region,
desired_delivery_mediums,
force_alias_creation,
user_attributes,
message_action,
username,
user_pool_id,
validation_data,
client_metadata
FROM aws.cognito.user_pool_users
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>user_pool_user</code>.
```sql
SELECT
region,
desired_delivery_mediums,
force_alias_creation,
user_attributes,
message_action,
username,
user_pool_id,
validation_data,
client_metadata
FROM aws.cognito.user_pool_users
WHERE region = 'us-east-1' AND data__Identifier = '<UserPoolId>|<Username>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_pool_user</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cognito.user_pool_users (
 UserPoolId,
 region
)
SELECT 
'{{ UserPoolId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cognito.user_pool_users (
 DesiredDeliveryMediums,
 ForceAliasCreation,
 UserAttributes,
 MessageAction,
 Username,
 UserPoolId,
 ValidationData,
 ClientMetadata,
 region
)
SELECT 
 '{{ DesiredDeliveryMediums }}',
 '{{ ForceAliasCreation }}',
 '{{ UserAttributes }}',
 '{{ MessageAction }}',
 '{{ Username }}',
 '{{ UserPoolId }}',
 '{{ ValidationData }}',
 '{{ ClientMetadata }}',
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
  - name: user_pool_user
    props:
      - name: DesiredDeliveryMediums
        value:
          - '{{ DesiredDeliveryMediums[0] }}'
      - name: ForceAliasCreation
        value: '{{ ForceAliasCreation }}'
      - name: UserAttributes
        value:
          - Name: '{{ Name }}'
            Value: '{{ Value }}'
      - name: MessageAction
        value: '{{ MessageAction }}'
      - name: Username
        value: '{{ Username }}'
      - name: UserPoolId
        value: '{{ UserPoolId }}'
      - name: ValidationData
        value:
          - null
      - name: ClientMetadata
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cognito.user_pool_users
WHERE data__Identifier = '<UserPoolId|Username>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_pool_users</code> resource, the following permissions are required:

### Create
```json
cognito-idp:AdminCreateUser,
cognito-idp:AdminGetUser,
iam:PassRole
```

### Read
```json
cognito-idp:AdminGetUser
```

### Delete
```json
cognito-idp:AdminDeleteUser
```

### List
```json
cognito-idp:ListUsers
```

