---
title: view_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - view_tags
  - connect
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

Expands all tag keys and values for <code>views</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>view_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::View</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.view_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the instance.</td></tr>
<tr><td><CopyableCode code="view_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the view.</td></tr>
<tr><td><CopyableCode code="view_id" /></td><td><code>string</code></td><td>The view id of the view.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the view.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the view.</td></tr>
<tr><td><CopyableCode code="template" /></td><td><code>object</code></td><td>The template of the view as JSON.</td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>array</code></td><td>The actions of the view in an array.</td></tr>
<tr><td><CopyableCode code="view_content_sha256" /></td><td><code>string</code></td><td>The view content hash.</td></tr>
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
Expands tags for all <code>views</code> in a region.
```sql
SELECT
region,
instance_arn,
view_arn,
view_id,
name,
description,
template,
actions,
view_content_sha256,
tag_key,
tag_value
FROM aws.connect.view_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>view_tags</code> resource, see <a href="/providers/aws/connect/views/#permissions"><code>views</code></a>


