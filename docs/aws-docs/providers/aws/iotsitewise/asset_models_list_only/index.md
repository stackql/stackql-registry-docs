---
title: asset_models_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - asset_models_list_only
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

Lists <code>asset_models</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/asset_models/"><code>asset_models</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asset_models_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::AssetModel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.asset_models_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="asset_model_id" /></td><td><code>string</code></td><td>The ID of the asset model.</td></tr>
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
Lists all <code>asset_models</code> in a region.
```sql
SELECT
region,
asset_model_id
FROM aws.iotsitewise.asset_models_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>asset_models_list_only</code> resource, see <a href="/providers/aws/iotsitewise/asset_models/#permissions"><code>asset_models</code></a>

