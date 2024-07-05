---
title: pipe_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - pipe_tags
  - pipes
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

Expands all tag keys and values for <code>pipes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipe_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Pipes::Pipe Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pipes.pipe_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="current_state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="desired_state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enrichment" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enrichment_parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="log_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="state_reason" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="target" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="target_parameters" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>pipes</code> in a region.
```sql
SELECT
region,
arn,
creation_time,
current_state,
description,
desired_state,
enrichment,
enrichment_parameters,
last_modified_time,
log_configuration,
name,
role_arn,
source,
source_parameters,
state_reason,
target,
target_parameters,
tag_key,
tag_value
FROM aws.pipes.pipe_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>pipe_tags</code> resource, see <a href="/providers/aws/pipes/pipes/#permissions"><code>pipes</code></a>


