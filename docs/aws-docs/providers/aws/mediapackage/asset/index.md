---
title: asset
hide_title: false
hide_table_of_contents: false
keywords:
  - asset
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


Gets or updates an individual <code>asset</code> resource, use <code>assets</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>asset</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::Asset</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.asset" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the Asset.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time the Asset was initially submitted for Ingest.</td></tr>
<tr><td><CopyableCode code="egress_endpoints" /></td><td><code>array</code></td><td>The list of egress endpoints available for the Asset.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifier for the Asset.</td></tr>
<tr><td><CopyableCode code="packaging_group_id" /></td><td><code>string</code></td><td>The ID of the PackagingGroup for the Asset.</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The resource ID to include in SPEKE key requests.</td></tr>
<tr><td><CopyableCode code="source_arn" /></td><td><code>string</code></td><td>ARN of the source object in S3.</td></tr>
<tr><td><CopyableCode code="source_role_arn" /></td><td><code>string</code></td><td>The IAM role_arn used to access the source S3 bucket.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
created_at,
egress_endpoints,
id,
packaging_group_id,
resource_id,
source_arn,
source_role_arn,
tags
FROM aws.mediapackage.asset
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## Permissions

To operate on the <code>asset</code> resource, the following permissions are required:

### Read
```json
mediapackage-vod:DescribeAsset
```

