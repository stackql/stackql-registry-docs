---
title: member_invitations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - member_invitations_list_only
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

Lists <code>member_invitations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/member_invitations/"><code>member_invitations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>member_invitations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Detective::MemberInvitation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.detective.member_invitations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="graph_arn" /></td><td><code>string</code></td><td>The ARN of the graph to which the member account will be invited</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>member_invitations</code> in a region.
```sql
SELECT
region,
graph_arn,
member_id
FROM aws.detective.member_invitations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>member_invitations_list_only</code> resource, see <a href="/providers/aws/detective/member_invitations/#permissions"><code>member_invitations</code></a>


