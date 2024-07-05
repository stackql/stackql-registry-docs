---
title: data_quality_job_definitions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - data_quality_job_definitions_list_only
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

Lists <code>data_quality_job_definitions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/data_quality_job_definitions/"><code>data_quality_job_definitions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_quality_job_definitions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::DataQualityJobDefinition</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.data_quality_job_definitions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="job_definition_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of job definition.</td></tr>
<tr><td><CopyableCode code="job_definition_name" /></td><td><code>string</code></td><td>The name of the job definition.</td></tr>
<tr><td><CopyableCode code="data_quality_baseline_config" /></td><td><code>object</code></td><td>Baseline configuration used to validate that the data conforms to the specified constraints and statistics.</td></tr>
<tr><td><CopyableCode code="data_quality_app_specification" /></td><td><code>object</code></td><td>Container image configuration object for the monitoring job.</td></tr>
<tr><td><CopyableCode code="data_quality_job_input" /></td><td><code>object</code></td><td>The inputs for a monitoring job.</td></tr>
<tr><td><CopyableCode code="data_quality_job_output_config" /></td><td><code>object</code></td><td>The output configuration for monitoring jobs.</td></tr>
<tr><td><CopyableCode code="job_resources" /></td><td><code>object</code></td><td>Identifies the resources to deploy for a monitoring job.</td></tr>
<tr><td><CopyableCode code="network_config" /></td><td><code>object</code></td><td>Networking options for a job, such as network traffic encryption between containers, whether to allow inbound and outbound network calls to and from containers, and the VPC subnets and security groups to use for VPC-enabled jobs.</td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td>The name of the endpoint used to run the monitoring job.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.</td></tr>
<tr><td><CopyableCode code="stopping_condition" /></td><td><code>object</code></td><td>Specifies a time limit for how long the monitoring job is allowed to run.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>data_quality_job_definitions</code> in a region.
```sql
SELECT
region,
job_definition_arn
FROM aws.sagemaker.data_quality_job_definitions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>data_quality_job_definitions_list_only</code> resource, see <a href="/providers/aws/sagemaker/data_quality_job_definitions/#permissions"><code>data_quality_job_definitions</code></a>


