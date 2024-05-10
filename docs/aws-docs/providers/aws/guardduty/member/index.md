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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>member</code> resource, use <code>members</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>member</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GuardDuty::Member</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.guardduty.member" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="member_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="email" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="disable_email_notification" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="detector_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
status,
member_id,
email,
message,
disable_email_notification,
detector_id
FROM aws.guardduty.member
WHERE region = 'us-east-1' AND data__Identifier = '<DetectorId>|<MemberId>';
```


## Permissions

To operate on the <code>member</code> resource, the following permissions are required:

### Read
```json
guardduty:GetMembers
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

