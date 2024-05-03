---
title: indices
hide_title: false
hide_table_of_contents: false
keywords:
  - indices
  - resourceexplorer2
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

Used to retrieve a list of <code>indices</code> in a region or create a <code>indices</code> resource, use <code>index</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ResourceExplorer2::Index Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.resourceexplorer2.indices" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
arn
FROM aws.resourceexplorer2.indices
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>indices</code> resource, the following permissions are required:

### Create
```json
resource-explorer-2:CreateIndex,
resource-explorer-2:GetIndex,
resource-explorer-2:TagResource,
resource-explorer-2:UpdateIndexType,
resource-explorer-2:DeleteIndex,
iam:CreateServiceLinkedRole
```

### List
```json
resource-explorer-2:ListIndexes
```

