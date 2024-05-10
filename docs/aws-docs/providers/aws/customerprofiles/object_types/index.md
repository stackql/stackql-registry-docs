---
title: object_types
hide_title: false
hide_table_of_contents: false
keywords:
  - object_types
  - customerprofiles
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


Used to retrieve a list of <code>object_types</code> in a region or to create or delete a <code>object_types</code> resource, use <code>object_type</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>object_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An ObjectType resource of Amazon Connect Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.object_types" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="object_type_name" /></td><td><code>string</code></td><td>The name of the profile object type.</td></tr>
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
domain_name,
object_type_name
FROM aws.customerprofiles.object_types
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
 "DomainName": "{{ DomainName }}",
 "ObjectTypeName": "{{ ObjectTypeName }}",
 "Description": "{{ Description }}"
}
>>>
--required properties only
INSERT INTO aws.customerprofiles.object_types (
 DomainName,
 ObjectTypeName,
 Description,
 region
)
SELECT 
{{ DomainName }},
 {{ ObjectTypeName }},
 {{ Description }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DomainName": "{{ DomainName }}",
 "ObjectTypeName": "{{ ObjectTypeName }}",
 "AllowProfileCreation": "{{ AllowProfileCreation }}",
 "Description": "{{ Description }}",
 "EncryptionKey": "{{ EncryptionKey }}",
 "ExpirationDays": "{{ ExpirationDays }}",
 "Fields": [
  {
   "Name": "{{ Name }}",
   "ObjectTypeField": {
    "Source": "{{ Source }}",
    "Target": "{{ Target }}",
    "ContentType": "{{ ContentType }}"
   }
  }
 ],
 "Keys": [
  {
   "Name": "{{ Name }}",
   "ObjectTypeKeyList": [
    {
     "FieldNames": [
      "{{ FieldNames[0] }}"
     ],
     "StandardIdentifiers": [
      "{{ StandardIdentifiers[0] }}"
     ]
    }
   ]
  }
 ],
 "SourceLastUpdatedTimestampFormat": "{{ SourceLastUpdatedTimestampFormat }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "TemplateId": "{{ TemplateId }}"
}
>>>
--all properties
INSERT INTO aws.customerprofiles.object_types (
 DomainName,
 ObjectTypeName,
 AllowProfileCreation,
 Description,
 EncryptionKey,
 ExpirationDays,
 Fields,
 Keys,
 SourceLastUpdatedTimestampFormat,
 Tags,
 TemplateId,
 region
)
SELECT 
 {{ DomainName }},
 {{ ObjectTypeName }},
 {{ AllowProfileCreation }},
 {{ Description }},
 {{ EncryptionKey }},
 {{ ExpirationDays }},
 {{ Fields }},
 {{ Keys }},
 {{ SourceLastUpdatedTimestampFormat }},
 {{ Tags }},
 {{ TemplateId }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.customerprofiles.object_types
WHERE data__Identifier = '<DomainName|ObjectTypeName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>object_types</code> resource, the following permissions are required:

### Create
```json
profile:GetProfileObjectType,
profile:PutProfileObjectType,
profile:TagResource
```

### Delete
```json
profile:DeleteProfileObjectType
```

### List
```json
profile:ListProfileObjectTypes
```

