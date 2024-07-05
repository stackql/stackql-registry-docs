---
title: lists_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - lists_list_only
  - frauddetector
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

Lists <code>lists</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/lists/"><code>lists</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lists_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema for a List in Amazon Fraud Detector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.frauddetector.lists_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The list ARN.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the list.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the list.</td></tr>
<tr><td><CopyableCode code="variable_type" /></td><td><code>string</code></td><td>The variable type of the list.</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td>The time when the list was created.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>The time when the list was last updated.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags associated with this list.</td></tr>
<tr><td><CopyableCode code="elements" /></td><td><code>array</code></td><td>The elements in this list.</td></tr>
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
Lists all <code>lists</code> in a region.
```sql
SELECT
region,
arn
FROM aws.frauddetector.lists_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>lists_list_only</code> resource, see <a href="/providers/aws/frauddetector/lists/#permissions"><code>lists</code></a>


