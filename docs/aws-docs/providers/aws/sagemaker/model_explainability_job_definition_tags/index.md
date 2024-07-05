---
title: model_explainability_job_definition_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - model_explainability_job_definition_tags
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

Expands all tag keys and values for <code>model_explainability_job_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_explainability_job_definition_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelExplainabilityJobDefinition</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_explainability_job_definition_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="job_definition_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of job definition.</td></tr>
<tr><td><CopyableCode code="job_definition_name" /></td><td><code>string</code></td><td>The name of the job definition.</td></tr>
<tr><td><CopyableCode code="model_explainability_baseline_config" /></td><td><code>object</code></td><td>Baseline configuration used to validate that the data conforms to the specified constraints and statistics.</td></tr>
<tr><td><CopyableCode code="model_explainability_app_specification" /></td><td><code>object</code></td><td>Container image configuration object for the monitoring job.</td></tr>
<tr><td><CopyableCode code="model_explainability_job_input" /></td><td><code>object</code></td><td>The inputs for a monitoring job.</td></tr>
<tr><td><CopyableCode code="model_explainability_job_output_config" /></td><td><code>object</code></td><td>The output configuration for monitoring jobs.</td></tr>
<tr><td><CopyableCode code="job_resources" /></td><td><code>object</code></td><td>Identifies the resources to deploy for a monitoring job.</td></tr>
<tr><td><CopyableCode code="network_config" /></td><td><code>object</code></td><td>Networking options for a job, such as network traffic encryption between containers, whether to allow inbound and outbound network calls to and from containers, and the VPC subnets and security groups to use for VPC-enabled jobs.</td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td>The name of the endpoint used to run the monitoring job.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.</td></tr>
<tr><td><CopyableCode code="stopping_condition" /></td><td><code>object</code></td><td>Specifies a time limit for how long the monitoring job is allowed to run.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the job definition was created.</td></tr>
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
Expands tags for all <code>model_explainability_job_definitions</code> in a region.
```sql
SELECT
region,
job_definition_arn,
job_definition_name,
model_explainability_baseline_config,
model_explainability_app_specification,
model_explainability_job_input,
model_explainability_job_output_config,
job_resources,
network_config,
endpoint_name,
role_arn,
stopping_condition,
creation_time,
tag_key,
tag_value
FROM aws.sagemaker.model_explainability_job_definition_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>model_explainability_job_definition_tags</code> resource, see <a href="/providers/aws/sagemaker/model_explainability_job_definitions/#permissions"><code>model_explainability_job_definitions</code></a>


