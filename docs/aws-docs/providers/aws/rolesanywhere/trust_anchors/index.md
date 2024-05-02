---
title: trust_anchors
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_anchors
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
Retrieves a list of <code>trust_anchors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_anchors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RolesAnywhere::TrustAnchor Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rolesanywhere.trust_anchors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>trust_anchor_id</code></td><td><code>string</code></td><td></td></tr>
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
trust_anchor_id
FROM aws.rolesanywhere.trust_anchors
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>trust_anchors</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
rolesanywhere:CreateTrustAnchor,
rolesanywhere:TagResource,
rolesanywhere:ListTagsForResource
```

### List
```json
rolesanywhere:ListTrustAnchors,
rolesanywhere:ListTagsForResource
```

