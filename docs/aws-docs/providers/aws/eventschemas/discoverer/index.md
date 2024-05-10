---
title: discoverer
hide_title: false
hide_table_of_contents: false
keywords:
  - discoverer
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


Gets or updates an individual <code>discoverer</code> resource, use <code>discoverers</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>discoverer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::Discoverer</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eventschemas.discoverer" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="discoverer_arn" /></td><td><code>string</code></td><td>The ARN of the discoverer.</td></tr>
<tr><td><CopyableCode code="discoverer_id" /></td><td><code>string</code></td><td>The Id of the discoverer.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the discoverer.</td></tr>
<tr><td><CopyableCode code="source_arn" /></td><td><code>string</code></td><td>The ARN of the event bus.</td></tr>
<tr><td><CopyableCode code="cross_account" /></td><td><code>boolean</code></td><td>Defines whether event schemas from other accounts are discovered. Default is True.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>Defines the current state of the discoverer.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags associated with the resource.</td></tr>
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
discoverer_arn,
discoverer_id,
description,
source_arn,
cross_account,
state,
tags
FROM aws.eventschemas.discoverer
WHERE region = 'us-east-1' AND data__Identifier = '<DiscovererArn>';
```


## Permissions

To operate on the <code>discoverer</code> resource, the following permissions are required:

### Read
```json
schemas:DescribeDiscoverer
```

### Update
```json
schemas:DescribeDiscoverer,
schemas:UpdateDiscoverer,
schemas:TagResource,
schemas:UntagResource,
schemas:ListTagsForResource,
events:PutTargets,
events:PutRule
```

