---
title: packaging_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - packaging_group_tags
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

Expands all tag keys and values for <code>packaging_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packaging_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::PackagingGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.packaging_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the PackagingGroup.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the PackagingGroup.</td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The fully qualified domain name for Assets in the PackagingGroup.</td></tr>
<tr><td><CopyableCode code="authorization" /></td><td><code>object</code></td><td>CDN Authorization</td></tr>
<tr><td><CopyableCode code="egress_access_logs" /></td><td><code>object</code></td><td>The configuration parameters for egress access logging.</td></tr>
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
Expands tags for all <code>packaging_groups</code> in a region.
```sql
SELECT
region,
id,
arn,
domain_name,
authorization,
egress_access_logs,
tag_key,
tag_value
FROM aws.mediapackage.packaging_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>packaging_group_tags</code> resource, see <a href="/providers/aws/mediapackage/packaging_groups/#permissions"><code>packaging_groups</code></a>


