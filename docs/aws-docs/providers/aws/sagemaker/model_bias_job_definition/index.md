---
title: model_bias_job_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - model_bias_job_definition
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


Gets or updates an individual <code>model_bias_job_definition</code> resource, use <code>model_bias_job_definitions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_bias_job_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelBiasJobDefinition</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_bias_job_definition" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="job_definition_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of job definition.</td></tr>
<tr><td><CopyableCode code="job_definition_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_bias_baseline_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="model_bias_app_specification" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="model_bias_job_input" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="model_bias_job_output_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="job_resources" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="network_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.</td></tr>
<tr><td><CopyableCode code="stopping_condition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the job definition was created.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
job_definition_arn,
job_definition_name,
model_bias_baseline_config,
model_bias_app_specification,
model_bias_job_input,
model_bias_job_output_config,
job_resources,
network_config,
endpoint_name,
role_arn,
stopping_condition,
tags,
creation_time
FROM aws.sagemaker.model_bias_job_definition
WHERE region = 'us-east-1' AND data__Identifier = '<JobDefinitionArn>';
```


## Permissions

To operate on the <code>model_bias_job_definition</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeModelBiasJobDefinition
```

