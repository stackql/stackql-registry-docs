---
title: flywheel_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - flywheel_tags
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

Expands all tag keys and values for <code>flywheels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flywheel_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Comprehend::Flywheel resource creates an Amazon Comprehend Flywheel that enables customer to train their model.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.comprehend.flywheel_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="active_model_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_access_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_lake_s3_uri" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_security_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="flywheel_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="task_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>flywheels</code> in a region.
```sql
SELECT
region,
active_model_arn,
data_access_role_arn,
data_lake_s3_uri,
data_security_config,
flywheel_name,
model_type,
task_config,
arn,
tag_key,
tag_value
FROM aws.comprehend.flywheel_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>flywheel_tags</code> resource, see <a href="/providers/aws/comprehend/flywheels/#permissions"><code>flywheels</code></a>


