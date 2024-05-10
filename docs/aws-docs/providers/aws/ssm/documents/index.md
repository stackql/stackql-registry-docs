---
title: documents
hide_title: false
hide_table_of_contents: false
keywords:
  - documents
  - ssm
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


Used to retrieve a list of <code>documents</code> in a region or to create or delete a <code>documents</code> resource, use <code>document</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SSM::Document resource is an SSM document in AWS Systems Manager that defines the actions that Systems Manager performs, which can be used to set up and run commands on your instances.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.documents" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the Systems Manager document.</td></tr>
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
name
FROM aws.ssm.documents
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
 "Content": {}
}
>>>
--required properties only
INSERT INTO aws.ssm.documents (
 Content,
 region
)
SELECT 
{{ Content }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Content": {},
 "Attachments": [
  {
   "Key": "{{ Key }}",
   "Values": [
    "{{ Values[0] }}"
   ],
   "Name": "{{ Name }}"
  }
 ],
 "Name": "{{ Name }}",
 "VersionName": "{{ VersionName }}",
 "DocumentType": "{{ DocumentType }}",
 "DocumentFormat": "{{ DocumentFormat }}",
 "TargetType": "{{ TargetType }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "Requires": [
  {
   "Name": "{{ Name }}",
   "Version": "{{ Version }}"
  }
 ],
 "UpdateMethod": "{{ UpdateMethod }}"
}
>>>
--all properties
INSERT INTO aws.ssm.documents (
 Content,
 Attachments,
 Name,
 VersionName,
 DocumentType,
 DocumentFormat,
 TargetType,
 Tags,
 Requires,
 UpdateMethod,
 region
)
SELECT 
 {{ Content }},
 {{ Attachments }},
 {{ Name }},
 {{ VersionName }},
 {{ DocumentType }},
 {{ DocumentFormat }},
 {{ TargetType }},
 {{ Tags }},
 {{ Requires }},
 {{ UpdateMethod }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ssm.documents
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>documents</code> resource, the following permissions are required:

### Create
```json
ssm:CreateDocument,
ssm:GetDocument,
ssm:AddTagsToResource,
ssm:ListTagsForResource,
s3:GetObject,
iam:PassRole
```

### Delete
```json
ssm:DeleteDocument,
ssm:GetDocument
```

### List
```json
ssm:ListDocuments
```

