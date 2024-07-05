---
title: cluster_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_tags
  - msk
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

Expands all tag keys and values for <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::Cluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.cluster_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="broker_node_group_info" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="enhanced_monitoring" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="kafka_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="number_of_broker_nodes" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="encryption_info" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="open_monitoring" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="current_version" /></td><td><code>string</code></td><td>The current version of the MSK cluster</td></tr>
<tr><td><CopyableCode code="client_authentication" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="logging_info" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="configuration_info" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="storage_mode" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>clusters</code> in a region.
```sql
SELECT
region,
broker_node_group_info,
enhanced_monitoring,
kafka_version,
number_of_broker_nodes,
encryption_info,
open_monitoring,
cluster_name,
arn,
current_version,
client_authentication,
logging_info,
configuration_info,
storage_mode,
tag_key,
tag_value
FROM aws.msk.cluster_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>cluster_tags</code> resource, see <a href="/providers/aws/msk/clusters/#permissions"><code>clusters</code></a>


