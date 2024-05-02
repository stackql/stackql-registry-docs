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
Retrieves a list of <code>enabled_controls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enabled_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Enables a control on a specified target.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.controltower.enabled_controls</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>target_identifier</code></td><td><code>string</code></td><td>Arn for Organizational unit to which the control needs to be applied</td></tr>
<tr><td><code>control_identifier</code></td><td><code>string</code></td><td>Arn of the control.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
target_identifier,
control_identifier
FROM aws.controltower.enabled_controls
WHERE region = 'us-east-1'
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

### List
```json
controltower:ListEnabledControls
```

