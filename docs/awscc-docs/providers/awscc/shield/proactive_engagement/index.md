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
Gets an individual <code>proactive_engagement</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>proactive_engagement</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>proactive_engagement</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.shield.proactive_engagement</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>proactive_engagement_status</code></td><td><code>string</code></td><td>If `ENABLED`, the Shield Response Team (SRT) will use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.&lt;br&#x2F;&gt;If `DISABLED`, the SRT will not proactively notify contacts about escalations or to initiate proactive customer support.</td></tr>
<tr><td><code>emergency_contact_list</code></td><td><code>array</code></td><td>A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you for escalations to the SRT and to initiate proactive customer support.&lt;br&#x2F;&gt;To enable proactive engagement, the contact list must include at least one phone number.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
account_id,
proactive_engagement_status,
emergency_contact_list
FROM awscc.shield.proactive_engagement
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

