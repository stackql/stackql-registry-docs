---
title: api_key
hide_title: false
hide_table_of_contents: false
keywords:
  - api_key
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


Gets or updates an individual <code>api_key</code> resource, use <code>api_keys</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::APIKey Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.api_key" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="create_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="expire_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="force_update" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="key_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="key_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="no_expiry" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="restrictions" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="update_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="force_delete" /></td><td><code>boolean</code></td><td></td></tr>
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
create_time,
description,
expire_time,
force_update,
key_arn,
key_name,
no_expiry,
restrictions,
tags,
update_time,
force_delete,
arn
FROM aws.location.api_key
WHERE region = 'us-east-1' AND data__Identifier = '<KeyName>';
```


## Permissions

To operate on the <code>api_key</code> resource, the following permissions are required:

### Read
```json
geo:DescribeKey
```

### Update
```json
geo:CreateKey,
geo:DescribeKey,
geo:TagResource,
geo:UntagResource,
geo:GetMapTile,
geo:GetMapStyleDescriptor,
geo:GetMapSprites,
geo:GetMapGlyphs,
geo:SearchPlaceIndexForText,
geo:SearchPlaceIndexForPosition,
geo:SearchPlaceIndexForSuggestions,
geo:GetPlace,
geo:CalculateRoute,
geo:CalculateRouteMatrix,
geo:UpdateKey
```

