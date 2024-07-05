---
title: collections_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - collections_list_only
  - rekognition
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
<tr><td><b>Description</b></td><td>The AWS::Rekognition::Collection type creates an Amazon Rekognition Collection. A collection is a logical grouping of information about detected faces which can later be referenced for searches on the group</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rekognition.collections_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the stream processor</td></tr>
<tr><td><CopyableCode code="collection_id" /></td><td><code>string</code></td><td>The name of the collection</td></tr>
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
Lists all <code>collections</code> in a region.
```sql
SELECT
region,
collection_id
FROM aws.rekognition.collections_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>collections_list_only</code> resource, see <a href="/providers/aws/rekognition/collections/#permissions"><code>collections</code></a>


