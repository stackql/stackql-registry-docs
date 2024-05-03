---
title: proactive_engagement
hide_title: false
hide_table_of_contents: false
keywords:
  - proactive_engagement
  - shield
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

Gets or operates on an individual <code>proactive_engagement</code> resource, use <code>proactive_engagements</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>proactive_engagement</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Authorizes the Shield Response Team (SRT) to use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.shield.proactive_engagement" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="proactive_engagement_status" /></td><td><code>string</code></td><td>If `ENABLED`, the Shield Response Team (SRT) will use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.&lt;br&#x2F;&gt;If `DISABLED`, the SRT will not proactively notify contacts about escalations or to initiate proactive customer support.</td></tr>
<tr><td><CopyableCode code="emergency_contact_list" /></td><td><code>array</code></td><td>A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you for escalations to the SRT and to initiate proactive customer support.&lt;br&#x2F;&gt;To enable proactive engagement, the contact list must include at least one phone number.</td></tr>
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
account_id,
proactive_engagement_status,
emergency_contact_list
FROM aws.shield.proactive_engagement
WHERE data__Identifier = '<AccountId>';
```

## Permissions

To operate on the <code>proactive_engagement</code> resource, the following permissions are required:

### Delete
```json
shield:DescribeSubscription,
shield:DescribeEmergencyContactSettings,
shield:UpdateEmergencyContactSettings,
shield:DisableProactiveEngagement
```

### Read
```json
shield:DescribeSubscription,
shield:DescribeEmergencyContactSettings
```

### Update
```json
shield:DescribeSubscription,
shield:DescribeEmergencyContactSettings,
shield:UpdateEmergencyContactSettings,
shield:EnableProactiveEngagement,
shield:DisableProactiveEngagement
```
