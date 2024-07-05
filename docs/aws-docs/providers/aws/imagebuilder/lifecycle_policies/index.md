---
title: lifecycle_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_policies
  - imagebuilder
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

Creates, updates, deletes or gets a <code>lifecycle_policy</code> resource or lists <code>lifecycle_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lifecycle_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::LifecyclePolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.lifecycle_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="execution_role" /></td><td><code>string</code></td><td>The execution role of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>The resource type of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="policy_details" /></td><td><code>array</code></td><td>The policy details of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="resource_selection" /></td><td><code>object</code></td><td>The resource selection of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The tags associated with the lifecycle policy.</td></tr>
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
    <td><CopyableCode code="Name, ExecutionRole, ResourceType, PolicyDetails, ResourceSelection, region" /></td>
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
Gets all <code>lifecycle_policies</code> in a region.
```sql
SELECT
region,
arn,
name,
description,
status,
execution_role,
resource_type,
policy_details,
resource_selection,
tags
FROM aws.imagebuilder.lifecycle_policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>lifecycle_policy</code>.
```sql
SELECT
region,
arn,
name,
description,
status,
execution_role,
resource_type,
policy_details,
resource_selection,
tags
FROM aws.imagebuilder.lifecycle_policies
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>lifecycle_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.imagebuilder.lifecycle_policies (
 Name,
 ExecutionRole,
 ResourceType,
 PolicyDetails,
 ResourceSelection,
 region
)
SELECT 
'{{ Name }}',
 '{{ ExecutionRole }}',
 '{{ ResourceType }}',
 '{{ PolicyDetails }}',
 '{{ ResourceSelection }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.imagebuilder.lifecycle_policies (
 Name,
 Description,
 Status,
 ExecutionRole,
 ResourceType,
 PolicyDetails,
 ResourceSelection,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ Status }}',
 '{{ ExecutionRole }}',
 '{{ ResourceType }}',
 '{{ PolicyDetails }}',
 '{{ ResourceSelection }}',
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
  - name: lifecycle_policy
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: Status
        value: '{{ Status }}'
      - name: ExecutionRole
        value: '{{ ExecutionRole }}'
      - name: ResourceType
        value: '{{ ResourceType }}'
      - name: PolicyDetails
        value:
          - Action:
              Type: '{{ Type }}'
              IncludeResources:
                Amis: '{{ Amis }}'
                Containers: '{{ Containers }}'
                Snapshots: '{{ Snapshots }}'
            Filter:
              Type: '{{ Type }}'
              Value: '{{ Value }}'
              Unit: '{{ Unit }}'
              RetainAtLeast: '{{ RetainAtLeast }}'
            ExclusionRules:
              TagMap: {}
              Amis:
                IsPublic: '{{ IsPublic }}'
                Regions:
                  - '{{ Regions[0] }}'
                SharedAccounts:
                  - '{{ SharedAccounts[0] }}'
                LastLaunched:
                  Value: '{{ Value }}'
                  Unit: null
                TagMap: {}
      - name: ResourceSelection
        value:
          Recipes:
            - Name: '{{ Name }}'
              SemanticVersion: '{{ SemanticVersion }}'
          TagMap: {}
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.imagebuilder.lifecycle_policies
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>lifecycle_policies</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
imagebuilder:CreateLifecyclePolicy,
imagebuilder:GetLifecyclePolicy,
imagebuilder:TagResource
```

### Update
```json
iam:PassRole,
imagebuilder:GetLifecyclePolicy,
imagebuilder:UpdateLifecyclePolicy
```

### Read
```json
imagebuilder:GetLifecyclePolicy
```

### Delete
```json
imagebuilder:GetLifecyclePolicy,
imagebuilder:DeleteLifecyclePolicy,
imagebuilder:UnTagResource
```

### List
```json
imagebuilder:ListLifecyclePolicies
```

