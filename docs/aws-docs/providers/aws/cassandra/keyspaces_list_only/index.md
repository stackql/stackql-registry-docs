---
title: keyspaces_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - keyspaces_list_only
  - cassandra
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

Lists <code>keyspaces</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/keyspaces/"><code>keyspaces</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keyspaces_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Cassandra::Keyspace</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cassandra.keyspaces_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="keyspace_name" /></td><td><code>string</code></td><td>Name for Cassandra keyspace</td></tr>
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
Lists all <code>keyspaces</code> in a region.
```sql
SELECT
region,
keyspace_name
FROM aws.cassandra.keyspaces_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>keyspaces_list_only</code> resource, see <a href="/providers/aws/cassandra/keyspaces/#permissions"><code>keyspaces</code></a>

