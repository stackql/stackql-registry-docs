---
title: member_invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - member_invitations
  - detective
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


Used to retrieve a list of <code>member_invitations</code> in a region or to create or delete a <code>member_invitations</code> resource, use <code>member_invitation</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>member_invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Detective::MemberInvitation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.detective.member_invitations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="graph_arn" /></td><td><code>string</code></td><td>The ARN of the graph to which the member account will be invited</td></tr>
<tr><td><CopyableCode code="member_id" /></td><td><code>string</code></td><td>The AWS account ID to be invited to join the graph as a member</td></tr>
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
    <td><CopyableCode code="GraphArn, MemberId, MemberEmailAddress, region" /></td>
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
graph_arn,
member_id
FROM aws.detective.member_invitations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>member_invitation</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.detective.member_invitations (
 GraphArn,
 MemberId,
 MemberEmailAddress,
 region
)
SELECT 
'{{ GraphArn }}',
 '{{ MemberId }}',
 '{{ MemberEmailAddress }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.detective.member_invitations (
 GraphArn,
 MemberId,
 MemberEmailAddress,
 DisableEmailNotification,
 Message,
 region
)
SELECT 
 '{{ GraphArn }}',
 '{{ MemberId }}',
 '{{ MemberEmailAddress }}',
 '{{ DisableEmailNotification }}',
 '{{ Message }}',
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
  - name: member_invitation
    props:
      - name: GraphArn
        value: '{{ GraphArn }}'
      - name: MemberId
        value: '{{ MemberId }}'
      - name: MemberEmailAddress
        value: '{{ MemberEmailAddress }}'
      - name: DisableEmailNotification
        value: '{{ DisableEmailNotification }}'
      - name: Message
        value: '{{ Message }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.detective.member_invitations
WHERE data__Identifier = '<GraphArn|MemberId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>member_invitations</code> resource, the following permissions are required:

### Create
```json
detective:CreateMembers,
detective:GetMembers
```

### Delete
```json
detective:DeleteMembers
```

### List
```json
detective:ListGraphs,
detective:ListMembers
```

