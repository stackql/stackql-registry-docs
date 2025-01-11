---
title: named_queries_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - named_queries_list_only
  - athena
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

Lists <code>named_queries</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/named_queries/"><code>named_queries</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>named_queries_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::NamedQuery</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.athena.named_queries_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The query name.</td></tr>
<tr><td><CopyableCode code="named_query_id" /></td><td><code>string</code></td><td>The unique ID of the query.</td></tr>
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
Lists all <code>named_queries</code> in a region.
```sql
SELECT
region,
named_query_id
FROM aws.athena.named_queries_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>named_queries_list_only</code> resource, see <a href="/providers/aws/athena/named_queries/#permissions"><code>named_queries</code></a>

