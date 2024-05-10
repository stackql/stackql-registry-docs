---
title: contact_channels
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_channels
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>contact_channels</code> in a region or to create or delete a <code>contact_channels</code> resource, use <code>contact_channel</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSMContacts::ContactChannel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmcontacts.contact_channels" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.ssmcontacts.contact_channels
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "ContactId": "{{ ContactId }}",
 "ChannelName": "{{ ChannelName }}",
 "ChannelType": "{{ ChannelType }}",
 "DeferActivation": "{{ DeferActivation }}",
 "ChannelAddress": "{{ ChannelAddress }}"
}
>>>
--required properties only
INSERT INTO aws.ssmcontacts.contact_channels (
 ContactId,
 ChannelName,
 ChannelType,
 DeferActivation,
 ChannelAddress,
 region
)
SELECT 
{{ ContactId }},
 {{ ChannelName }},
 {{ ChannelType }},
 {{ DeferActivation }},
 {{ ChannelAddress }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ContactId": "{{ ContactId }}",
 "ChannelName": "{{ ChannelName }}",
 "ChannelType": "{{ ChannelType }}",
 "DeferActivation": "{{ DeferActivation }}",
 "ChannelAddress": "{{ ChannelAddress }}"
}
>>>
--all properties
INSERT INTO aws.ssmcontacts.contact_channels (
 ContactId,
 ChannelName,
 ChannelType,
 DeferActivation,
 ChannelAddress,
 region
)
SELECT 
 {{ ContactId }},
 {{ ChannelName }},
 {{ ChannelType }},
 {{ DeferActivation }},
 {{ ChannelAddress }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ssmcontacts.contact_channels
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>contact_channels</code> resource, the following permissions are required:

### Create
```json
ssm-contacts:CreateContactChannel,
ssm-contacts:GetContactChannel
```

### Delete
```json
ssm-contacts:DeleteContactChannel,
ssm-contacts:GetContactChannel
```

### List
```json
ssm-contacts:ListContactChannels
```

