---
title: state_machine_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - state_machine_versions
  - stepfunctions
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

Creates, updates, deletes or gets a <code>state_machine_version</code> resource or lists <code>state_machine_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_machine_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for StateMachineVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.stepfunctions.state_machine_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state_machine_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state_machine_revision_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachineversion.html"><code>AWS::StepFunctions::StateMachineVersion</code></a>.

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
    <td><CopyableCode code="StateMachineArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>state_machine_versions</code> in a region.
```sql
SELECT
region,
arn,
state_machine_arn,
state_machine_revision_id,
description
FROM aws.stepfunctions.state_machine_versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>state_machine_version</code>.
```sql
SELECT
region,
arn,
state_machine_arn,
state_machine_revision_id,
description
FROM aws.stepfunctions.state_machine_versions
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>state_machine_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.stepfunctions.state_machine_versions (
 StateMachineArn,
 region
)
SELECT 
'{{ StateMachineArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.stepfunctions.state_machine_versions (
 StateMachineArn,
 StateMachineRevisionId,
 Description,
 region
)
SELECT 
 '{{ StateMachineArn }}',
 '{{ StateMachineRevisionId }}',
 '{{ Description }}',
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
  - name: state_machine_version
    props:
      - name: StateMachineArn
        value: '{{ StateMachineArn }}'
      - name: StateMachineRevisionId
        value: '{{ StateMachineRevisionId }}'
      - name: Description
        value: '{{ Description }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.stepfunctions.state_machine_versions
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>state_machine_versions</code> resource, the following permissions are required:

### Create
```json
states:PublishStateMachineVersion,
states:ListStateMachineVersions,
states:DescribeStateMachine
```

### Read
```json
states:DescribeStateMachine
```

### Delete
```json
states:DeleteStateMachineVersion,
states:DescribeStateMachine
```

### List
```json
states:ListStateMachineVersions
```
