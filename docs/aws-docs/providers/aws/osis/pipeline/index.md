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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>pipeline</code> resource, use <code>pipelines</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An OpenSearch Ingestion Service Data Prepper pipeline running Data Prepper.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.osis.pipeline" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="buffer_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="encryption_at_rest_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="log_publishing_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="max_units" /></td><td><code>integer</code></td><td>The maximum pipeline capacity, in Ingestion OpenSearch Compute Units (OCUs).</td></tr>
<tr><td><CopyableCode code="min_units" /></td><td><code>integer</code></td><td>The minimum pipeline capacity, in Ingestion OpenSearch Compute Units (OCUs).</td></tr>
<tr><td><CopyableCode code="pipeline_configuration_body" /></td><td><code>string</code></td><td>The Data Prepper pipeline configuration.</td></tr>
<tr><td><CopyableCode code="pipeline_name" /></td><td><code>string</code></td><td>Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="vpc_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_endpoints" /></td><td><code>array</code></td><td>The VPC interface endpoints that have access to the pipeline.</td></tr>
<tr><td><CopyableCode code="pipeline_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the pipeline.</td></tr>
<tr><td><CopyableCode code="ingest_endpoint_urls" /></td><td><code>array</code></td><td>A list of endpoints that can be used for ingesting data into a pipeline</td></tr>
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
FROM aws.osis.pipeline
WHERE region = 'us-east-1' AND data__Identifier = '<PipelineArn>';
```


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

