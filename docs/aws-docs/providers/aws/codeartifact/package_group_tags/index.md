---
title: package_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - package_group_tags
  - codeartifact
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

Expands all tag keys and values for <code>package_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>package_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The resource schema to create a CodeArtifact package group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codeartifact.package_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The name of the domain that contains the package group.</td></tr>
<tr><td><CopyableCode code="domain_owner" /></td><td><code>string</code></td><td>The 12-digit account ID of the AWS account that owns the domain.</td></tr>
<tr><td><CopyableCode code="pattern" /></td><td><code>string</code></td><td>The package group pattern that is used to gather packages.</td></tr>
<tr><td><CopyableCode code="contact_info" /></td><td><code>string</code></td><td>The contact info of the package group.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The text description of the package group.</td></tr>
<tr><td><CopyableCode code="origin_configuration" /></td><td><code>object</code></td><td>The package origin configuration of the package group.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the package group.</td></tr>
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
Expands tags for all <code>package_groups</code> in a region.
```sql
SELECT
region,
domain_name,
domain_owner,
pattern,
contact_info,
description,
origin_configuration,
arn,
tag_key,
tag_value
FROM aws.codeartifact.package_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>package_group_tags</code> resource, see <a href="/providers/aws/codeartifact/package_groups/#permissions"><code>package_groups</code></a>


