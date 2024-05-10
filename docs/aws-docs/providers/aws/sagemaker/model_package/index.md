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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>model_package</code> resource, use <code>model_packages</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_package</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelPackage</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_package" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="additional_inference_specifications" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="certify_for_marketplace" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_metadata_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="drift_check_baselines" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="inference_specification" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="metadata_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="model_approval_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_metrics" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="model_package_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_package_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_package_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sample_payload_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="skip_model_validation" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_algorithm_specification" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="task" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="validation_specification" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="model_package_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="approval_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_package_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_package_version" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="additional_inference_specifications_to_add" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="model_package_status_details" /></td><td><code>object</code></td><td></td></tr>
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
tags,
additional_inference_specifications,
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
skip_model_validation,
source_algorithm_specification,
task,
validation_specification,
model_package_arn,
approval_description,
creation_time,
last_modified_time,
model_package_status,
model_package_version,
additional_inference_specifications_to_add,
model_package_status_details
FROM aws.sagemaker.model_package
WHERE region = 'us-east-1' AND data__Identifier = '<ModelPackageArn>';
```


## Permissions

To operate on the <code>model_package</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeModelPackage,
sagemaker:ListTags
```

### Update
```json
sagemaker:UpdateModelPackage,
sagemaker:DescribeModelPackage,
sagemaker:ListTags,
sagemaker:AddTags,
sagemaker:DeleteTags
```

