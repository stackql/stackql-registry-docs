---
title: frameworks
hide_title: false
hide_table_of_contents: false
keywords:
  - frameworks
  - backup
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


Used to retrieve a list of <code>frameworks</code> in a region or to create or delete a <code>frameworks</code> resource, use <code>framework</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>frameworks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains detailed information about a framework. Frameworks contain controls, which evaluate and report on your backup events and resources. Frameworks generate daily compliance results.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.frameworks" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="framework_arn" /></td><td><code>string</code></td><td>An Amazon Resource Name (ARN) that uniquely identifies Framework as a resource</td></tr>
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
framework_arn
FROM aws.backup.frameworks
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
 "FrameworkControls": [
  {
   "ControlName": "{{ ControlName }}",
   "ControlInputParameters": [
    {
     "ParameterName": "{{ ParameterName }}",
     "ParameterValue": "{{ ParameterValue }}"
    }
   ],
   "ControlScope": {
    "ComplianceResourceIds": [
     "{{ ComplianceResourceIds[0] }}"
    ],
    "ComplianceResourceTypes": [
     "{{ ComplianceResourceTypes[0] }}"
    ],
    "Tags": [
     {
      "Key": "{{ Key }}",
      "Value": "{{ Value }}"
     }
    ]
   }
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.backup.frameworks (
 FrameworkControls,
 region
)
SELECT 
{{ .FrameworkControls }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "FrameworkName": "{{ FrameworkName }}",
 "FrameworkDescription": "{{ FrameworkDescription }}",
 "FrameworkControls": [
  {
   "ControlName": "{{ ControlName }}",
   "ControlInputParameters": [
    {
     "ParameterName": "{{ ParameterName }}",
     "ParameterValue": "{{ ParameterValue }}"
    }
   ],
   "ControlScope": {
    "ComplianceResourceIds": [
     "{{ ComplianceResourceIds[0] }}"
    ],
    "ComplianceResourceTypes": [
     "{{ ComplianceResourceTypes[0] }}"
    ],
    "Tags": [
     {
      "Key": "{{ Key }}",
      "Value": "{{ Value }}"
     }
    ]
   }
  }
 ],
 "FrameworkTags": [
  null
 ]
}
>>>
--all properties
INSERT INTO aws.backup.frameworks (
 FrameworkName,
 FrameworkDescription,
 FrameworkControls,
 FrameworkTags,
 region
)
SELECT 
 {{ .FrameworkName }},
 {{ .FrameworkDescription }},
 {{ .FrameworkControls }},
 {{ .FrameworkTags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.backup.frameworks
WHERE data__Identifier = '<FrameworkArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>frameworks</code> resource, the following permissions are required:

### Create
```json
backup:CreateFramework,
backup:DescribeFramework,
backup:ListTags,
backup:TagResource,
iam:CreateServiceLinkedRole
```

### Delete
```json
backup:DeleteFramework,
backup:DescribeFramework
```

### List
```json
backup:ListFrameworks
```

