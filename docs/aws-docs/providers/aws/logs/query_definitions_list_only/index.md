---
title: query_definitions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - query_definitions_list_only
  - logs
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

Lists <code>query_definitions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/query_definitions/"><code>query_definitions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>query_definitions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The resource schema for AWSLogs QueryDefinition</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.query_definitions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the saved query definition</td></tr>
<tr><td><CopyableCode code="query_string" /></td><td><code>string</code></td><td>The query string to use for this definition</td></tr>
<tr><td><CopyableCode code="log_group_names" /></td><td><code>array</code></td><td>Optionally define specific log groups as part of your query definition</td></tr>
<tr><td><CopyableCode code="query_definition_id" /></td><td><code>string</code></td><td>Unique identifier of a query definition</td></tr>
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
Lists all <code>query_definitions</code> in a region.
```sql
SELECT
region,
query_definition_id
FROM aws.logs.query_definitions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>query_definitions_list_only</code> resource, see <a href="/providers/aws/logs/query_definitions/#permissions"><code>query_definitions</code></a>


