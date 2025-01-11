---
title: data_sources_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources_list_only
  - datazone
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

Lists <code>data_sources</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/data_sources/"><code>data_sources</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A data source is used to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.data_sources_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain where the data source is created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifier of the data source.</td></tr>
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
Lists all <code>data_sources</code> in a region.
```sql
SELECT
region,
domain_id,
id
FROM aws.datazone.data_sources_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>data_sources_list_only</code> resource, see <a href="/providers/aws/datazone/data_sources/#permissions"><code>data_sources</code></a>

