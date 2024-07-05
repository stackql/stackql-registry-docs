---
title: traffic_distribution_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_distribution_group_tags
  - connect
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

Expands all tag keys and values for <code>traffic_distribution_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>traffic_distribution_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::TrafficDistributionGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.traffic_distribution_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance that has been replicated.</td></tr>
<tr><td><CopyableCode code="traffic_distribution_group_arn" /></td><td><code>string</code></td><td>The identifier of the traffic distribution group.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the traffic distribution group.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the traffic distribution group.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the traffic distribution group.</td></tr>
<tr><td><CopyableCode code="is_default" /></td><td><code>boolean</code></td><td>If this is the default traffic distribution group.</td></tr>
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
Expands tags for all <code>traffic_distribution_groups</code> in a region.
```sql
SELECT
region,
instance_arn,
traffic_distribution_group_arn,
description,
name,
status,
is_default,
tag_key,
tag_value
FROM aws.connect.traffic_distribution_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>traffic_distribution_group_tags</code> resource, see <a href="/providers/aws/connect/traffic_distribution_groups/#permissions"><code>traffic_distribution_groups</code></a>


