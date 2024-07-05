---
title: software_package_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - software_package_tags
  - iot
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

Expands all tag keys and values for <code>software_packages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>software_package_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource definition</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.software_package_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="package_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="package_name" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>software_packages</code> in a region.
```sql
SELECT
region,
description,
package_arn,
package_name,
tag_key,
tag_value
FROM aws.iot.software_package_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>software_package_tags</code> resource, see <a href="/providers/aws/iot/software_packages/#permissions"><code>software_packages</code></a>


