---
title: enabled_control
hide_title: false
hide_table_of_contents: false
keywords:
  - enabled_control
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
Gets or operates on an individual <code>enabled_control</code> resource, use <code>enabled_controls</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enabled_control</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Enables a control on a specified target.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.controltower.enabled_control</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>control_identifier</code></td><td><code>string</code></td><td>Arn of the control.</td></tr>
<tr><td><code>target_identifier</code></td><td><code>string</code></td><td>Arn for Organizational unit to which the control needs to be applied</td></tr>
<tr><td><code>parameters</code></td><td><code>array</code></td><td>Parameters to configure the enabled control behavior.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A set of tags to assign to the enabled control.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
control_identifier,
target_identifier,
parameters,
tags
FROM aws.controltower.enabled_control
WHERE data__Identifier = '<TargetIdentifier>|<ControlIdentifier>';
```

## Permissions

To operate on the <code>enabled_control</code> resource, the following permissions are required:

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

