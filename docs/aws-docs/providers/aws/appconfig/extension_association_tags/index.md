---
title: extension_association_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - extension_association_tags
  - appconfig
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

Expands all tag keys and values for <code>extension_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extension_association_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.extension_association_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="extension_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="extension_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="extension_version_number" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>extension_associations</code> in a region.
```sql
SELECT
region,
id,
arn,
extension_arn,
resource_arn,
extension_identifier,
resource_identifier,
extension_version_number,
parameters,
tag_key,
tag_value
FROM aws.appconfig.extension_association_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>extension_association_tags</code> resource, see <a href="/providers/aws/appconfig/extension_associations/#permissions"><code>extension_associations</code></a>


