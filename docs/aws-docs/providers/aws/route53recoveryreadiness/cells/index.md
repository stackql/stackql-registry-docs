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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>cell</code> resource or lists <code>cells</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cells</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The API Schema for AWS Route53 Recovery Readiness Cells.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoveryreadiness.cells" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cell_name" /></td><td><code>string</code></td><td>The name of the cell to create.</td></tr>
<tr><td><CopyableCode code="cell_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cell.</td></tr>
<tr><td><CopyableCode code="cells" /></td><td><code>array</code></td><td>A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells. For example, Availability Zones within specific Regions.</td></tr>
<tr><td><CopyableCode code="parent_readiness_scopes" /></td><td><code>array</code></td><td>The readiness scope for the cell, which can be a cell Amazon Resource Name (ARN) or a recovery group ARN. This is a list but currently can have only one element.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>cells</code> in a region.
```sql
SELECT
region,
cell_name,
cell_arn,
cells,
parent_readiness_scopes,
tags
FROM aws.route53recoveryreadiness.cells
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>cell</code>.
```sql
SELECT
region,
cell_name,
cell_arn,
cells,
parent_readiness_scopes,
tags
FROM aws.route53recoveryreadiness.cells
WHERE region = 'us-east-1' AND data__Identifier = '<CellName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cell</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53recoveryreadiness.cells (
 CellName,
 Cells,
 Tags,
 region
)
SELECT 
'{{ CellName }}',
 '{{ Cells }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53recoveryreadiness.cells (
 CellName,
 Cells,
 Tags,
 region
)
SELECT 
 '{{ CellName }}',
 '{{ Cells }}',
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
  - name: cell
    props:
      - name: CellName
        value: '{{ CellName }}'
      - name: Cells
        value:
          - '{{ Cells[0] }}'
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
DELETE FROM aws.route53recoveryreadiness.cells
WHERE data__Identifier = '<CellName>'
AND region = 'us-east-1';
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

### List
```json
route53-recovery-readiness:ListCells
```

