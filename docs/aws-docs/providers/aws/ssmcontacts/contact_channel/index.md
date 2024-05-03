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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>contact_channel</code> resource, use <code>contact_channels</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSMContacts::ContactChannel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmcontacts.contact_channel" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="contact_id" /></td><td><code>string</code></td><td>ARN of the contact resource</td></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td>The device name. String of 6 to 50 alphabetical, numeric, dash, and underscore characters.</td></tr>
<tr><td><CopyableCode code="channel_type" /></td><td><code>string</code></td><td>Device type, which specify notification channel. Currently supported values: “SMS”, “VOICE”, “EMAIL”, “CHATBOT.</td></tr>
<tr><td><CopyableCode code="defer_activation" /></td><td><code>boolean</code></td><td>If you want to activate the channel at a later time, you can choose to defer activation. SSM Incident Manager can't engage your contact channel until it has been activated.</td></tr>
<tr><td><CopyableCode code="channel_address" /></td><td><code>string</code></td><td>The details that SSM Incident Manager uses when trying to engage the contact channel.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the engagement to a contact channel.</td></tr>
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
contact_id,
channel_name,
channel_type,
defer_activation,
channel_address,
arn
FROM aws.ssmcontacts.contact_channel
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

