---
title: contact_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_lists
  - ses
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


Used to retrieve a list of <code>contact_lists</code> in a region or to create or delete a <code>contact_lists</code> resource, use <code>contact_list</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SES::ContactList.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.contact_lists" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="contact_list_name" /></td><td><code>string</code></td><td>The name of the contact list.</td></tr>
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
contact_list_name
FROM aws.ses.contact_lists
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
 "ContactListName": "{{ ContactListName }}",
 "Description": "{{ Description }}",
 "Topics": [
  {
   "TopicName": "{{ TopicName }}",
   "DisplayName": "{{ DisplayName }}",
   "Description": "{{ Description }}",
   "DefaultSubscriptionStatus": "{{ DefaultSubscriptionStatus }}"
  }
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.ses.contact_lists (
 ContactListName,
 Description,
 Topics,
 Tags,
 region
)
SELECT 
{{ ContactListName }},
 {{ Description }},
 {{ Topics }},
 {{ Tags }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ContactListName": "{{ ContactListName }}",
 "Description": "{{ Description }}",
 "Topics": [
  {
   "TopicName": "{{ TopicName }}",
   "DisplayName": "{{ DisplayName }}",
   "Description": "{{ Description }}",
   "DefaultSubscriptionStatus": "{{ DefaultSubscriptionStatus }}"
  }
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ses.contact_lists (
 ContactListName,
 Description,
 Topics,
 Tags,
 region
)
SELECT 
 {{ ContactListName }},
 {{ Description }},
 {{ Topics }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ses.contact_lists
WHERE data__Identifier = '<ContactListName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>contact_lists</code> resource, the following permissions are required:

### Create
```json
ses:CreateContactList
```

### Delete
```json
ses:DeleteContactList
```

### List
```json
ses:ListContactLists
```

