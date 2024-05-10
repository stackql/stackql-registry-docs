---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - guardduty
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


Used to retrieve a list of <code>members</code> in a region or to create or delete a <code>members</code> resource, use <code>member</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GuardDuty::Member</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.guardduty.members" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="detector_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="member_id" /></td><td><code>string</code></td><td></td></tr>
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
detector_id,
member_id
FROM aws.guardduty.members
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>member</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- member.iql (required properties only)
INSERT INTO aws.guardduty.members (
 Email,
 region
)
SELECT 
'{{ Email }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- member.iql (all properties)
INSERT INTO aws.guardduty.members (
 Status,
 MemberId,
 Email,
 Message,
 DisableEmailNotification,
 DetectorId,
 region
)
SELECT 
 '{{ Status }}',
 '{{ MemberId }}',
 '{{ Email }}',
 '{{ Message }}',
 '{{ DisableEmailNotification }}',
 '{{ DetectorId }}',
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
  - name: member
    props:
      - name: Status
        value: '{{ Status }}'
      - name: MemberId
        value: '{{ MemberId }}'
      - name: Email
        value: '{{ Email }}'
      - name: Message
        value: '{{ Message }}'
      - name: DisableEmailNotification
        value: '{{ DisableEmailNotification }}'
      - name: DetectorId
        value: '{{ DetectorId }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.guardduty.members
WHERE data__Identifier = '<DetectorId|MemberId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>members</code> resource, the following permissions are required:

### Create
```json
guardduty:CreateMembers,
guardduty:GetMembers
```

### Delete
```json
guardduty:GetMembers,
guardduty:DisassociateMembers,
guardduty:DeleteMembers
```

### List
```json
guardduty:ListMembers
```

