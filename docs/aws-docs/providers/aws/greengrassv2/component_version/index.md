---
title: component_version
hide_title: false
hide_table_of_contents: false
keywords:
  - component_version
  - greengrassv2
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


Gets or updates an individual <code>component_version</code> resource, use <code>component_versions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource for Greengrass component version.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.greengrassv2.component_version" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="component_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="component_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="inline_recipe" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="lambda_function" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
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
arn,
component_name,
component_version,
inline_recipe,
lambda_function,
tags
FROM aws.greengrassv2.component_version
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>component_version</code> resource, the following permissions are required:

### Read
```json
greengrass:DescribeComponent,
greengrass:ListTagsForResource
```

### Update
```json
greengrass:DescribeComponent,
greengrass:ListTagsForResource,
greengrass:TagResource,
greengrass:UntagResource
```

