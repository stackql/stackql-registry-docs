---
title: filter
hide_title: false
hide_table_of_contents: false
keywords:
  - filter
  - inspectorv2
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

Gets or operates on an individual <code>filter</code> resource, use <code>filters</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>filter</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Inspector Filter resource schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.inspectorv2.filter" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Findings filter name.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Findings filter description.</td></tr>
<tr><td><CopyableCode code="filter_criteria" /></td><td><code>object</code></td><td>Findings filter criteria.</td></tr>
<tr><td><CopyableCode code="filter_action" /></td><td><code>string</code></td><td>Findings filter action.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Findings filter ARN.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name,
description,
filter_criteria,
filter_action,
arn
FROM aws.inspectorv2.filter
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>filter</code> resource, the following permissions are required:

### Read
```json
inspector2:ListFilters
```

### Update
```json
inspector2:ListFilters,
inspector2:UpdateFilter
```

### Delete
```json
inspector2:DeleteFilter,
inspector2:ListFilters
```

