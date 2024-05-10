---
title: dimension
hide_title: false
hide_table_of_contents: false
keywords:
  - dimension
  - iot
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


Gets or updates an individual <code>dimension</code> resource, use <code>dimensions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dimension</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A dimension can be used to limit the scope of a metric used in a security profile for AWS IoT Device Defender.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.dimension" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A unique identifier for the dimension.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Specifies the type of the dimension.</td></tr>
<tr><td><CopyableCode code="string_values" /></td><td><code>array</code></td><td>Specifies the value or list of values for the dimension.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Metadata that can be used to manage the dimension.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN (Amazon resource name) of the created dimension.</td></tr>
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
name,
type,
string_values,
tags,
arn
FROM aws.iot.dimension
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## Permissions

To operate on the <code>dimension</code> resource, the following permissions are required:

### Read
```json
iot:DescribeDimension,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateDimension,
iot:ListTagsForResource,
iot:UntagResource,
iot:TagResource
```

