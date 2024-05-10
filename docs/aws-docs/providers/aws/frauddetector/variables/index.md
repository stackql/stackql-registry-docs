---
title: variables
hide_title: false
hide_table_of_contents: false
keywords:
  - variables
  - frauddetector
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


Used to retrieve a list of <code>variables</code> in a region or to create or delete a <code>variables</code> resource, use <code>variable</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>variables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema for a Variable in Amazon Fraud Detector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.frauddetector.variables" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the variable.</td></tr>
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
FROM aws.frauddetector.variables
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
 "Name": "{{ Name }}",
 "DataSource": "{{ DataSource }}",
 "DataType": "{{ DataType }}",
 "DefaultValue": "{{ DefaultValue }}"
}
>>>
--required properties only
INSERT INTO aws.frauddetector.variables (
 Name,
 DataSource,
 DataType,
 DefaultValue,
 region
)
SELECT 
{{ Name }},
 {{ DataSource }},
 {{ DataType }},
 {{ DefaultValue }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "DataSource": "{{ DataSource }}",
 "DataType": "{{ DataType }}",
 "DefaultValue": "{{ DefaultValue }}",
 "Description": "{{ Description }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "VariableType": "{{ VariableType }}"
}
>>>
--all properties
INSERT INTO aws.frauddetector.variables (
 Name,
 DataSource,
 DataType,
 DefaultValue,
 Description,
 Tags,
 VariableType,
 region
)
SELECT 
 {{ Name }},
 {{ DataSource }},
 {{ DataType }},
 {{ DefaultValue }},
 {{ Description }},
 {{ Tags }},
 {{ VariableType }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.frauddetector.variables
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>variables</code> resource, the following permissions are required:

### Create
```json
frauddetector:GetVariables,
frauddetector:CreateVariable,
frauddetector:ListTagsForResource,
frauddetector:TagResource
```

### Delete
```json
frauddetector:GetVariables,
frauddetector:DeleteVariable
```

### List
```json
frauddetector:GetVariables,
frauddetector:ListTagsForResource
```

