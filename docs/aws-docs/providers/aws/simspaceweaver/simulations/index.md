---
title: simulations
hide_title: false
hide_table_of_contents: false
keywords:
  - simulations
  - simspaceweaver
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

Creates, updates, deletes or gets a <code>simulation</code> resource or lists <code>simulations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>simulations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::SimSpaceWeaver::Simulation resource creates an AWS Simulation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.simspaceweaver.simulations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the simulation.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role ARN.</td></tr>
<tr><td><CopyableCode code="schema_s3_location" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="describe_payload" /></td><td><code>string</code></td><td>Json object with all simulation details</td></tr>
<tr><td><CopyableCode code="maximum_duration" /></td><td><code>string</code></td><td>The maximum running time of the simulation.</td></tr>
<tr><td><CopyableCode code="snapshot_s3_location" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-simspaceweaver-simulation.html"><code>AWS::SimSpaceWeaver::Simulation</code></a>.

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
    <td><CopyableCode code="Name, RoleArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>simulations</code> in a region.
```sql
SELECT
region,
name,
role_arn,
schema_s3_location,
describe_payload,
maximum_duration,
snapshot_s3_location
FROM aws.simspaceweaver.simulations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>simulation</code>.
```sql
SELECT
region,
name,
role_arn,
schema_s3_location,
describe_payload,
maximum_duration,
snapshot_s3_location
FROM aws.simspaceweaver.simulations
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>simulation</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
INSERT INTO aws.simspaceweaver.simulations (
 Name,
 RoleArn,
 region
)
SELECT 
'{{ Name }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.simspaceweaver.simulations (
 Name,
 RoleArn,
 SchemaS3Location,
 MaximumDuration,
 SnapshotS3Location,
 region
)
SELECT 
 '{{ Name }}',
 '{{ RoleArn }}',
 '{{ SchemaS3Location }}',
 '{{ MaximumDuration }}',
 '{{ SnapshotS3Location }}',
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
  - name: simulation
    props:
      - name: Name
        value: '{{ Name }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: SchemaS3Location
        value:
          BucketName: '{{ BucketName }}'
          ObjectKey: '{{ ObjectKey }}'
      - name: MaximumDuration
        value: '{{ MaximumDuration }}'
      - name: SnapshotS3Location
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.simspaceweaver.simulations
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>simulations</code> resource, the following permissions are required:

### Create
```json
simspaceweaver:StartSimulation,
simspaceweaver:DescribeSimulation,
iam:GetRole,
iam:PassRole
```

### Read
```json
simspaceweaver:DescribeSimulation
```

### Update
```json
simspaceweaver:StartSimulation,
simspaceweaver:StopSimulation,
simspaceweaver:DeleteSimulation,
simspaceweaver:DescribeSimulation
```

### Delete
```json
simspaceweaver:StopSimulation,
simspaceweaver:DeleteSimulation,
simspaceweaver:DescribeSimulation
```

### List
```json
simspaceweaver:ListSimulations
```
