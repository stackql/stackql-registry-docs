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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>cells</code> in a region or create a <code>cells</code> resource, use <code>cell</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cells</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The API Schema for AWS Route53 Recovery Readiness Cells.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoveryreadiness.cells" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cell_name" /></td><td><code>string</code></td><td>The name of the cell to create.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
cell_name
FROM aws.route53recoveryreadiness.cells
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>cells</code> resource, the following permissions are required:

### Create
```json
route53-recovery-readiness:CreateCell,
route53-recovery-readiness:GetCell,
route53-recovery-readiness:ListTagsForResources,
route53-recovery-readiness:TagResource
```

### List
```json
route53-recovery-readiness:ListCells
```

