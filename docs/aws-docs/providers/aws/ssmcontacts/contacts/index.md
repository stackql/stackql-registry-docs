---
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
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


Used to retrieve a list of <code>contacts</code> in a region or to create or delete a <code>contacts</code> resource, use <code>contact</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSMContacts::Contact</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmcontacts.contacts" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the contact.</td></tr>
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
FROM aws.ssmcontacts.contacts
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
 "Alias": "{{ Alias }}",
 "DisplayName": "{{ DisplayName }}",
 "Type": "{{ Type }}"
}
>>>
--required properties only
INSERT INTO aws.ssmcontacts.contacts (
 Alias,
 DisplayName,
 Type,
 region
)
SELECT 
{{ .Alias }},
 {{ .DisplayName }},
 {{ .Type }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Alias": "{{ Alias }}",
 "DisplayName": "{{ DisplayName }}",
 "Type": "{{ Type }}",
 "Plan": [
  {
   "DurationInMinutes": "{{ DurationInMinutes }}",
   "Targets": [
    {
     "ContactTargetInfo": {
      "ContactId": "{{ ContactId }}",
      "IsEssential": "{{ IsEssential }}"
     },
     "ChannelTargetInfo": {
      "ChannelId": "{{ ChannelId }}",
      "RetryIntervalInMinutes": "{{ RetryIntervalInMinutes }}"
     }
    }
   ]
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ssmcontacts.contacts (
 Alias,
 DisplayName,
 Type,
 Plan,
 region
)
SELECT 
 {{ .Alias }},
 {{ .DisplayName }},
 {{ .Type }},
 {{ .Plan }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ssmcontacts.contacts
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>contacts</code> resource, the following permissions are required:

### Create
```json
ssm-contacts:CreateContact,
ssm-contacts:GetContact,
ssm-contacts:AssociateContact
```

### Delete
```json
ssm-contacts:DeleteContact,
ssm-contacts:GetContact,
ssm-contacts:AssociateContact
```

### List
```json
ssm-contacts:ListContacts
```

