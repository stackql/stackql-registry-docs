---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - rolesanywhere
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Used to retrieve a list of <code>profiles</code> in a region or create a <code>profiles</code> resource, use <code>profile</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RolesAnywhere::Profile Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rolesanywhere.profiles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>profile_id</code></td><td><code>string</code></td><td></td></tr>
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
profile_id
FROM aws.rolesanywhere.profiles
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>profiles</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:GetPolicy,
iam:PassRole,
rolesanywhere:CreateProfile,
rolesanywhere:TagResource,
rolesanywhere:ListTagsForResource
```

### List
```json
rolesanywhere:ListProfiles,
rolesanywhere:ListTagsForResource
```

