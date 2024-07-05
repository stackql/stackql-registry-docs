---
title: geofence_collection_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - geofence_collection_tags
  - location
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

Expands all tag keys and values for <code>geofence_collections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>geofence_collection_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::GeofenceCollection Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.geofence_collection_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="collection_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collection_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="create_time" /></td><td><code>string</code></td><td>The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pricing_plan" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pricing_plan_data_source" /></td><td><code>string</code></td><td>This shape is deprecated since 2022-02-01: Deprecated. No longer allowed.</td></tr>
<tr><td><CopyableCode code="update_time" /></td><td><code>string</code></td><td>The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>geofence_collections</code> in a region.
```sql
SELECT
region,
collection_arn,
collection_name,
create_time,
description,
kms_key_id,
pricing_plan,
pricing_plan_data_source,
update_time,
arn,
tag_key,
tag_value
FROM aws.location.geofence_collection_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>geofence_collection_tags</code> resource, see <a href="/providers/aws/location/geofence_collections/#permissions"><code>geofence_collections</code></a>


