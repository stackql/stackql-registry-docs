---
title: api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - api_keys
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

Used to retrieve a list of <code>api_keys</code> in a region or create a <code>api_keys</code> resource, use <code>api_key</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::APIKey Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.api_keys" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="key_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
key_name
FROM aws.location.api_keys
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>api_keys</code> resource, the following permissions are required:

### Create
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
geo:CalculateRouteMatrix
```

### List
```json
geo:ListKeys
```

