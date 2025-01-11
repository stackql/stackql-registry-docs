---
title: package_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - package_tags
  - panorama
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

Expands all tag keys and values for <code>packages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>package_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a package and storage location in an Amazon S3 access point.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.panorama.package_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="package_name" /></td><td><code>string</code></td><td>A name for the package.</td></tr>
<tr><td><CopyableCode code="package_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="storage_location" /></td><td><code>object</code></td><td>A storage location.</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>integer</code></td><td></td></tr>
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
Expands tags for all <code>packages</code> in a region.
```sql
SELECT
region,
package_name,
package_id,
arn,
storage_location,
created_time,
tag_key,
tag_value
FROM aws.panorama.package_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>package_tags</code> resource, see <a href="/providers/aws/panorama/packages/#permissions"><code>packages</code></a>

