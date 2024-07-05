---
title: inference_components_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_components_list_only
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

Lists <code>inference_components</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/inference_components/"><code>inference_components</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_components_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::InferenceComponent</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.inference_components_list_only" /></td></tr>
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
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of tags to apply to the resource</td></tr>
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
Lists all <code>inference_components</code> in a region.
```sql
SELECT
region,
inference_component_arn
FROM aws.sagemaker.inference_components_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>inference_components_list_only</code> resource, see <a href="/providers/aws/sagemaker/inference_components/#permissions"><code>inference_components</code></a>


