---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - iam
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


List of policies (requires `aws` provider to be installed)

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>List of policies (requires `aws` provider to be installed)</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam.policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td>The name for the policy</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN</td></tr>
<tr><td><CopyableCode code="attachment_count" /></td><td><code>number</code></td><td>The attachment count for the policy</td></tr>
<tr><td><CopyableCode code="create_date" /></td><td><code>string</code></td><td>The creation date for the policy</td></tr>
<tr><td><CopyableCode code="default_version_id" /></td><td><code>string</code></td><td>The default version id for the policy</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description for the policy</td></tr>
<tr><td><CopyableCode code="is_attachable" /></td><td><code>boolean</code></td><td>Is the policy attachable?</td></tr>
<tr><td><CopyableCode code="path" /></td><td><code>string</code></td><td>The path for the policy</td></tr>
<tr><td><CopyableCode code="permissions_boundary_usage_count" /></td><td><code>number</code></td><td>The permissions boundary usage count for the policy</td></tr>
<tr><td><CopyableCode code="policy_id" /></td><td><code>string</code></td><td>The id for the policy</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags for the policy</td></tr>
<tr><td><CopyableCode code="update_date" /></td><td><code>string</code></td><td>The update date for the policy</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="view" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
policy_name,
arn,
attachment_count,
create_date,
default_version_id,
description,
is_attachable,
path,
permissions_boundary_usage_count,
policy_id,
tags,
update_date,
region
FROM aws.iam.policies

```





