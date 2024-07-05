---
title: assets_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - assets_list_only
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

Lists <code>assets</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/assets/"><code>assets</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::Asset</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.assets_list_only" /></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>assets</code> in a region.
```sql
SELECT
region,
id
FROM aws.mediapackage.assets_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>assets_list_only</code> resource, see <a href="/providers/aws/mediapackage/assets/#permissions"><code>assets</code></a>


