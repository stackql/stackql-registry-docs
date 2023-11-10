---
title: model_package
hide_title: false
hide_table_of_contents: false
keywords:
  - model_package
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
Gets an individual <code>model_package</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_package</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>model_package</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.model_package</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>additional_inference_specifications</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>additional_inference_specification_definition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>certify_for_marketplace</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>client_token</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>customer_metadata_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>domain</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>drift_check_baselines</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>inference_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>metadata_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>model_approval_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_metrics</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>model_package_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_package_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_package_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sample_payload_url</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_algorithm_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>task</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>validation_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>model_package_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>approval_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_modified_by</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>last_modified_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_package_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_package_version</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>additional_inference_specifications_to_add</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>model_package_status_details</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>model_package_status_item</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>created_by</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>environment</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
tags,
additional_inference_specifications,
additional_inference_specification_definition,
certify_for_marketplace,
client_token,
customer_metadata_properties,
domain,
drift_check_baselines,
inference_specification,
metadata_properties,
model_approval_status,
model_metrics,
model_package_description,
model_package_group_name,
model_package_name,
sample_payload_url,
source_algorithm_specification,
task,
validation_specification,
model_package_arn,
approval_description,
creation_time,
last_modified_by,
last_modified_time,
model_package_status,
model_package_version,
additional_inference_specifications_to_add,
model_package_status_details,
model_package_status_item,
created_by,
environment
FROM aws.sagemaker.model_package
WHERE region = 'us-east-1'
AND data__Identifier = '<ModelPackageArn>'
```
