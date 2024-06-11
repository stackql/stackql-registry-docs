---
title: user_pool_user_to_group_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_user_to_group_attachments
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

Creates, updates, deletes or gets an <code>user_pool_user_to_group_attachment</code> resource or lists <code>user_pool_user_to_group_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_user_to_group_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolUserToGroupAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_pool_user_to_group_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="username" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="UserPoolId, Username, GroupName, region" /></td>
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

Gets all properties from an <code>user_pool_user_to_group_attachment</code>.
```sql
SELECT
region,
user_pool_id,
username,
group_name
FROM aws.cognito.user_pool_user_to_group_attachments
WHERE region = 'us-east-1' AND data__Identifier = '<UserPoolId>|<GroupName>|<Username>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_pool_user_to_group_attachment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cognito.user_pool_user_to_group_attachments (
 UserPoolId,
 Username,
 GroupName,
 region
)
SELECT 
'{{ UserPoolId }}',
 '{{ Username }}',
 '{{ GroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cognito.user_pool_user_to_group_attachments (
 UserPoolId,
 Username,
 GroupName,
 region
)
SELECT 
 '{{ UserPoolId }}',
 '{{ Username }}',
 '{{ GroupName }}',
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
  - name: user_pool_user_to_group_attachment
    props:
      - name: UserPoolId
        value: '{{ UserPoolId }}'
      - name: Username
        value: '{{ Username }}'
      - name: GroupName
        value: '{{ GroupName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cognito.user_pool_user_to_group_attachments
WHERE data__Identifier = '<UserPoolId|GroupName|Username>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_pool_user_to_group_attachments</code> resource, the following permissions are required:

### Create
```json
cognito-idp:AdminAddUserToGroup,
cognito-idp:AdminListGroupsForUser
```

### Delete
```json
cognito-idp:AdminRemoveUserFromGroup,
cognito-idp:AdminListGroupsForUser
```

### Read
```json
cognito-idp:AdminListGroupsForUser
```

