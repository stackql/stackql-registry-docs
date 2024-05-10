---
title: session
hide_title: false
hide_table_of_contents: false
keywords:
  - session
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


Gets or updates an individual <code>session</code> resource, use <code>sessions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>session</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Macie::Session resource specifies a new Amazon Macie session. A session is an object that represents the Amazon Macie service. A session is required for Amazon Macie to become operational.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.macie.session" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td>AWS account ID of customer</td></tr>
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
aws_account_id,
status,
finding_publishing_frequency,
service_role
FROM aws.macie.session
WHERE region = 'us-east-1' AND data__Identifier = '<AwsAccountId>';
```


## Permissions

To operate on the <code>session</code> resource, the following permissions are required:

### Read
```json
macie2:GetMacieSession
```

### Update
```json
macie2:GetMacieSession,
macie2:UpdateMacieSession
```

