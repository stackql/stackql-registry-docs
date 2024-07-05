---
title: pipeline_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_tags
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

Expands all tag keys and values for <code>pipelines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An OpenSearch Ingestion Service Data Prepper pipeline running Data Prepper.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.osis.pipeline_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="buffer_options" /></td><td><code>object</code></td><td>Key-value pairs to configure buffering.</td></tr>
<tr><td><CopyableCode code="encryption_at_rest_options" /></td><td><code>object</code></td><td>Key-value pairs to configure encryption at rest.</td></tr>
<tr><td><CopyableCode code="log_publishing_options" /></td><td><code>object</code></td><td>Key-value pairs to configure log publishing.</td></tr>
<tr><td><CopyableCode code="max_units" /></td><td><code>integer</code></td><td>The maximum pipeline capacity, in Ingestion OpenSearch Compute Units (OCUs).</td></tr>
<tr><td><CopyableCode code="min_units" /></td><td><code>integer</code></td><td>The minimum pipeline capacity, in Ingestion OpenSearch Compute Units (OCUs).</td></tr>
<tr><td><CopyableCode code="pipeline_configuration_body" /></td><td><code>string</code></td><td>The Data Prepper pipeline configuration.</td></tr>
<tr><td><CopyableCode code="pipeline_name" /></td><td><code>string</code></td><td>Name of the OpenSearch Ingestion Service pipeline to create. Pipeline names are unique across the pipelines owned by an account within an AWS Region.</td></tr>
<tr><td><CopyableCode code="vpc_options" /></td><td><code>object</code></td><td>Container for the values required to configure VPC access for the pipeline. If you don't specify these values, OpenSearch Ingestion Service creates the pipeline with a public endpoint.</td></tr>
<tr><td><CopyableCode code="vpc_endpoints" /></td><td><code>array</code></td><td>The VPC interface endpoints that have access to the pipeline.</td></tr>
<tr><td><CopyableCode code="pipeline_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the pipeline.</td></tr>
<tr><td><CopyableCode code="ingest_endpoint_urls" /></td><td><code>array</code></td><td>A list of endpoints that can be used for ingesting data into a pipeline</td></tr>
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
Expands tags for all <code>pipelines</code> in a region.
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
vpc_options,
vpc_endpoints,
pipeline_arn,
ingest_endpoint_urls,
tag_key,
tag_value
FROM aws.osis.pipeline_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>pipeline_tags</code> resource, see <a href="/providers/aws/osis/pipelines/#permissions"><code>pipelines</code></a>


