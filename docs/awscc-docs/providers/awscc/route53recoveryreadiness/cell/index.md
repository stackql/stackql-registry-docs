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
Gets an individual <code>cell</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cell</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cell</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53recoveryreadiness.cell</code></td></tr>
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
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>cell</code> resource, the following permissions are required:

### Read
<pre>
route53-recovery-readiness:GetCell,
route53-recovery-readiness:ListTagsForResources</pre>

### Update
<pre>
route53-recovery-readiness:GetCell,
route53-recovery-readiness:ListTagsForResources,
route53-recovery-readiness:TagResource,
route53-recovery-readiness:UntagResource,
route53-recovery-readiness:UpdateCell</pre>

### Delete
<pre>
route53-recovery-readiness:DeleteCell,
route53-recovery-readiness:GetCell</pre>


## Example
```sql
SELECT
region,
cell_name,
cell_arn,
cells,
parent_readiness_scopes,
tags
FROM awscc.route53recoveryreadiness.cell
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;CellName&gt;'
```
