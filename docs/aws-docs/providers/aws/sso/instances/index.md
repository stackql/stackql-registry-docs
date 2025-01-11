---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - sso
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

Creates, updates, deletes or gets an <code>instance</code> resource or lists <code>instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for Identity Center (SSO) Instance</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sso.instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name you want to assign to this Identity Center (SSO) Instance</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The SSO Instance ARN that is returned upon creation of the Identity Center (SSO) Instance</td></tr>
<tr><td><CopyableCode code="owner_account_id" /></td><td><code>string</code></td><td>The AWS accountId of the owner of the Identity Center (SSO) Instance</td></tr>
<tr><td><CopyableCode code="identity_store_id" /></td><td><code>string</code></td><td>The ID of the identity store associated with the created Identity Center (SSO) Instance</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the Identity Center (SSO) Instance, create_in_progress/delete_in_progress/active</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instance.html"><code>AWS::SSO::Instance</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>instances</code> in a region.
```sql
SELECT
region,
name,
instance_arn,
owner_account_id,
identity_store_id,
status,
tags
FROM aws.sso.instances
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>instance</code>.
```sql
SELECT
region,
name,
instance_arn,
owner_account_id,
identity_store_id,
status,
tags
FROM aws.sso.instances
WHERE region = 'us-east-1' AND data__Identifier = '<InstanceArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sso.instances (
 Name,
 Tags,
 region
)
SELECT 
'{{ Name }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sso.instances (
 Name,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
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
  - name: instance
    props:
      - name: Name
        value: '{{ Name }}'
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
DELETE FROM aws.sso.instances
WHERE data__Identifier = '<InstanceArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>instances</code> resource, the following permissions are required:

### Create
```json
sso:CreateInstance,
sso:DescribeInstance,
sso:TagResource,
iam:CreateServiceLinkedRole,
sso:TagInstance,
sso:ListTagsForResource
```

### Read
```json
sso:DescribeInstance,
sso:ListTagsForResource
```

### Update
```json
sso:UpdateInstance,
sso:TagResource,
sso:UntagResource,
sso:ListTagsForResource,
sso:TagInstance,
sso:DescribeInstance
```

### Delete
```json
sso:DeleteInstance
```

### List
```json
sso:ListInstances
```
