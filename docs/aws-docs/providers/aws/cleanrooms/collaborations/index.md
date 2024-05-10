---
title: collaborations
hide_title: false
hide_table_of_contents: false
keywords:
  - collaborations
  - cleanrooms
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


Used to retrieve a list of <code>collaborations</code> in a region or to create or delete a <code>collaborations</code> resource, use <code>collaboration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collaborations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a collaboration between AWS accounts that allows for secure data collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.collaborations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="collaboration_identifier" /></td><td><code>string</code></td><td></td></tr>
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
collaboration_identifier
FROM aws.cleanrooms.collaborations
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
 "CreatorDisplayName": "{{ CreatorDisplayName }}",
 "CreatorMemberAbilities": [
  "{{ CreatorMemberAbilities[0] }}"
 ],
 "Description": "{{ Description }}",
 "Members": [
  {
   "AccountId": "{{ AccountId }}",
   "MemberAbilities": null,
   "DisplayName": null,
   "PaymentConfiguration": {
    "QueryCompute": {
     "IsResponsible": "{{ IsResponsible }}"
    }
   }
  }
 ],
 "Name": "{{ Name }}",
 "QueryLogStatus": "{{ QueryLogStatus }}"
}
>>>
--required properties only
INSERT INTO aws.cleanrooms.collaborations (
 CreatorDisplayName,
 CreatorMemberAbilities,
 Description,
 Members,
 Name,
 QueryLogStatus,
 region
)
SELECT 
{{ CreatorDisplayName }},
 {{ CreatorMemberAbilities }},
 {{ Description }},
 {{ Members }},
 {{ Name }},
 {{ QueryLogStatus }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "CreatorDisplayName": "{{ CreatorDisplayName }}",
 "CreatorMemberAbilities": [
  "{{ CreatorMemberAbilities[0] }}"
 ],
 "DataEncryptionMetadata": {
  "AllowCleartext": "{{ AllowCleartext }}",
  "AllowDuplicates": "{{ AllowDuplicates }}",
  "AllowJoinsOnColumnsWithDifferentNames": "{{ AllowJoinsOnColumnsWithDifferentNames }}",
  "PreserveNulls": "{{ PreserveNulls }}"
 },
 "Description": "{{ Description }}",
 "Members": [
  {
   "AccountId": "{{ AccountId }}",
   "MemberAbilities": null,
   "DisplayName": null,
   "PaymentConfiguration": {
    "QueryCompute": {
     "IsResponsible": "{{ IsResponsible }}"
    }
   }
  }
 ],
 "Name": "{{ Name }}",
 "QueryLogStatus": "{{ QueryLogStatus }}",
 "CreatorPaymentConfiguration": null
}
>>>
--all properties
INSERT INTO aws.cleanrooms.collaborations (
 Tags,
 CreatorDisplayName,
 CreatorMemberAbilities,
 DataEncryptionMetadata,
 Description,
 Members,
 Name,
 QueryLogStatus,
 CreatorPaymentConfiguration,
 region
)
SELECT 
 {{ Tags }},
 {{ CreatorDisplayName }},
 {{ CreatorMemberAbilities }},
 {{ DataEncryptionMetadata }},
 {{ Description }},
 {{ Members }},
 {{ Name }},
 {{ QueryLogStatus }},
 {{ CreatorPaymentConfiguration }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cleanrooms.collaborations
WHERE data__Identifier = '<CollaborationIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>collaborations</code> resource, the following permissions are required:

### Create
```json
cleanrooms:CreateCollaboration,
cleanrooms:GetCollaboration,
cleanrooms:ListMembers,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:GetCollaboration,
cleanrooms:ListCollaborations
```

### Delete
```json
cleanrooms:DeleteCollaboration,
cleanrooms:GetCollaboration,
cleanrooms:ListTagsForResource,
cleanrooms:UntagResource,
cleanrooms:ListMembers,
cleanrooms:ListCollaborations
```

### List
```json
cleanrooms:ListCollaborations
```

