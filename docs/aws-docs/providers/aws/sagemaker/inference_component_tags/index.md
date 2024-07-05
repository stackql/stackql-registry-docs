---
title: inference_component_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_component_tags
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

Expands all tag keys and values for <code>inference_components</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_component_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::InferenceComponent</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.inference_component_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="inference_component_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the inference component</td></tr>
<tr><td><CopyableCode code="inference_component_name" /></td><td><code>string</code></td><td>The name of the inference component</td></tr>
<tr><td><CopyableCode code="endpoint_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the endpoint the inference component is associated with</td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td>The name of the endpoint used to run the monitoring job.</td></tr>
<tr><td><CopyableCode code="variant_name" /></td><td><code>string</code></td><td>The name of the endpoint variant the inference component is associated with</td></tr>
<tr><td><CopyableCode code="failure_reason" /></td><td><code>string</code></td><td>The failure reason if the inference component is in a failed state</td></tr>
<tr><td><CopyableCode code="specification" /></td><td><code>object</code></td><td>The specification for the inference component</td></tr>
<tr><td><CopyableCode code="runtime_config" /></td><td><code>object</code></td><td>The runtime config for the inference component</td></tr>
<tr><td><CopyableCode code="inference_component_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>inference_components</code> in a region.
```sql
SELECT
region,
inference_component_arn,
inference_component_name,
endpoint_arn,
endpoint_name,
variant_name,
failure_reason,
specification,
runtime_config,
inference_component_status,
creation_time,
last_modified_time,
tag_key,
tag_value
FROM aws.sagemaker.inference_component_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>inference_component_tags</code> resource, see <a href="/providers/aws/sagemaker/inference_components/#permissions"><code>inference_components</code></a>


