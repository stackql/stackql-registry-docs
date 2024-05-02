---
title: cell
hide_title: false
hide_table_of_contents: false
keywords:
  - cell
  - route53recoveryreadiness
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>cell</code> resource, use <code>cells</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cell</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The API Schema for AWS Route53 Recovery Readiness Cells.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53recoveryreadiness.cell</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cell_name</code></td><td><code>string</code></td><td>The name of the cell to create.</td></tr>
<tr><td><code>cell_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cell.</td></tr>
<tr><td><code>cells</code></td><td><code>array</code></td><td>A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells. For example, Availability Zones within specific Regions.</td></tr>
<tr><td><code>parent_readiness_scopes</code></td><td><code>array</code></td><td>The readiness scope for the cell, which can be a cell Amazon Resource Name (ARN) or a recovery group ARN. This is a list but currently can have only one element.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
cell_name,
cell_arn,
cells,
parent_readiness_scopes,
tags
FROM aws.route53recoveryreadiness.cell
WHERE data__Identifier = '<CellName>';
```

## Permissions

To operate on the <code>cell</code> resource, the following permissions are required:

### Read
```json
route53-recovery-readiness:GetCell,
route53-recovery-readiness:ListTagsForResources
```

### Update
```json
route53-recovery-readiness:GetCell,
route53-recovery-readiness:ListTagsForResources,
route53-recovery-readiness:TagResource,
route53-recovery-readiness:UntagResource,
route53-recovery-readiness:UpdateCell
```

### Delete
```json
route53-recovery-readiness:DeleteCell,
route53-recovery-readiness:GetCell
```

