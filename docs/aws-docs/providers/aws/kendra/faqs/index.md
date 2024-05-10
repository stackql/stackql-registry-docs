---
title: faqs
hide_title: false
hide_table_of_contents: false
keywords:
  - faqs
  - kendra
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


Used to retrieve a list of <code>faqs</code> in a region or to create or delete a <code>faqs</code> resource, use <code>faq</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>faqs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A Kendra FAQ resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kendra.faqs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="index_id" /></td><td><code>undefined</code></td><td>Index ID</td></tr>
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
id,
index_id
FROM aws.kendra.faqs
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
 "IndexId": "{{ IndexId }}",
 "Name": "{{ Name }}",
 "S3Path": {
  "Bucket": "{{ Bucket }}",
  "Key": "{{ Key }}"
 },
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.kendra.faqs (
 IndexId,
 Name,
 S3Path,
 RoleArn,
 region
)
SELECT 
{{ .IndexId }},
 {{ .Name }},
 {{ .S3Path }},
 {{ .RoleArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "IndexId": "{{ IndexId }}",
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "FileFormat": "{{ FileFormat }}",
 "S3Path": {
  "Bucket": "{{ Bucket }}",
  "Key": "{{ Key }}"
 },
 "RoleArn": "{{ RoleArn }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "LanguageCode": "{{ LanguageCode }}"
}
>>>
--all properties
INSERT INTO aws.kendra.faqs (
 IndexId,
 Name,
 Description,
 FileFormat,
 S3Path,
 RoleArn,
 Tags,
 LanguageCode,
 region
)
SELECT 
 {{ .IndexId }},
 {{ .Name }},
 {{ .Description }},
 {{ .FileFormat }},
 {{ .S3Path }},
 {{ .RoleArn }},
 {{ .Tags }},
 {{ .LanguageCode }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.kendra.faqs
WHERE data__Identifier = '<Id|IndexId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>faqs</code> resource, the following permissions are required:

### Create
```json
kendra:CreateFaq,
kendra:DescribeFaq,
iam:PassRole,
kendra:ListTagsForResource,
kendra:TagResource
```

### Delete
```json
kendra:DeleteFaq,
kendra:DescribeFaq
```

### List
```json
kendra:ListFaqs
```

