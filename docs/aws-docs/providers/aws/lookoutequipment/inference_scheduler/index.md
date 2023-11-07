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
Gets an individual <code>inference_scheduler</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_scheduler</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.lookoutequipment.inference_scheduler</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DataDelayOffsetInMinutes</code></td><td><code>integer</code></td><td>A period of time (in minutes) by which inference on the data is delayed after the data starts.</td></tr>
<tr><td><code>DataInputConfiguration</code></td><td><code>object</code></td><td>Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location.</td></tr>
<tr><td><code>DataOutputConfiguration</code></td><td><code>object</code></td><td>Specifies configuration information for the output results for the inference scheduler, including the S3 location for the output.</td></tr>
<tr><td><code>DataUploadFrequency</code></td><td><code>string</code></td><td>How often data is uploaded to the source S3 bucket for the input data.</td></tr>
<tr><td><code>InferenceSchedulerName</code></td><td><code>string</code></td><td>The name of the inference scheduler being created.</td></tr>
<tr><td><code>ModelName</code></td><td><code>string</code></td><td>The name of the previously trained ML model being used to create the inference scheduler.</td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of a role with permission to access the data source being used for the inference.</td></tr>
<tr><td><code>ServerSideKmsKeyId</code></td><td><code>string</code></td><td>Provides the identifier of the AWS KMS customer master key (CMK) used to encrypt inference scheduler data by Amazon Lookout for Equipment.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Any tags associated with the inference scheduler.</td></tr>
<tr><td><code>InferenceSchedulerArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the inference scheduler being created.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.lookoutequipment.inference_scheduler
WHERE region = 'us-east-1' AND data__Identifier = '&lt;InferenceSchedulerName&gt;'
</pre>
