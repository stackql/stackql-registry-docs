---
title: collections_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - collections_list_only
  - opensearchserverless
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

Lists <code>collections</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/collections/"><code>collections</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collections_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon OpenSearchServerless collection resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchserverless.collections_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the collection</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The identifier of the collection</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the collection.<br />The name must meet the following criteria:<br />Unique to your account and AWS Region<br />Starts with a lowercase letter<br />Contains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)<br />Contains between 3 and 32 characters<br /></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>List of tags to be added to the resource</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the collection.</td></tr>
<tr><td><CopyableCode code="collection_endpoint" /></td><td><code>string</code></td><td>The endpoint for the collection.</td></tr>
<tr><td><CopyableCode code="dashboard_endpoint" /></td><td><code>string</code></td><td>The OpenSearch Dashboards endpoint for the collection.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The possible types for the collection</td></tr>
<tr><td><CopyableCode code="standby_replicas" /></td><td><code>string</code></td><td>The possible standby replicas for the collection</td></tr>
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
Lists all <code>collections</code> in a region.
```sql
SELECT
region,
id
FROM aws.opensearchserverless.collections_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>collections_list_only</code> resource, see <a href="/providers/aws/opensearchserverless/collections/#permissions"><code>collections</code></a>


