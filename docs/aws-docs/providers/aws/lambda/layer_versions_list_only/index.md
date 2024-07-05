---
title: layer_versions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - layer_versions_list_only
  - lambda
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

Lists <code>layer_versions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/layer_versions/"><code>layer_versions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>layer_versions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lambda::LayerVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.layer_versions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="compatible_runtimes" /></td><td><code>array</code></td><td>A list of compatible function runtimes. Used for filtering with ListLayers and ListLayerVersions.</td></tr>
<tr><td><CopyableCode code="license_info" /></td><td><code>string</code></td><td>The layer's software license.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the version.</td></tr>
<tr><td><CopyableCode code="layer_name" /></td><td><code>string</code></td><td>The name or Amazon Resource Name (ARN) of the layer.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>object</code></td><td>The function layer archive.</td></tr>
<tr><td><CopyableCode code="layer_version_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="compatible_architectures" /></td><td><code>array</code></td><td>A list of compatible instruction set architectures.</td></tr>
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
Lists all <code>layer_versions</code> in a region.
```sql
SELECT
region,
layer_version_arn
FROM aws.lambda.layer_versions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>layer_versions_list_only</code> resource, see <a href="/providers/aws/lambda/layer_versions/#permissions"><code>layer_versions</code></a>


