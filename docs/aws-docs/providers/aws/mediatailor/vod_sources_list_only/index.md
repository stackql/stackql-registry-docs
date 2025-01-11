---
title: vod_sources_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - vod_sources_list_only
  - mediatailor
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

Lists <code>vod_sources</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/vod_sources/"><code>vod_sources</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vod_sources_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::VodSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.vod_sources_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="source_location_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vod_source_name" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>vod_sources</code> in a region.
```sql
SELECT
region,
source_location_name,
vod_source_name
FROM aws.mediatailor.vod_sources_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vod_sources_list_only</code> resource, see <a href="/providers/aws/mediatailor/vod_sources/#permissions"><code>vod_sources</code></a>

