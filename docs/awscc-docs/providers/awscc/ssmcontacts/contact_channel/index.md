---
title: contact_channel
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_channel
  - ssmcontacts
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>contact_channel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>contact_channel</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ssmcontacts.contact_channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>contact_id</code></td><td><code>string</code></td><td>ARN of the contact resource</td></tr>
<tr><td><code>channel_name</code></td><td><code>string</code></td><td>The device name. String of 6 to 50 alphabetical, numeric, dash, and underscore characters.</td></tr>
<tr><td><code>channel_type</code></td><td><code>string</code></td><td>Device type, which specify notification channel. Currently supported values: “SMS”, “VOICE”, “EMAIL”, “CHATBOT.</td></tr>
<tr><td><code>defer_activation</code></td><td><code>boolean</code></td><td>If you want to activate the channel at a later time, you can choose to defer activation. SSM Incident Manager can't engage your contact channel until it has been activated.</td></tr>
<tr><td><code>channel_address</code></td><td><code>string</code></td><td>The details that SSM Incident Manager uses when trying to engage the contact channel.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the engagement to a contact channel.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
contact_id,
channel_name,
channel_type,
defer_activation,
channel_address,
arn
FROM awscc.ssmcontacts.contact_channel
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>contact_channel</code> resource, the following permissions are required:

### Read
```json
ssm-contacts:GetContactChannel
```

### Update
```json
ssm-contacts:UpdateContactChannel,
ssm-contacts:GetContactChannel
```

### Delete
```json
ssm-contacts:DeleteContactChannel,
ssm-contacts:GetContactChannel
```

