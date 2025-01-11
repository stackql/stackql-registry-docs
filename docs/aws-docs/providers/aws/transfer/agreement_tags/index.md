---
title: agreement_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - agreement_tags
  - transfer
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

Expands all tag keys and values for <code>agreements</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agreement_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Transfer::Agreement</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.agreement_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A textual description for the agreement.</td></tr>
<tr><td><CopyableCode code="server_id" /></td><td><code>string</code></td><td>A unique identifier for the server.</td></tr>
<tr><td><CopyableCode code="local_profile_id" /></td><td><code>string</code></td><td>A unique identifier for the local profile.</td></tr>
<tr><td><CopyableCode code="partner_profile_id" /></td><td><code>string</code></td><td>A unique identifier for the partner profile.</td></tr>
<tr><td><CopyableCode code="base_directory" /></td><td><code>string</code></td><td>Specifies the base directory for the agreement.</td></tr>
<tr><td><CopyableCode code="access_role" /></td><td><code>string</code></td><td>Specifies the access role for the agreement.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Specifies the status of the agreement.</td></tr>
<tr><td><CopyableCode code="agreement_id" /></td><td><code>string</code></td><td>A unique identifier for the agreement.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the agreement.</td></tr>
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
Expands tags for all <code>agreements</code> in a region.
```sql
SELECT
region,
description,
server_id,
local_profile_id,
partner_profile_id,
base_directory,
access_role,
status,
agreement_id,
arn,
tag_key,
tag_value
FROM aws.transfer.agreement_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>agreement_tags</code> resource, see <a href="/providers/aws/transfer/agreements/#permissions"><code>agreements</code></a>

