---
title: collection_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - collection_tags
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

Expands all tag keys and values for <code>collections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collection_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon OpenSearchServerless collection resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchserverless.collection_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the collection</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The identifier of the collection</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the collection.<br />The name must meet the following criteria:<br />Unique to your account and AWS Region<br />Starts with a lowercase letter<br />Contains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)<br />Contains between 3 and 32 characters<br /></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the collection.</td></tr>
<tr><td><CopyableCode code="collection_endpoint" /></td><td><code>string</code></td><td>The endpoint for the collection.</td></tr>
<tr><td><CopyableCode code="dashboard_endpoint" /></td><td><code>string</code></td><td>The OpenSearch Dashboards endpoint for the collection.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The possible types for the collection</td></tr>
<tr><td><CopyableCode code="standby_replicas" /></td><td><code>string</code></td><td>The possible standby replicas for the collection</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>collections</code> in a region.
```sql
SELECT
region,
description,
id,
name,
arn,
collection_endpoint,
dashboard_endpoint,
type,
standby_replicas,
tag_key,
tag_value
FROM aws.opensearchserverless.collection_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>collection_tags</code> resource, see <a href="/providers/aws/opensearchserverless/collections/#permissions"><code>collections</code></a>


