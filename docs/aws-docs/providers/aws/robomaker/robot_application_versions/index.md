---
title: robot_application_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - robot_application_versions
  - robomaker
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


Used to retrieve a list of <code>robot_application_versions</code> in a region or to create or delete a <code>robot_application_versions</code> resource, use <code>robot_application_version</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>robot_application_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::RoboMaker::RobotApplicationVersion resource creates an AWS RoboMaker RobotApplicationVersion. This helps you control which code your robot uses.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.robomaker.robot_application_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td></td></tr>
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
FROM aws.robomaker.robot_application_versions
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
 "Application": "{{ Application }}"
}
>>>
--required properties only
INSERT INTO aws.robomaker.robot_application_versions (
 Application,
 region
)
SELECT 
{{ .Application }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Application": "{{ Application }}",
 "CurrentRevisionId": "{{ CurrentRevisionId }}"
}
>>>
--all properties
INSERT INTO aws.robomaker.robot_application_versions (
 Application,
 CurrentRevisionId,
 region
)
SELECT 
 {{ .Application }},
 {{ .CurrentRevisionId }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.robomaker.robot_application_versions
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>robot_application_versions</code> resource, the following permissions are required:

### Create
```json
robomaker:CreateRobotApplicationVersion,
s3:GetObject,
ecr:BatchGetImage,
ecr:GetAuthorizationToken,
ecr:BatchCheckLayerAvailability,
ecr-public:GetAuthorizationToken,
sts:GetServiceBearerToken
```

### Delete
```json
robomaker:DeleteRobotApplication,
robomaker:DescribeRobotApplication
```

