---
title: data_cells_filters_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - data_cells_filters_list_only
  - lakeformation
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

Lists <code>data_cells_filters</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/data_cells_filters/"><code>data_cells_filters</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_cells_filters_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema representing a Lake Formation Data Cells Filter.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lakeformation.data_cells_filters_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="table_catalog_id" /></td><td><code>string</code></td><td>The Catalog Id of the Table on which to create a Data Cells Filter.</td></tr>
<tr><td><CopyableCode code="database_name" /></td><td><code>string</code></td><td>The name of the Database that the Table resides in.</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td>The name of the Table to create a Data Cells Filter for.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The desired name of the Data Cells Filter.</td></tr>
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
Lists all <code>data_cells_filters</code> in a region.
```sql
SELECT
region,
table_catalog_id,
database_name,
table_name,
name
FROM aws.lakeformation.data_cells_filters_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>data_cells_filters_list_only</code> resource, see <a href="/providers/aws/lakeformation/data_cells_filters/#permissions"><code>data_cells_filters</code></a>

