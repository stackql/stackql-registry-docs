---
title: campaign
hide_title: false
hide_table_of_contents: false
keywords:
  - campaign
  - iotfleetwise
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

Gets or operates on an individual <code>campaign</code> resource, use <code>campaigns</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>campaign</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::Campaign Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleetwise.campaign" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="action" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="compression" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="priority" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="signals_to_collect" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="data_destination_configs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="start_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="expiry_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modification_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="spooling_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="signal_catalog_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="post_trigger_collection_duration" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="data_extra_dimensions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="diagnostics_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="target_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collection_scheme" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
status,
action,
creation_time,
compression,
description,
priority,
signals_to_collect,
data_destination_configs,
start_time,
name,
expiry_time,
last_modification_time,
spooling_mode,
signal_catalog_arn,
post_trigger_collection_duration,
data_extra_dimensions,
diagnostics_mode,
target_arn,
arn,
collection_scheme,
tags
FROM aws.iotfleetwise.campaign
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>campaign</code> resource, the following permissions are required:

### Read
```json
iotfleetwise:GetCampaign,
iotfleetwise:ListTagsForResource
```

### Update
```json
iotfleetwise:GetCampaign,
iotfleetwise:ListTagsForResource,
iotfleetwise:UpdateCampaign,
iotfleetwise:TagResource,
iotfleetwise:UntagResource
```

### Delete
```json
iotfleetwise:DeleteCampaign,
iotfleetwise:GetCampaign
```

