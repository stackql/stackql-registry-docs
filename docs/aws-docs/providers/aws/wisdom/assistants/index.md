---
title: assistants
hide_title: false
hide_table_of_contents: false
keywords:
  - assistants
  - wisdom
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


Used to retrieve a list of <code>assistants</code> in a region or to create or delete a <code>assistants</code> resource, use <code>assistant</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assistants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Wisdom::Assistant Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wisdom.assistants" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="assistant_id" /></td><td><code>string</code></td><td></td></tr>
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
assistant_id
FROM aws.wisdom.assistants
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
 "Type": "{{ Type }}",
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.wisdom.assistants (
 Type,
 Name,
 region
)
SELECT 
{{ .Type }},
 {{ .Name }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Type": "{{ Type }}",
 "Description": "{{ Description }}",
 "ServerSideEncryptionConfiguration": {
  "KmsKeyId": "{{ KmsKeyId }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "Name": "{{ Name }}"
}
>>>
--all properties
INSERT INTO aws.wisdom.assistants (
 Type,
 Description,
 ServerSideEncryptionConfiguration,
 Tags,
 Name,
 region
)
SELECT 
 {{ .Type }},
 {{ .Description }},
 {{ .ServerSideEncryptionConfiguration }},
 {{ .Tags }},
 {{ .Name }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.wisdom.assistants
WHERE data__Identifier = '<AssistantId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>assistants</code> resource, the following permissions are required:

### Create
```json
kms:CreateGrant,
kms:DescribeKey,
wisdom:CreateAssistant,
wisdom:TagResource
```

### List
```json
wisdom:ListAssistants
```

### Delete
```json
wisdom:DeleteAssistant
```

