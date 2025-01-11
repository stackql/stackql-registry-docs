---
title: queue_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - queue_tags
  - pcs
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

Expands all tag keys and values for <code>queues</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::PCS::Queue resource creates an AWS PCS queue.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcs.queue_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The unique Amazon Resource Name (ARN) of the queue.</td></tr>
<tr><td><CopyableCode code="cluster_id" /></td><td><code>string</code></td><td>The ID of the cluster of the queue.</td></tr>
<tr><td><CopyableCode code="compute_node_group_configurations" /></td><td><code>array</code></td><td>The list of compute node group configurations associated with the queue. Queues assign jobs to associated compute node groups.</td></tr>
<tr><td><CopyableCode code="error_info" /></td><td><code>array</code></td><td>The list of errors that occurred during queue provisioning.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The generated unique ID of the queue.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name that identifies the queue.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The provisioning status of the queue. The provisioning status doesn't indicate the overall health of the queue.</td></tr>
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
Expands tags for all <code>queues</code> in a region.
```sql
SELECT
region,
arn,
cluster_id,
compute_node_group_configurations,
error_info,
id,
name,
status,
tag_key,
tag_value
FROM aws.pcs.queue_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>queue_tags</code> resource, see <a href="/providers/aws/pcs/queues/#permissions"><code>queues</code></a>

