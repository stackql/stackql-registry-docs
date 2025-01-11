---
title: storage_configuration_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_configuration_tags
  - ivs
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

Expands all tag keys and values for <code>storage_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_configuration_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::StorageConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.storage_configuration_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Storage Configuration ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Storage Configuration Name.</td></tr>
<tr><td><CopyableCode code="s3" /></td><td><code>object</code></td><td>A complex type that describes an S3 location where recorded videos will be stored.</td></tr>
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
Expands tags for all <code>storage_configurations</code> in a region.
```sql
SELECT
region,
arn,
name,
s3,
tag_key,
tag_value
FROM aws.ivs.storage_configuration_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>storage_configuration_tags</code> resource, see <a href="/providers/aws/ivs/storage_configurations/#permissions"><code>storage_configurations</code></a>

