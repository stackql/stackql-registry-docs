---
title: model_package_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - model_package_group_tags
  - sagemaker
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

Expands all tag keys and values for <code>model_package_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_package_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelPackageGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_package_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="model_package_group_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the model package group.</td></tr>
<tr><td><CopyableCode code="model_package_group_name" /></td><td><code>string</code></td><td>The name of the model package group.</td></tr>
<tr><td><CopyableCode code="model_package_group_description" /></td><td><code>string</code></td><td>The description of the model package group.</td></tr>
<tr><td><CopyableCode code="model_package_group_policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the model package group was created.</td></tr>
<tr><td><CopyableCode code="model_package_group_status" /></td><td><code>string</code></td><td>The status of a modelpackage group job.</td></tr>
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
Expands tags for all <code>model_package_groups</code> in a region.
```sql
SELECT
region,
model_package_group_arn,
model_package_group_name,
model_package_group_description,
model_package_group_policy,
creation_time,
model_package_group_status,
tag_key,
tag_value
FROM aws.sagemaker.model_package_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>model_package_group_tags</code> resource, see <a href="/providers/aws/sagemaker/model_package_groups/#permissions"><code>model_package_groups</code></a>

