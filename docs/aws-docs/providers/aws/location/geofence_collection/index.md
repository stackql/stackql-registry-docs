---
title: geofence_collection
hide_title: false
hide_table_of_contents: false
keywords:
  - geofence_collection
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


Gets or updates an individual <code>geofence_collection</code> resource, use <code>geofence_collections</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>geofence_collection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::GeofenceCollection Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.geofence_collection" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="collection_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collection_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="create_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pricing_plan" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pricing_plan_data_source" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="update_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
tags,
update_time,
arn
FROM aws.location.geofence_collection
WHERE region = 'us-east-1' AND data__Identifier = '<CollectionName>';
```


## Permissions

To operate on the <code>geofence_collection</code> resource, the following permissions are required:

### Read
```json
geo:DescribeGeofenceCollection,
kms:DescribeKey
```

### Update
```json
geo:CreateGeofenceCollection,
geo:DescribeGeofenceCollection,
geo:TagResource,
geo:UntagResource,
kms:DescribeKey,
kms:CreateGrant,
geo:UpdateGeofenceCollection
```

