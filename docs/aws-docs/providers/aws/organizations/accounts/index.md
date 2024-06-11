---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - organizations
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

Creates, updates, deletes or gets an <code>account</code> resource or lists <code>accounts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>You can use AWS::Organizations::Account to manage accounts in organization.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.organizations.accounts" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_name" /></td><td><code>string</code></td><td>The friendly name of the member account.</td></tr>
<tr><td><CopyableCode code="email" /></td><td><code>string</code></td><td>The email address of the owner to assign to the new member account.</td></tr>
<tr><td><CopyableCode code="role_name" /></td><td><code>string</code></td><td>The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. Default name is OrganizationAccountAccessRole if not specified.</td></tr>
<tr><td><CopyableCode code="parent_ids" /></td><td><code>array</code></td><td>List of parent nodes for the member account. Currently only one parent at a time is supported. Default is root.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value.</td></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>If the account was created successfully, the unique identifier (ID) of the new account.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the account.</td></tr>
<tr><td><CopyableCode code="joined_method" /></td><td><code>string</code></td><td>The method by which the account joined the organization.</td></tr>
<tr><td><CopyableCode code="joined_timestamp" /></td><td><code>string</code></td><td>The date the account became a part of the organization.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the account in the organization.</td></tr>
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
    <td><CopyableCode code="AccountName, Email, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>accounts</code> in a region.
```sql
SELECT
region,
account_id
FROM aws.organizations.accounts
WHERE region = 'us-east-1';
```
Gets all properties from an <code>account</code>.
```sql
SELECT
region,
account_name,
email,
role_name,
parent_ids,
tags,
account_id,
arn,
joined_method,
joined_timestamp,
status
FROM aws.organizations.accounts
WHERE region = 'us-east-1' AND data__Identifier = '<AccountId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>account</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.organizations.accounts (
 AccountName,
 Email,
 region
)
SELECT 
'{{ AccountName }}',
 '{{ Email }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.organizations.accounts (
 AccountName,
 Email,
 RoleName,
 ParentIds,
 Tags,
 region
)
SELECT 
 '{{ AccountName }}',
 '{{ Email }}',
 '{{ RoleName }}',
 '{{ ParentIds }}',
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
  - name: account
    props:
      - name: AccountName
        value: '{{ AccountName }}'
      - name: Email
        value: '{{ Email }}'
      - name: RoleName
        value: '{{ RoleName }}'
      - name: ParentIds
        value:
          - '{{ ParentIds[0] }}'
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
DELETE FROM aws.organizations.accounts
WHERE data__Identifier = '<AccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>accounts</code> resource, the following permissions are required:

### Create
```json
organizations:CreateAccount,
organizations:DescribeCreateAccountStatus,
organizations:MoveAccount,
organizations:ListParents,
organizations:TagResource,
organizations:DescribeAccount,
organizations:ListTagsForResource
```

### Read
```json
organizations:DescribeAccount,
organizations:ListParents,
organizations:ListTagsForResource
```

### Update
```json
organizations:MoveAccount,
organizations:TagResource,
organizations:UntagResource,
organizations:ListRoots,
organizations:DescribeAccount,
organizations:ListParents,
organizations:ListTagsForResource
```

### Delete
```json
organizations:CloseAccount
```

### List
```json
organizations:ListAccounts
```

