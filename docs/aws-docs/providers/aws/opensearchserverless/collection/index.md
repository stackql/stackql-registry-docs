---
title: collection
hide_title: false
hide_table_of_contents: false
keywords:
  - collection
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


Gets or updates an individual <code>collection</code> resource, use <code>collections</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon OpenSearchServerless collection resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchserverless.collection" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the collection</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The identifier of the collection</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the collection.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;The name must meet the following criteria:&lt;br&#x2F;&gt;Unique to your account and AWS Region&lt;br&#x2F;&gt;Starts with a lowercase letter&lt;br&#x2F;&gt;Contains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)&lt;br&#x2F;&gt;Contains between 3 and 32 characters&lt;br&#x2F;&gt;</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>List of tags to be added to the resource</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the collection.</td></tr>
<tr><td><CopyableCode code="collection_endpoint" /></td><td><code>string</code></td><td>The endpoint for the collection.</td></tr>
<tr><td><CopyableCode code="dashboard_endpoint" /></td><td><code>string</code></td><td>The OpenSearch Dashboards endpoint for the collection.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="standby_replicas" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
description,
id,
name,
tags,
arn,
collection_endpoint,
dashboard_endpoint,
type,
standby_replicas
FROM aws.opensearchserverless.collection
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## Permissions

To operate on the <code>collection</code> resource, the following permissions are required:

### Read
```json
aoss:BatchGetCollection
```

### Update
```json
aoss:UpdateCollection,
aoss:BatchGetCollection
```

