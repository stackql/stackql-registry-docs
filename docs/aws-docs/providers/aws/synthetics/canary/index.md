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
Gets or operates on an individual <code>canary</code> resource, use <code>canaries</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>canary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Synthetics::Canary</td></tr>
<tr><td><b>Id</b></td><td><code>aws.synthetics.canary</code></td></tr>
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
<tr><td><code>vpc_config</code></td><td><code>object</code></td><td>Provide VPC Configuration if enabled.</td></tr>
<tr><td><code>run_config</code></td><td><code>object</code></td><td>Provide canary run configuration</td></tr>
<tr><td><code>start_canary_after_creation</code></td><td><code>boolean</code></td><td>Runs canary if set to True. Default is False</td></tr>
<tr><td><code>visual_reference</code></td><td><code>object</code></td><td>Visual reference configuration for visual testing</td></tr>
<tr><td><code>delete_lambda_resources_on_canary_deletion</code></td><td><code>boolean</code></td><td>Deletes associated lambda resources created by Synthetics if set to True. Default is False</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
vpc_config,
run_config,
start_canary_after_creation,
visual_reference,
delete_lambda_resources_on_canary_deletion
FROM aws.synthetics.canary
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>canary</code> resource, the following permissions are required:

### Update
```json
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
iam:PassRole
```

### Read
```json
synthetics:GetCanary,
synthetics:DescribeCanaries,
synthetics:ListTagsForResource,
iam:ListRoles,
s3:ListAllMyBuckets,
s3:GetBucketLocation
```

### Delete
```json
synthetics:DeleteCanary,
synthetics:GetCanary
```

