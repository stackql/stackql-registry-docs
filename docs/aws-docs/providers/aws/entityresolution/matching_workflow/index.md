---
title: matching_workflow
hide_title: false
hide_table_of_contents: false
keywords:
  - matching_workflow
  - entityresolution
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


Gets or updates an individual <code>matching_workflow</code> resource, use <code>matching_workflows</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>matching_workflow</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>MatchingWorkflow defined in AWS Entity Resolution service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.matching_workflow" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="workflow_name" /></td><td><code>string</code></td><td>The name of the MatchingWorkflow</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the MatchingWorkflow</td></tr>
<tr><td><CopyableCode code="input_source_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="output_source_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resolution_techniques" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="workflow_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
workflow_name,
description,
input_source_config,
output_source_config,
resolution_techniques,
role_arn,
tags,
workflow_arn,
created_at,
updated_at
FROM aws.entityresolution.matching_workflow
WHERE region = 'us-east-1' AND data__Identifier = '<WorkflowName>';
```


## Permissions

To operate on the <code>matching_workflow</code> resource, the following permissions are required:

### Read
```json
entityresolution:GetMatchingWorkflow,
entityresolution:ListTagsForResource
```

### Update
```json
entityresolution:GetMatchingWorkflow,
entityresolution:UpdateMatchingWorkflow,
entityresolution:ListTagsForResource,
entityresolution:TagResource,
entityresolution:UntagResource,
iam:PassRole,
kms:CreateGrant,
kms:DescribeKey
```

