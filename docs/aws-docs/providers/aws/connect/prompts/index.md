---
title: prompts
hide_title: false
hide_table_of_contents: false
keywords:
  - prompts
  - connect
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


Used to retrieve a list of <code>prompts</code> in a region or to create or delete a <code>prompts</code> resource, use <code>prompt</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prompts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::Prompt</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.prompts" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="prompt_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the prompt.</td></tr>
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
prompt_arn
FROM aws.connect.prompts
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
 "InstanceArn": "{{ InstanceArn }}",
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.connect.prompts (
 InstanceArn,
 Name,
 region
)
SELECT 
{{ InstanceArn }},
 {{ Name }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "InstanceArn": "{{ InstanceArn }}",
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "S3Uri": "{{ S3Uri }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.connect.prompts (
 InstanceArn,
 Name,
 Description,
 S3Uri,
 Tags,
 region
)
SELECT 
 {{ InstanceArn }},
 {{ Name }},
 {{ Description }},
 {{ S3Uri }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.connect.prompts
WHERE data__Identifier = '<PromptArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>prompts</code> resource, the following permissions are required:

### Create
```json
connect:CreatePrompt,
connect:TagResource,
s3:GetObject,
kms:Decrypt,
s3:GetObjectAcl
```

### Delete
```json
connect:DeletePrompt
```

### List
```json
connect:ListPrompts
```

