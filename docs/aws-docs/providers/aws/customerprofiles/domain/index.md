---
title: domain
hide_title: false
hide_table_of_contents: false
keywords:
  - domain
  - customerprofiles
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


Gets or updates an individual <code>domain</code> resource, use <code>domains</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A domain defined for 3rd party data source in Profile Service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.domain" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="dead_letter_queue_url" /></td><td><code>string</code></td><td>The URL of the SQS dead letter queue</td></tr>
<tr><td><CopyableCode code="default_encryption_key" /></td><td><code>string</code></td><td>The default encryption key</td></tr>
<tr><td><CopyableCode code="default_expiration_days" /></td><td><code>integer</code></td><td>The default number of days until the data within the domain expires.</td></tr>
<tr><td><CopyableCode code="matching" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_based_matching" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="stats" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags (keys and values) associated with the domain</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this integration got created</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The time of this integration got last updated at</td></tr>
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
domain_name,
dead_letter_queue_url,
default_encryption_key,
default_expiration_days,
matching,
rule_based_matching,
stats,
tags,
created_at,
last_updated_at
FROM aws.customerprofiles.domain
WHERE region = 'us-east-1' AND data__Identifier = '<DomainName>';
```


## Permissions

To operate on the <code>domain</code> resource, the following permissions are required:

### Read
```json
profile:GetDomain
```

### Update
```json
profile:GetDomain,
profile:UpdateDomain,
profile:UntagResource,
profile:TagResource
```

