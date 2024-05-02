---
title: mitigation_action
hide_title: false
hide_table_of_contents: false
keywords:
  - mitigation_action
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>mitigation_action</code> resource, use <code>mitigation_actions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mitigation_action</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Mitigation actions can be used to take actions to mitigate issues that were found in an Audit finding or Detect violation.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.mitigation_action</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>action_name</code></td><td><code>string</code></td><td>A unique identifier for the mitigation action.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>action_params</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>mitigation_action_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>mitigation_action_id</code></td><td><code>string</code></td><td></td></tr>
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
action_name,
role_arn,
tags,
action_params,
mitigation_action_arn,
mitigation_action_id
FROM aws.iot.mitigation_action
WHERE data__Identifier = '<ActionName>';
```

## Permissions

To operate on the <code>mitigation_action</code> resource, the following permissions are required:

### Read
```json
iot:DescribeMitigationAction,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateMitigationAction,
iot:ListTagsForResource,
iot:UntagResource,
iot:TagResource,
iam:PassRole
```

### Delete
```json
iot:DescribeMitigationAction,
iot:DeleteMitigationAction
```

