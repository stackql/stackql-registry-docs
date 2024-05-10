---
title: lifecycle_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_policy
  - imagebuilder
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


Gets or updates an individual <code>lifecycle_policy</code> resource, use <code>lifecycle_policies</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lifecycle_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::LifecyclePolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.lifecycle_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="execution_role" /></td><td><code>string</code></td><td>The execution role of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>The resource type of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="policy_details" /></td><td><code>array</code></td><td>The policy details of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="resource_selection" /></td><td><code>object</code></td><td>The resource selection of the lifecycle policy.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The tags associated with the lifecycle policy.</td></tr>
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
arn,
name,
description,
status,
execution_role,
resource_type,
policy_details,
resource_selection,
tags
FROM aws.imagebuilder.lifecycle_policy
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>lifecycle_policy</code> resource, the following permissions are required:

### Update
```json
iam:PassRole,
imagebuilder:GetLifecyclePolicy,
imagebuilder:UpdateLifecyclePolicy
```

### Read
```json
imagebuilder:GetLifecyclePolicy
```

