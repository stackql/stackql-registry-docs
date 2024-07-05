---
title: model_packages_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - model_packages_list_only
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

Lists <code>model_packages</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/model_packages/"><code>model_packages</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_packages_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelPackage</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_packages_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="additional_inference_specifications" /></td><td><code>array</code></td><td>An array of additional Inference Specification objects.</td></tr>
<tr><td><CopyableCode code="certify_for_marketplace" /></td><td><code>boolean</code></td><td>Whether to certify the model package for listing on AWS Marketplace.</td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td>A unique token that guarantees that the call to this API is idempotent.</td></tr>
<tr><td><CopyableCode code="customer_metadata_properties" /></td><td><code>object</code></td><td>The metadata properties associated with the model package versions.</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The machine learning domain of the model package you specified.</td></tr>
<tr><td><CopyableCode code="drift_check_baselines" /></td><td><code>object</code></td><td>Represents the drift check baselines that can be used when the model monitor is set using the model package.</td></tr>
<tr><td><CopyableCode code="inference_specification" /></td><td><code>object</code></td><td>Details about inference jobs that can be run with models based on this model package.</td></tr>
<tr><td><CopyableCode code="metadata_properties" /></td><td><code>object</code></td><td>Metadata properties of the tracking entity, trial, or trial component.</td></tr>
<tr><td><CopyableCode code="model_approval_status" /></td><td><code>string</code></td><td>The approval status of the model package.</td></tr>
<tr><td><CopyableCode code="model_metrics" /></td><td><code>object</code></td><td>A structure that contains model metrics reports.</td></tr>
<tr><td><CopyableCode code="model_package_description" /></td><td><code>string</code></td><td>The description of the model package.</td></tr>
<tr><td><CopyableCode code="model_package_group_name" /></td><td><code>string</code></td><td>The name of the model package group.</td></tr>
<tr><td><CopyableCode code="model_package_name" /></td><td><code>string</code></td><td>The name or arn of the model package.</td></tr>
<tr><td><CopyableCode code="sample_payload_url" /></td><td><code>string</code></td><td>The Amazon Simple Storage Service (Amazon S3) path where the sample payload are stored pointing to single gzip compressed tar archive.</td></tr>
<tr><td><CopyableCode code="skip_model_validation" /></td><td><code>string</code></td><td>Indicates if you want to skip model validation.</td></tr>
<tr><td><CopyableCode code="source_algorithm_specification" /></td><td><code>object</code></td><td>Details about the algorithm that was used to create the model package.</td></tr>
<tr><td><CopyableCode code="task" /></td><td><code>string</code></td><td>The machine learning task your model package accomplishes.</td></tr>
<tr><td><CopyableCode code="validation_specification" /></td><td><code>object</code></td><td>Specifies configurations for one or more transform jobs that Amazon SageMaker runs to test the model package.</td></tr>
<tr><td><CopyableCode code="model_package_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the model package group.</td></tr>
<tr><td><CopyableCode code="approval_description" /></td><td><code>string</code></td><td>A description provided for the model approval.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the model package was created.</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td>The time at which the model package was last modified.</td></tr>
<tr><td><CopyableCode code="model_package_status" /></td><td><code>string</code></td><td>The current status of the model package.</td></tr>
<tr><td><CopyableCode code="model_package_version" /></td><td><code>integer</code></td><td>The version of the model package.</td></tr>
<tr><td><CopyableCode code="additional_inference_specifications_to_add" /></td><td><code>array</code></td><td>An array of additional Inference Specification objects.</td></tr>
<tr><td><CopyableCode code="model_package_status_details" /></td><td><code>object</code></td><td>Details about the current status of the model package.</td></tr>
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
Lists all <code>model_packages</code> in a region.
```sql
SELECT
region,
model_package_arn
FROM aws.sagemaker.model_packages_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>model_packages_list_only</code> resource, see <a href="/providers/aws/sagemaker/model_packages/#permissions"><code>model_packages</code></a>


