---
title: tables_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - tables_list_only
  - timestream
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

Lists <code>tables</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/tables/"><code>tables</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Timestream::Table resource creates a Timestream Table.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.timestream.tables_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The table name exposed as a read-only attribute.</td></tr>
<tr><td><CopyableCode code="database_name" /></td><td><code>string</code></td><td>The name for the database which the table to be created belongs to.</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td>The name for the table. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the table name.</td></tr>
<tr><td><CopyableCode code="retention_properties" /></td><td><code>object</code></td><td>The retention duration of the memory store and the magnetic store.</td></tr>
<tr><td><CopyableCode code="schema" /></td><td><code>object</code></td><td>A Schema specifies the expected data model of the table.</td></tr>
<tr><td><CopyableCode code="magnetic_store_write_properties" /></td><td><code>object</code></td><td>The properties that determine whether magnetic store writes are enabled.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
Lists all <code>tables</code> in a region.
```sql
SELECT
region,
database_name,
table_name
FROM aws.timestream.tables_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>tables_list_only</code> resource, see <a href="/providers/aws/timestream/tables/#permissions"><code>tables</code></a>


