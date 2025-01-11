---
title: vpc_connection_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_connection_tags
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

Expands all tag keys and values for <code>vpc_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connection_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::VpcConnection</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.vpc_connection_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="authentication" /></td><td><code>string</code></td><td>The type of private link authentication</td></tr>
<tr><td><CopyableCode code="client_subnets" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="target_cluster_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the target cluster</td></tr>
<tr><td><CopyableCode code="security_groups" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>vpc_connections</code> in a region.
```sql
SELECT
region,
arn,
authentication,
client_subnets,
target_cluster_arn,
security_groups,
vpc_id,
tag_key,
tag_value
FROM aws.msk.vpc_connection_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpc_connection_tags</code> resource, see <a href="/providers/aws/msk/vpc_connections/#permissions"><code>vpc_connections</code></a>

