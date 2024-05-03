---
title: findings_filter
hide_title: false
hide_table_of_contents: false
keywords:
  - findings_filter
  - macie
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

Gets or operates on an individual <code>findings_filter</code> resource, use <code>findings_filters</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>findings_filter</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Macie FindingsFilter resource schema.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.macie.findings_filter" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Findings filter name</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Findings filter description</td></tr>
<tr><td><CopyableCode code="finding_criteria" /></td><td><code>object</code></td><td>Findings filter criteria.</td></tr>
<tr><td><CopyableCode code="action" /></td><td><code>string</code></td><td>Findings filter action.</td></tr>
<tr><td><CopyableCode code="position" /></td><td><code>integer</code></td><td>Findings filter position.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Findings filter ID.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Findings filter ARN.</td></tr>
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
finding_criteria,
action,
position,
id,
arn,
tags
FROM aws.macie.findings_filter
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>findings_filter</code> resource, the following permissions are required:

### Read
```json
macie2:GetFindingsFilter
```

### Update
```json
macie2:GetFindingsFilter,
macie2:UpdateFindingsFilter,
macie2:TagResource,
macie2:UntagResource
```

### Delete
```json
macie2:DeleteFindingsFilter
```

