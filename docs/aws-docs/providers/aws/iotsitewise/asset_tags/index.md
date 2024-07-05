---
title: asset_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - asset_tags
  - iotsitewise
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

Expands all tag keys and values for <code>assets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asset_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::Asset</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.asset_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="asset_id" /></td><td><code>string</code></td><td>The ID of the asset</td></tr>
<tr><td><CopyableCode code="asset_external_id" /></td><td><code>string</code></td><td>The External ID of the asset</td></tr>
<tr><td><CopyableCode code="asset_model_id" /></td><td><code>string</code></td><td>The ID of the asset model from which to create the asset.</td></tr>
<tr><td><CopyableCode code="asset_arn" /></td><td><code>string</code></td><td>The ARN of the asset</td></tr>
<tr><td><CopyableCode code="asset_name" /></td><td><code>string</code></td><td>A unique, friendly name for the asset.</td></tr>
<tr><td><CopyableCode code="asset_description" /></td><td><code>string</code></td><td>A description for the asset</td></tr>
<tr><td><CopyableCode code="asset_properties" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="asset_hierarchies" /></td><td><code>array</code></td><td></td></tr>
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
Expands tags for all <code>assets</code> in a region.
```sql
SELECT
region,
asset_id,
asset_external_id,
asset_model_id,
asset_arn,
asset_name,
asset_description,
asset_properties,
asset_hierarchies,
tag_key,
tag_value
FROM aws.iotsitewise.asset_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>asset_tags</code> resource, see <a href="/providers/aws/iotsitewise/assets/#permissions"><code>assets</code></a>


