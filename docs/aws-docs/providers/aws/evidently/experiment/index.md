---
title: experiment
hide_title: false
hide_table_of_contents: false
keywords:
  - experiment
  - evidently
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

Gets or operates on an individual <code>experiment</code> resource, use <code>experiments</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Evidently::Experiment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.evidently.experiment" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="project" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="running_status" /></td><td><code>object</code></td><td>Start Experiment. Default is False</td></tr>
<tr><td><CopyableCode code="randomization_salt" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="treatments" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="metric_goals" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="sampling_rate" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="online_ab_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="segment" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="remove_segment" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
arn,
name,
project,
description,
running_status,
randomization_salt,
treatments,
metric_goals,
sampling_rate,
online_ab_config,
segment,
remove_segment,
tags
FROM aws.evidently.experiment
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>experiment</code> resource, the following permissions are required:

### Read
```json
evidently:GetExperiment,
evidently:ListTagsForResource
```

### Update
```json
evidently:UpdateExperiment,
evidently:TagResource,
evidently:UntagResource,
evidently:GetExperiment,
evidently:StartExperiment,
evidently:StopExperiment
```

### Delete
```json
evidently:DeleteExperiment,
evidently:UntagResource,
evidently:GetExperiment
```

