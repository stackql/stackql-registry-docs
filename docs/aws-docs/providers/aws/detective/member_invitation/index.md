---
title: member_invitation
hide_title: false
hide_table_of_contents: false
keywords:
  - member_invitation
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

Gets or operates on an individual <code>member_invitation</code> resource, use <code>member_invitations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>member_invitation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Detective::MemberInvitation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.detective.member_invitation" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="graph_arn" /></td><td><code>string</code></td><td>The ARN of the graph to which the member account will be invited</td></tr>
<tr><td><CopyableCode code="member_id" /></td><td><code>string</code></td><td>The AWS account ID to be invited to join the graph as a member</td></tr>
<tr><td><CopyableCode code="member_email_address" /></td><td><code>string</code></td><td>The root email address for the account to be invited, for validation. Updating this field has no effect.</td></tr>
<tr><td><CopyableCode code="disable_email_notification" /></td><td><code>boolean</code></td><td>When set to true, invitation emails are not sent to the member accounts. Member accounts must still accept the invitation before they are added to the behavior graph. Updating this field has no effect.</td></tr>
<tr><td><CopyableCode code="message" /></td><td><code>string</code></td><td>A message to be included in the email invitation sent to the invited account. Updating this field has no effect.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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

## `SELECT` Example
```sql
SELECT
region,
graph_arn,
member_id,
member_email_address,
disable_email_notification,
message
FROM aws.detective.member_invitation
WHERE data__Identifier = '<GraphArn>|<MemberId>';
```

## Permissions

To operate on the <code>member_invitation</code> resource, the following permissions are required:

### Read
```json
detective:GetMembers
```

### Delete
```json
detective:DeleteMembers
```

