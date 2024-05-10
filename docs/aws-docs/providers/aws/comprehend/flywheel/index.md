---
title: flywheel
hide_title: false
hide_table_of_contents: false
keywords:
  - flywheel
  - comprehend
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


Gets or updates an individual <code>flywheel</code> resource, use <code>flywheels</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flywheel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Comprehend::Flywheel resource creates an Amazon Comprehend Flywheel that enables customer to train their model.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.comprehend.flywheel" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="active_model_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_access_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_lake_s3_uri" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_security_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="flywheel_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="task_config" /></td><td><code>object</code></td><td></td></tr>
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
active_model_arn,
data_access_role_arn,
data_lake_s3_uri,
data_security_config,
flywheel_name,
model_type,
tags,
task_config,
arn
FROM aws.comprehend.flywheel
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>flywheel</code> resource, the following permissions are required:

### Read
```json
comprehend:DescribeFlywheel,
comprehend:ListTagsForResource
```

### Update
```json
iam:PassRole,
comprehend:DescribeFlywheel,
comprehend:UpdateFlywheel,
comprehend:ListTagsForResource,
comprehend:TagResource,
comprehend:UntagResource
```

