---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - m2
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


Used to retrieve a list of <code>applications</code> in a region or to create or delete a <code>applications</code> resource, use <code>application</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents an application that runs on an AWS Mainframe Modernization Environment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.m2.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td></td></tr>
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
application_arn
FROM aws.m2.applications
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
 "Definition": null,
 "EngineType": "{{ EngineType }}",
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.m2.applications (
 Definition,
 EngineType,
 Name,
 region
)
SELECT 
{{ .Definition }},
 {{ .EngineType }},
 {{ .Name }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Definition": null,
 "Description": "{{ Description }}",
 "EngineType": "{{ EngineType }}",
 "KmsKeyId": "{{ KmsKeyId }}",
 "Name": "{{ Name }}",
 "RoleArn": "{{ RoleArn }}",
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.m2.applications (
 Definition,
 Description,
 EngineType,
 KmsKeyId,
 Name,
 RoleArn,
 Tags,
 region
)
SELECT 
 {{ .Definition }},
 {{ .Description }},
 {{ .EngineType }},
 {{ .KmsKeyId }},
 {{ .Name }},
 {{ .RoleArn }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.m2.applications
WHERE data__Identifier = '<ApplicationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
m2:CreateApplication,
m2:GetApplication,
m2:ListTagsForResource,
m2:TagResource,
s3:GetObject,
s3:ListBucket,
kms:DescribeKey,
kms:CreateGrant,
iam:PassRole
```

### Delete
```json
elasticloadbalancing:DeleteListener,
elasticloadbalancing:DeleteTargetGroup,
logs:DeleteLogDelivery,
m2:GetApplication,
m2:DeleteApplication
```

### List
```json
m2:ListApplications
```

