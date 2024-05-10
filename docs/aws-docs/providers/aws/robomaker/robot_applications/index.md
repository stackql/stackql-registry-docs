---
title: robot_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - robot_applications
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


Used to retrieve a list of <code>robot_applications</code> in a region or to create or delete a <code>robot_applications</code> resource, use <code>robot_application</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>robot_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This schema is for testing purpose only.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.robomaker.robot_applications" /></td></tr>
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
FROM aws.robomaker.robot_applications
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>robot_application</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- robot_application.iql (required properties only)
INSERT INTO aws.robomaker.robot_applications (
 RobotSoftwareSuite,
 region
)
SELECT 
'{{ RobotSoftwareSuite }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- robot_application.iql (all properties)
INSERT INTO aws.robomaker.robot_applications (
 Name,
 Sources,
 Environment,
 RobotSoftwareSuite,
 CurrentRevisionId,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Sources }}',
 '{{ Environment }}',
 '{{ RobotSoftwareSuite }}',
 '{{ CurrentRevisionId }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: robot_application
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Sources
        value:
          - S3Bucket: '{{ S3Bucket }}'
            S3Key: '{{ S3Key }}'
            Architecture: '{{ Architecture }}'
      - name: Environment
        value: '{{ Environment }}'
      - name: RobotSoftwareSuite
        value:
          Name: '{{ Name }}'
          Version: '{{ Version }}'
      - name: CurrentRevisionId
        value: '{{ CurrentRevisionId }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.robomaker.robot_applications
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>robot_applications</code> resource, the following permissions are required:

### Create
```json
robomaker:CreateRobotApplication,
robomaker:TagResource,
robomaker:UntagResource,
ecr:BatchGetImage,
ecr:GetAuthorizationToken,
ecr:BatchCheckLayerAvailability,
ecr-public:GetAuthorizationToken,
sts:GetServiceBearerToken
```

### Delete
```json
robomaker:DescribeRobotApplication,
robomaker:DeleteRobotApplication
```

### List
```json
robomaker:ListRobotApplications
```

