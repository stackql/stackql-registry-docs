---
title: pipeline
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline
  - osis
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>pipeline</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>pipeline</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.osis.pipeline</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>buffer_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>encryption_at_rest_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>log_publishing_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>max_units</code></td><td><code>integer</code></td><td>The maximum pipeline capacity, in Ingestion Compute Units (ICUs).</td></tr>
<tr><td><code>min_units</code></td><td><code>integer</code></td><td>The minimum pipeline capacity, in Ingestion Compute Units (ICUs).</td></tr>
<tr><td><code>pipeline_configuration_body</code></td><td><code>string</code></td><td>The Data Prepper pipeline configuration in YAML format.</td></tr>
<tr><td><code>pipeline_name</code></td><td><code>string</code></td><td>Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>vpc_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>vpc_endpoints</code></td><td><code>array</code></td><td>The VPC interface endpoints that have access to the pipeline.</td></tr>
<tr><td><code>pipeline_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the pipeline.</td></tr>
<tr><td><code>ingest_endpoint_urls</code></td><td><code>array</code></td><td>A list of endpoints that can be used for ingesting data into a pipeline</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>pipeline</code> resource, the following permissions are required:

### Read
```json
osis:GetPipeline,
osis:ListTagsForResource
```

### Update
```json
osis:UpdatePipeline,
osis:GetPipeline,
osis:ListTagsForResource,
osis:TagResource,
osis:UntagResource,
iam:PassRole,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:ListLogDeliveries,
kms:DescribeKey
```

### Delete
```json
osis:DeletePipeline,
osis:GetPipeline,
logs:GetLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries
```


## Example
```sql
SELECT
region,
buffer_options,
encryption_at_rest_options,
log_publishing_options,
max_units,
min_units,
pipeline_configuration_body,
pipeline_name,
tags,
vpc_options,
vpc_endpoints,
pipeline_arn,
ingest_endpoint_urls
FROM awscc.osis.pipeline
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;PipelineArn&gt;'
```
