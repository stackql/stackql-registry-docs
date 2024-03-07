---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - emrserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.emrserverless.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>architecture</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>User friendly Application name.</td></tr>
<tr><td><code>release_label</code></td><td><code>string</code></td><td>EMR release label.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of the application</td></tr>
<tr><td><code>initial_capacity</code></td><td><code>array</code></td><td>Initial capacity initialized when an Application is started.</td></tr>
<tr><td><code>maximum_capacity</code></td><td><code>object</code></td><td>Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tag map with key and value</td></tr>
<tr><td><code>auto_start_configuration</code></td><td><code>object</code></td><td>Configuration for Auto Start of Application.</td></tr>
<tr><td><code>auto_stop_configuration</code></td><td><code>object</code></td><td>Configuration for Auto Stop of Application.</td></tr>
<tr><td><code>image_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>monitoring_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>runtime_configuration</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>network_configuration</code></td><td><code>object</code></td><td>Network Configuration for customer VPC connectivity.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the EMR Serverless Application.</td></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td>The ID of the EMR Serverless Application.</td></tr>
<tr><td><code>worker_type_specifications</code></td><td><code>object</code></td><td>The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
<pre>
emr-serverless:GetApplication</pre>

### Update
<pre>
emr-serverless:UpdateApplication,
emr-serverless:TagResource,
emr-serverless:UntagResource,
emr-serverless:GetApplication,
ec2:CreateNetworkInterface,
ecr:BatchGetImage,
ecr:DescribeImages,
ecr:GetDownloadUrlForLayer,
kms:Create*,
kms:Describe*,
kms:Enable*,
kms:List*,
kms:Put*,
kms:Update*,
kms:Revoke*,
kms:Disable*,
kms:Get*,
kms:Delete*,
kms:ScheduleKeyDeletion,
kms:CancelKeyDeletion,
kms:GenerateDataKey,
kms:TagResource,
kms:UntagResource,
kms:Decrypt</pre>

### Delete
<pre>
emr-serverless:DeleteApplication,
emr-serverless:GetApplication</pre>


## Example
```sql
SELECT
region,
architecture,
name,
release_label,
type,
initial_capacity,
maximum_capacity,
tags,
auto_start_configuration,
auto_stop_configuration,
image_configuration,
monitoring_configuration,
runtime_configuration,
network_configuration,
arn,
application_id,
worker_type_specifications
FROM awscc.emrserverless.application
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ApplicationId&gt;'
```
