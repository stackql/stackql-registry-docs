---
title: simulation_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - simulation_applications
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


Used to retrieve a list of <code>simulation_applications</code> in a region or to create or delete a <code>simulation_applications</code> resource, use <code>simulation_application</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simulation_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This schema is for testing purpose only.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.robomaker.simulation_applications" /></td></tr>
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
FROM aws.robomaker.simulation_applications
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
 "RobotSoftwareSuite": {
  "Name": "{{ Name }}",
  "Version": "{{ Version }}"
 },
 "SimulationSoftwareSuite": {
  "Name": "{{ Name }}",
  "Version": "{{ Version }}"
 }
}
>>>
--required properties only
INSERT INTO aws.robomaker.simulation_applications (
 RobotSoftwareSuite,
 SimulationSoftwareSuite,
 region
)
SELECT 
{{ RobotSoftwareSuite }},
 {{ SimulationSoftwareSuite }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "CurrentRevisionId": "{{ CurrentRevisionId }}",
 "RenderingEngine": {
  "Name": "{{ Name }}",
  "Version": "{{ Version }}"
 },
 "RobotSoftwareSuite": {
  "Name": "{{ Name }}",
  "Version": "{{ Version }}"
 },
 "SimulationSoftwareSuite": {
  "Name": "{{ Name }}",
  "Version": "{{ Version }}"
 },
 "Sources": [
  {
   "S3Bucket": "{{ S3Bucket }}",
   "S3Key": "{{ S3Key }}",
   "Architecture": "{{ Architecture }}"
  }
 ],
 "Environment": "{{ Environment }}",
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.robomaker.simulation_applications (
 Name,
 CurrentRevisionId,
 RenderingEngine,
 RobotSoftwareSuite,
 SimulationSoftwareSuite,
 Sources,
 Environment,
 Tags,
 region
)
SELECT 
 {{ Name }},
 {{ CurrentRevisionId }},
 {{ RenderingEngine }},
 {{ RobotSoftwareSuite }},
 {{ SimulationSoftwareSuite }},
 {{ Sources }},
 {{ Environment }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.robomaker.simulation_applications
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>simulation_applications</code> resource, the following permissions are required:

### Create
```json
robomaker:CreateSimulationApplication,
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
robomaker:DescribeSimulationApplication,
robomaker:DeleteSimulationApplication
```

### List
```json
robomaker:ListSimulationApplications
```

