---
title: realtime_log_configs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - realtime_log_configs_list_only
  - cloudfront
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

Lists <code>realtime_log_configs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/realtime_log_configs/"><code>realtime_log_configs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>realtime_log_configs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A real-time log configuration.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.realtime_log_configs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>realtime_log_configs</code> in a region.
```sql
SELECT
region,
arn
FROM aws.cloudfront.realtime_log_configs_list_only
;
```


## Permissions

For permissions required to operate on the <code>realtime_log_configs_list_only</code> resource, see <a href="/providers/aws/cloudfront/realtime_log_configs/#permissions"><code>realtime_log_configs</code></a>

