---
title: discoverer_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - discoverer_tags
  - eventschemas
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

Expands all tag keys and values for <code>discoverers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>discoverer_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::Discoverer</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eventschemas.discoverer_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="discoverer_arn" /></td><td><code>string</code></td><td>The ARN of the discoverer.</td></tr>
<tr><td><CopyableCode code="discoverer_id" /></td><td><code>string</code></td><td>The Id of the discoverer.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the discoverer.</td></tr>
<tr><td><CopyableCode code="source_arn" /></td><td><code>string</code></td><td>The ARN of the event bus.</td></tr>
<tr><td><CopyableCode code="cross_account" /></td><td><code>boolean</code></td><td>Defines whether event schemas from other accounts are discovered. Default is True.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>Defines the current state of the discoverer.</td></tr>
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
Expands tags for all <code>discoverers</code> in a region.
```sql
SELECT
region,
discoverer_arn,
discoverer_id,
description,
source_arn,
cross_account,
state,
tag_key,
tag_value
FROM aws.eventschemas.discoverer_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>discoverer_tags</code> resource, see <a href="/providers/aws/eventschemas/discoverers/#permissions"><code>discoverers</code></a>


