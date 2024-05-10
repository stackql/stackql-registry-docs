---
title: view
hide_title: false
hide_table_of_contents: false
keywords:
  - view
  - resourceexplorer2
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


Gets or updates an individual <code>view</code> resource, use <code>views</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>view</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ResourceExplorer2::View Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.resourceexplorer2.view" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="filters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="included_properties" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="view_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="view_name" /></td><td><code>string</code></td><td></td></tr>
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
filters,
included_properties,
scope,
tags,
view_arn,
view_name
FROM aws.resourceexplorer2.view
WHERE region = 'us-east-1' AND data__Identifier = '<ViewArn>';
```


## Permissions

To operate on the <code>view</code> resource, the following permissions are required:

### Read
```json
resource-explorer-2:GetView
```

### Update
```json
resource-explorer-2:UpdateView,
resource-explorer-2:TagResource,
resource-explorer-2:UntagResource,
resource-explorer-2:ListTagsForResource
```

