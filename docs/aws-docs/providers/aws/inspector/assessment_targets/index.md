---
title: assessment_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - assessment_targets
  - inspector
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

Creates, updates, deletes or gets an <code>assessment_target</code> resource or lists <code>assessment_targets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessment_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Inspector::AssessmentTarget</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.inspector.assessment_targets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="assessment_target_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_group_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>assessment_targets</code> in a region.
```sql
SELECT
region,
arn
FROM aws.inspector.assessment_targets
WHERE region = 'us-east-1';
```
Gets all properties from an <code>assessment_target</code>.
```sql
SELECT
region,
arn,
assessment_target_name,
resource_group_arn
FROM aws.inspector.assessment_targets
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assessment_target</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.inspector.assessment_targets (
 AssessmentTargetName,
 ResourceGroupArn,
 region
)
SELECT 
'{{ AssessmentTargetName }}',
 '{{ ResourceGroupArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.inspector.assessment_targets (
 AssessmentTargetName,
 ResourceGroupArn,
 region
)
SELECT 
 '{{ AssessmentTargetName }}',
 '{{ ResourceGroupArn }}',
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
  - name: assessment_target
    props:
      - name: AssessmentTargetName
        value: '{{ AssessmentTargetName }}'
      - name: ResourceGroupArn
        value: '{{ ResourceGroupArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.inspector.assessment_targets
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>assessment_targets</code> resource, the following permissions are required:

### Create
```json
inspector:CreateAssessmentTarget,
inspector:ListAssessmentTargets,
inspector:DescribeAssessmentTargets
```

### Update
```json
inspector:DescribeAssessmentTargets,
inspector:UpdateAssessmentTarget
```

### Read
```json
inspector:DescribeAssessmentTargets
```

### Delete
```json
inspector:DeleteAssessmentTarget
```

### List
```json
inspector:ListAssessmentTargets
```

