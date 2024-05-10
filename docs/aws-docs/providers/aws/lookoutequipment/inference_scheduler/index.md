---
title: inference_scheduler
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_scheduler
  - lookoutequipment
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


Gets or updates an individual <code>inference_scheduler</code> resource, use <code>inference_schedulers</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_scheduler</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for LookoutEquipment InferenceScheduler.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lookoutequipment.inference_scheduler" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="data_delay_offset_in_minutes" /></td><td><code>integer</code></td><td>A period of time (in minutes) by which inference on the data is delayed after the data starts.</td></tr>
<tr><td><CopyableCode code="data_input_configuration" /></td><td><code>object</code></td><td>Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location.</td></tr>
<tr><td><CopyableCode code="data_output_configuration" /></td><td><code>object</code></td><td>Specifies configuration information for the output results for the inference scheduler, including the S3 location for the output.</td></tr>
<tr><td><CopyableCode code="data_upload_frequency" /></td><td><code>string</code></td><td>How often data is uploaded to the source S3 bucket for the input data.</td></tr>
<tr><td><CopyableCode code="inference_scheduler_name" /></td><td><code>string</code></td><td>The name of the inference scheduler being created.</td></tr>
<tr><td><CopyableCode code="model_name" /></td><td><code>string</code></td><td>The name of the previously trained ML model being used to create the inference scheduler.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of a role with permission to access the data source being used for the inference.</td></tr>
<tr><td><CopyableCode code="server_side_kms_key_id" /></td><td><code>string</code></td><td>Provides the identifier of the AWS KMS customer master key (CMK) used to encrypt inference scheduler data by Amazon Lookout for Equipment.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags associated with the inference scheduler.</td></tr>
<tr><td><CopyableCode code="inference_scheduler_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the inference scheduler being created.</td></tr>
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
data_delay_offset_in_minutes,
data_input_configuration,
data_output_configuration,
data_upload_frequency,
inference_scheduler_name,
model_name,
role_arn,
server_side_kms_key_id,
tags,
inference_scheduler_arn
FROM aws.lookoutequipment.inference_scheduler
WHERE region = 'us-east-1' AND data__Identifier = '<InferenceSchedulerName>';
```


## Permissions

To operate on the <code>inference_scheduler</code> resource, the following permissions are required:

### Read
```json
lookoutequipment:DescribeInferenceScheduler
```

### Update
```json
lookoutequipment:UpdateInferenceScheduler,
lookoutequipment:DescribeInferenceScheduler,
lookoutequipment:StopInferenceScheduler,
lookoutequipment:StartInferenceScheduler
```

