--- 
title: results
hide_title: false
hide_table_of_contents: false
keywords:
  - results
  - result
  - snowflake
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage snowflake resources using SQL
custom_edit_url: null
image: /img/providers/snowflake/stackql-snowflake-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.result.results" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#fetch_result"><CopyableCode code="fetch_result" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-result_handler"><code>result_handler</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-page"><code>page</code></a></td>
    <td>Get result status or the result when it is ready.</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
<tr id="parameter-result_handler">
    <td><CopyableCode code="result_handler" /></td>
    <td><code>string</code></td>
    <td>The opaque result id.</td>
</tr>
<tr id="parameter-page">
    <td><CopyableCode code="page" /></td>
    <td><code>integer (int64)</code></td>
    <td>Number of the page of results to return. The number can range from 0 to the total number of pages minus 1.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="fetch_result"
    values={[
        { label: 'fetch_result', value: 'fetch_result' }
    ]}
>
<TabItem value="fetch_result">

Get result status or the result when it is ready.

```sql
EXEC snowflake.result.results.fetch_result 
@result_handler='{{ result_handler }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@page='{{ page }}';
```
</TabItem>
</Tabs>
