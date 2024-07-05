---
title: faqs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - faqs_list_only
  - kendra
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

Lists <code>faqs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/faqs/"><code>faqs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>faqs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A Kendra FAQ resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kendra.faqs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Unique ID of index</td></tr>
<tr><td><CopyableCode code="index_id" /></td><td><code>string</code></td><td>Index ID</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>FAQ name</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>FAQ description</td></tr>
<tr><td><CopyableCode code="file_format" /></td><td><code>string</code></td><td>FAQ file format</td></tr>
<tr><td><CopyableCode code="s3_path" /></td><td><code>object</code></td><td>FAQ S3 path</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>FAQ role ARN</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags for labeling the FAQ</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="language_code" /></td><td><code>string</code></td><td>The code for a language.</td></tr>
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
Lists all <code>faqs</code> in a region.
```sql
SELECT
region,
id,
index_id
FROM aws.kendra.faqs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>faqs_list_only</code> resource, see <a href="/providers/aws/kendra/faqs/#permissions"><code>faqs</code></a>


