---
title: sessions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions_list_only
  - macie
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

Lists <code>sessions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/sessions/"><code>sessions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sessions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Macie::Session resource specifies a new Amazon Macie session. A session is an object that represents the Amazon Macie service. A session is required for Amazon Macie to become operational.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.macie.sessions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td>AWS account ID of customer</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>A enumeration value that specifies the status of the Macie Session.</td></tr>
<tr><td><CopyableCode code="finding_publishing_frequency" /></td><td><code>string</code></td><td>A enumeration value that specifies how frequently finding updates are published.</td></tr>
<tr><td><CopyableCode code="service_role" /></td><td><code>string</code></td><td>Service role used by Macie</td></tr>
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
Lists all <code>sessions</code> in a region.
```sql
SELECT
region,
aws_account_id
FROM aws.macie.sessions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>sessions_list_only</code> resource, see <a href="/providers/aws/macie/sessions/#permissions"><code>sessions</code></a>


