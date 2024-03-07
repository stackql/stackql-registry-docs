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
Gets an individual <code>member_invitation</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>member_invitation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>member_invitation</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.detective.member_invitation</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>graph_arn</code></td><td><code>string</code></td><td>The ARN of the graph to which the member account will be invited</td></tr>
<tr><td><code>member_id</code></td><td><code>string</code></td><td>The AWS account ID to be invited to join the graph as a member</td></tr>
<tr><td><code>member_email_address</code></td><td><code>string</code></td><td>The root email address for the account to be invited, for validation. Updating this field has no effect.</td></tr>
<tr><td><code>disable_email_notification</code></td><td><code>boolean</code></td><td>When set to true, invitation emails are not sent to the member accounts. Member accounts must still accept the invitation before they are added to the behavior graph. Updating this field has no effect.</td></tr>
<tr><td><code>message</code></td><td><code>string</code></td><td>A message to be included in the email invitation sent to the invited account. Updating this field has no effect.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>member_invitation</code> resource, the following permissions are required:

### Read
<pre>
detective:GetMembers</pre>

### Update
<pre>
</pre>

### Delete
<pre>
detective:DeleteMembers</pre>


## Example
```sql
SELECT
region,
graph_arn,
member_id,
member_email_address,
disable_email_notification,
message
FROM awscc.detective.member_invitation
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;GraphArn&gt;'
AND data__Identifier = '&lt;MemberId&gt;'
```
