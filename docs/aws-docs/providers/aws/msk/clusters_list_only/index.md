---
title: clusters_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_list_only
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

Lists <code>clusters</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/clusters/"><code>clusters</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::Cluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.clusters_list_only" /></td></tr>
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
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><CopyableCode code="configuration_info" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="storage_mode" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>clusters</code> in a region.
```sql
SELECT
region,
arn
FROM aws.msk.clusters_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>clusters_list_only</code> resource, see <a href="/providers/aws/msk/clusters/#permissions"><code>clusters</code></a>


