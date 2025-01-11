---
title: asset_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - asset_tags
  - mediapackage
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
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::Asset</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.asset_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the Asset.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time the Asset was initially submitted for Ingest.</td></tr>
<tr><td><CopyableCode code="egress_endpoints" /></td><td><code>array</code></td><td>The list of egress endpoints available for the Asset.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifier for the Asset.</td></tr>
<tr><td><CopyableCode code="packaging_group_id" /></td><td><code>string</code></td><td>The ID of the PackagingGroup for the Asset.</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The resource ID to include in SPEKE key requests.</td></tr>
<tr><td><CopyableCode code="source_arn" /></td><td><code>string</code></td><td>ARN of the source object in S3.</td></tr>
<tr><td><CopyableCode code="source_role_arn" /></td><td><code>string</code></td><td>The IAM role_arn used to access the source S3 bucket.</td></tr>
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
arn,
created_at,
egress_endpoints,
id,
packaging_group_id,
resource_id,
source_arn,
source_role_arn,
tag_key,
tag_value
FROM aws.mediapackage.asset_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>asset_tags</code> resource, see <a href="/providers/aws/mediapackage/assets/#permissions"><code>assets</code></a>

