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

Creates, updates, deletes or gets a <code>member</code> resource or lists <code>members</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GuardDuty::Member</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.guardduty.members" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="member_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="email" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="disable_email_notification" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="detector_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html"><code>AWS::GuardDuty::Member</code></a>.

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
    <td><CopyableCode code="Email, region" /></td>
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
Gets all <code>members</code> in a region.
```sql
SELECT
region,
status,
member_id,
email,
message,
disable_email_notification,
detector_id
FROM aws.guardduty.members
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>member</code>.
```sql
SELECT
region,
status,
member_id,
email,
message,
disable_email_notification,
detector_id
FROM aws.guardduty.members
WHERE region = 'us-east-1' AND data__Identifier = '<DetectorId>|<MemberId>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
guardduty:GetMembers
```

### Delete
```json
guardduty:GetMembers,
guardduty:DisassociateMembers,
guardduty:DeleteMembers
```

### Update
```json
guardduty:GetMembers,
guardduty:CreateMembers,
guardduty:DisassociateMembers,
guardduty:StartMonitoringMembers,
guardduty:StopMonitoringMembers,
guardduty:InviteMembers
```

### List
```json
guardduty:ListMembers
```
