---
title: configured_tables_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - configured_tables_list_only
  - cleanrooms
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

Lists <code>configured_tables</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/configured_tables/"><code>configured_tables</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configured_tables_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a table that can be associated with collaborations</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.configured_tables_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.</td></tr>
<tr><td><CopyableCode code="allowed_columns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="analysis_method" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="configured_table_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="analysis_rules" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="table_reference" /></td><td><code>object</code></td><td></td></tr>
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
Lists all <code>configured_tables</code> in a region.
```sql
SELECT
region,
configured_table_identifier
FROM aws.cleanrooms.configured_tables_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>configured_tables_list_only</code> resource, see <a href="/providers/aws/cleanrooms/configured_tables/#permissions"><code>configured_tables</code></a>


