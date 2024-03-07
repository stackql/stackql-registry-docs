---
title: member
hide_title: false
hide_table_of_contents: false
keywords:
  - member
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
Gets an individual <code>member</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>member</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>member</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.guardduty.member</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>member_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>email</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>message</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>disable_email_notification</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>detector_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>member</code> resource, the following permissions are required:

### Read
<pre>
guardduty:GetMembers</pre>

### Delete
<pre>
guardduty:GetMembers,
guardduty:DisassociateMembers,
guardduty:DeleteMembers</pre>

### Update
<pre>
guardduty:GetMembers,
guardduty:CreateMembers,
guardduty:DisassociateMembers,
guardduty:StartMonitoringMembers,
guardduty:StopMonitoringMembers,
guardduty:InviteMembers</pre>


## Example
```sql
SELECT
region,
status,
member_id,
email,
message,
disable_email_notification,
detector_id
FROM awscc.guardduty.member
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DetectorId&gt;'
AND data__Identifier = '&lt;MemberId&gt;'
```
