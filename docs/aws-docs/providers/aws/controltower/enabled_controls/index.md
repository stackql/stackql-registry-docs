---
title: enabled_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - enabled_controls
  - controltower
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

Creates, updates, deletes or gets an <code>enabled_control</code> resource or lists <code>enabled_controls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enabled_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Enables a control on a specified target.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.controltower.enabled_controls" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="control_identifier" /></td><td><code>string</code></td><td>Arn of the control.</td></tr>
<tr><td><CopyableCode code="target_identifier" /></td><td><code>string</code></td><td>Arn for Organizational unit to which the control needs to be applied</td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>array</code></td><td>Parameters to configure the enabled control behavior.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A set of tags to assign to the enabled control.</td></tr>
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
    <td><CopyableCode code="TargetIdentifier, ControlIdentifier, region" /></td>
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
List all <code>enabled_controls</code> in a region.
```sql
SELECT
region,
target_identifier,
control_identifier
FROM aws.controltower.enabled_controls
WHERE region = 'us-east-1';
```
Gets all properties from an <code>enabled_control</code>.
```sql
SELECT
region,
control_identifier,
target_identifier,
parameters,
tags
FROM aws.controltower.enabled_controls
WHERE region = 'us-east-1' AND data__Identifier = '<TargetIdentifier>|<ControlIdentifier>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>enabled_control</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.controltower.enabled_controls (
 ControlIdentifier,
 TargetIdentifier,
 region
)
SELECT 
'{{ ControlIdentifier }}',
 '{{ TargetIdentifier }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.controltower.enabled_controls (
 ControlIdentifier,
 TargetIdentifier,
 Parameters,
 Tags,
 region
)
SELECT 
 '{{ ControlIdentifier }}',
 '{{ TargetIdentifier }}',
 '{{ Parameters }}',
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
  - name: enabled_control
    props:
      - name: ControlIdentifier
        value: '{{ ControlIdentifier }}'
      - name: TargetIdentifier
        value: '{{ TargetIdentifier }}'
      - name: Parameters
        value:
          - Value: null
            Key: '{{ Key }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.controltower.enabled_controls
WHERE data__Identifier = '<TargetIdentifier|ControlIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>enabled_controls</code> resource, the following permissions are required:

### Create
```json
controltower:ListEnabledControls,
controltower:GetEnabledControl,
controltower:GetControlOperation,
controltower:EnableControl,
controltower:TagResource,
organizations:UpdatePolicy,
organizations:CreatePolicy,
organizations:AttachPolicy,
organizations:DetachPolicy,
organizations:ListPoliciesForTarget,
organizations:ListTargetsForPolicy,
organizations:DescribePolicy
```

### Update
```json
controltower:ListEnabledControls,
controltower:GetEnabledControl,
controltower:GetControlOperation,
controltower:UpdateEnabledControl,
controltower:UntagResource,
controltower:TagResource,
organizations:UpdatePolicy,
organizations:CreatePolicy,
organizations:AttachPolicy,
organizations:DetachPolicy,
organizations:ListPoliciesForTarget,
organizations:ListTargetsForPolicy,
organizations:DescribePolicy
```

### Delete
```json
controltower:GetControlOperation,
controltower:DisableControl,
organizations:UpdatePolicy,
organizations:DeletePolicy,
organizations:CreatePolicy,
organizations:AttachPolicy,
organizations:DetachPolicy,
organizations:ListPoliciesForTarget,
organizations:ListTargetsForPolicy,
organizations:DescribePolicy
```

### Read
```json
controltower:ListEnabledControls,
controltower:GetEnabledControl,
controltower:ListTagsForResource
```

### List
```json
controltower:ListEnabledControls
```

