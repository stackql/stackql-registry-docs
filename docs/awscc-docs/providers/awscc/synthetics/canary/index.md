---
title: canary
hide_title: false
hide_table_of_contents: false
keywords:
  - canary
  - synthetics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>canary</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>canary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>canary</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.synthetics.canary</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the canary.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id of the canary</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>State of the canary</td></tr>
<tr><td><code>code</code></td><td><code>object</code></td><td>Provide the canary script source</td></tr>
<tr><td><code>artifact_s3_location</code></td><td><code>string</code></td><td>Provide the s3 bucket output location for test results</td></tr>
<tr><td><code>artifact_config</code></td><td><code>object</code></td><td>Provide artifact configuration</td></tr>
<tr><td><code>schedule</code></td><td><code>object</code></td><td>Frequency to run your canaries</td></tr>
<tr><td><code>execution_role_arn</code></td><td><code>string</code></td><td>Lambda Execution role used to run your canaries</td></tr>
<tr><td><code>runtime_version</code></td><td><code>string</code></td><td>Runtime version of Synthetics Library</td></tr>
<tr><td><code>success_retention_period</code></td><td><code>integer</code></td><td>Retention period of successful canary runs represented in number of days</td></tr>
<tr><td><code>failure_retention_period</code></td><td><code>integer</code></td><td>Retention period of failed canary runs represented in number of days</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>v_pc_config</code></td><td><code>object</code></td><td>Provide VPC Configuration if enabled.</td></tr>
<tr><td><code>run_config</code></td><td><code>object</code></td><td>Provide canary run configuration</td></tr>
<tr><td><code>start_canary_after_creation</code></td><td><code>boolean</code></td><td>Runs canary if set to True. Default is False</td></tr>
<tr><td><code>visual_reference</code></td><td><code>object</code></td><td>Visual reference configuration for visual testing</td></tr>
<tr><td><code>delete_lambda_resources_on_canary_deletion</code></td><td><code>boolean</code></td><td>Deletes associated lambda resources created by Synthetics if set to True. Default is False</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>canary</code> resource, the following permissions are required:

### Update
<pre>
synthetics:UpdateCanary,
synthetics:StartCanary,
synthetics:StopCanary,
synthetics:GetCanary,
synthetics:TagResource,
synthetics:UntagResource,
s3:GetObject,
s3:GetObjectVersion,
s3:PutBucketEncryption,
s3:PutEncryptionConfiguration,
s3:GetBucketLocation,
lambda:AddPermission,
lambda:PublishVersion,
lambda:UpdateFunctionConfiguration,
lambda:GetFunctionConfiguration,
lambda:GetLayerVersionByArn,
lambda:GetLayerVersion,
lambda:PublishLayerVersion,
iam:PassRole</pre>

### Read
<pre>
synthetics:GetCanary,
synthetics:DescribeCanaries,
synthetics:ListTagsForResource,
iam:ListRoles,
s3:ListAllMyBuckets,
s3:GetBucketLocation</pre>

### Delete
<pre>
synthetics:DeleteCanary,
synthetics:GetCanary</pre>


## Example
```sql
SELECT
region,
name,
id,
state,
code,
artifact_s3_location,
artifact_config,
schedule,
execution_role_arn,
runtime_version,
success_retention_period,
failure_retention_period,
tags,
v_pc_config,
run_config,
start_canary_after_creation,
visual_reference,
delete_lambda_resources_on_canary_deletion
FROM awscc.synthetics.canary
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
