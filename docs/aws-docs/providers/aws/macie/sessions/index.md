---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
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


Used to retrieve a list of <code>sessions</code> in a region or to create or delete a <code>sessions</code> resource, use <code>session</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Macie::Session resource specifies a new Amazon Macie session. A session is an object that represents the Amazon Macie service. A session is required for Amazon Macie to become operational.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.macie.sessions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td>AWS account ID of customer</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
aws_account_id
FROM aws.macie.sessions
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Status": "{{ Status }}",
 "FindingPublishingFrequency": "{{ FindingPublishingFrequency }}"
}
>>>
--required properties only
INSERT INTO aws.macie.sessions (
 Status,
 FindingPublishingFrequency,
 region
)
SELECT 
{{ Status }},
 {{ FindingPublishingFrequency }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Status": "{{ Status }}",
 "FindingPublishingFrequency": "{{ FindingPublishingFrequency }}"
}
>>>
--all properties
INSERT INTO aws.macie.sessions (
 Status,
 FindingPublishingFrequency,
 region
)
SELECT 
 {{ Status }},
 {{ FindingPublishingFrequency }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.macie.sessions
WHERE data__Identifier = '<AwsAccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>sessions</code> resource, the following permissions are required:

### Create
```json
macie2:GetMacieSession,
macie2:EnableMacie
```

### List
```json
macie2:GetMacieSession
```

### Delete
```json
macie2:DisableMacie
```

