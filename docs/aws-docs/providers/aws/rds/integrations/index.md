---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
  - rds
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


Used to retrieve a list of <code>integrations</code> in a region or to create or delete a <code>integrations</code> resource, use <code>integration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a zero-ETL integration with Amazon Redshift.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.integrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="integration_arn" /></td><td><code>string</code></td><td>The ARN of the integration.</td></tr>
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
integration_arn
FROM aws.rds.integrations
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
 "SourceArn": "{{ SourceArn }}",
 "TargetArn": "{{ TargetArn }}"
}
>>>
--required properties only
INSERT INTO aws.rds.integrations (
 SourceArn,
 TargetArn,
 region
)
SELECT 
{{ .SourceArn }},
 {{ .TargetArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "IntegrationName": "{{ IntegrationName }}",
 "Description": "{{ Description }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "DataFilter": "{{ DataFilter }}",
 "SourceArn": "{{ SourceArn }}",
 "TargetArn": "{{ TargetArn }}",
 "KMSKeyId": "{{ KMSKeyId }}",
 "AdditionalEncryptionContext": {}
}
>>>
--all properties
INSERT INTO aws.rds.integrations (
 IntegrationName,
 Description,
 Tags,
 DataFilter,
 SourceArn,
 TargetArn,
 KMSKeyId,
 AdditionalEncryptionContext,
 region
)
SELECT 
 {{ .IntegrationName }},
 {{ .Description }},
 {{ .Tags }},
 {{ .DataFilter }},
 {{ .SourceArn }},
 {{ .TargetArn }},
 {{ .KMSKeyId }},
 {{ .AdditionalEncryptionContext }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.rds.integrations
WHERE data__Identifier = '<IntegrationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>integrations</code> resource, the following permissions are required:

### Create
```json
rds:CreateIntegration,
rds:DescribeIntegrations,
rds:AddTagsToResource,
kms:CreateGrant,
kms:DescribeKey,
redshift:CreateInboundIntegration
```

### Delete
```json
rds:DeleteIntegration,
rds:DescribeIntegrations
```

### List
```json
rds:DescribeIntegrations
```

