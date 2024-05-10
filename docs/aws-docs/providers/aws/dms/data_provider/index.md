---
title: data_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - data_provider
  - dms
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


Gets or updates an individual <code>data_provider</code> resource, use <code>data_providers</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DMS::DataProvider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.data_provider" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="data_provider_name" /></td><td><code>string</code></td><td>The property describes a name to identify the data provider.</td></tr>
<tr><td><CopyableCode code="data_provider_identifier" /></td><td><code>string</code></td><td>The property describes an identifier for the data provider. It is used for describing&#x2F;deleting&#x2F;modifying can be name&#x2F;arn</td></tr>
<tr><td><CopyableCode code="data_provider_arn" /></td><td><code>string</code></td><td>The data provider ARN.</td></tr>
<tr><td><CopyableCode code="data_provider_creation_time" /></td><td><code>string</code></td><td>The data provider creation time.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The optional description of the data provider.</td></tr>
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>The property describes a data engine for the data provider.</td></tr>
<tr><td><CopyableCode code="exact_settings" /></td><td><code>boolean</code></td><td>The property describes the exact settings which can be modified</td></tr>
<tr><td><CopyableCode code="settings" /></td><td><code>object</code></td><td>The property identifies the exact type of settings for the data provider.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
data_provider_name,
data_provider_identifier,
data_provider_arn,
data_provider_creation_time,
description,
engine,
exact_settings,
settings,
tags
FROM aws.dms.data_provider
WHERE region = 'us-east-1' AND data__Identifier = '<DataProviderArn>';
```


## Permissions

To operate on the <code>data_provider</code> resource, the following permissions are required:

### Read
```json
dms:ListDataProviders,
dms:DescribeDataProviders,
dms:ListTagsForResource
```

### Update
```json
dms:UpdateDataProvider,
dms:ModifyDataProvider,
dms:AddTagsToResource,
dms:RemoveTagsToResource,
dms:ListTagsForResource
```

