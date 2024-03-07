---
title: cells
hide_title: false
hide_table_of_contents: false
keywords:
  - cells
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
Retrieves a list of <code>cells</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cells</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cells</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53recoveryreadiness.cells</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cell_name</code></td><td><code>string</code></td><td>The name of the cell to create.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>cells</code> resource, the following permissions are required:

### Create
<pre>
route53-recovery-readiness:CreateCell,
route53-recovery-readiness:GetCell,
route53-recovery-readiness:ListTagsForResources,
route53-recovery-readiness:TagResource</pre>

### List
<pre>
route53-recovery-readiness:ListCells</pre>


## Example
```sql
SELECT
region,
cell_name
FROM awscc.route53recoveryreadiness.cells
WHERE region = 'us-east-1'
```
