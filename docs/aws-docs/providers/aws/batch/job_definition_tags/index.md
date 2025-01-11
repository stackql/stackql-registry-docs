---
title: job_definition_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - job_definition_tags
  - batch
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

Expands all tag keys and values for <code>job_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_definition_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Batch::JobDefinition</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.batch.job_definition_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="timeout" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="job_definition_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="propagate_tags" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="platform_capabilities" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="eks_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="node_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="scheduling_priority" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="container_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="ecs_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="retry_strategy" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>job_definitions</code> in a region.
```sql
SELECT
region,
parameters,
timeout,
job_definition_name,
propagate_tags,
platform_capabilities,
eks_properties,
type,
node_properties,
scheduling_priority,
container_properties,
ecs_properties,
retry_strategy,
tag_key,
tag_value
FROM aws.batch.job_definition_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>job_definition_tags</code> resource, see <a href="/providers/aws/batch/job_definitions/#permissions"><code>job_definitions</code></a>

