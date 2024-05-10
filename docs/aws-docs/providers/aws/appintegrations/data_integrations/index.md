---
title: data_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - data_integrations
  - appintegrations
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


Used to retrieve a list of <code>data_integrations</code> in a region or to create or delete a <code>data_integrations</code> resource, use <code>data_integration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppIntegrations::DataIntegration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appintegrations.data_integrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifer of the data integration.</td></tr>
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
id
FROM aws.appintegrations.data_integrations
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
 "Name": "{{ Name }}",
 "KmsKey": "{{ KmsKey }}",
 "SourceURI": "{{ SourceURI }}"
}
>>>
--required properties only
INSERT INTO aws.appintegrations.data_integrations (
 Name,
 KmsKey,
 SourceURI,
 region
)
SELECT 
{{ .Name }},
 {{ .KmsKey }},
 {{ .SourceURI }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "Name": "{{ Name }}",
 "KmsKey": "{{ KmsKey }}",
 "ScheduleConfig": {
  "FirstExecutionFrom": "{{ FirstExecutionFrom }}",
  "Object": "{{ Object }}",
  "ScheduleExpression": "{{ ScheduleExpression }}"
 },
 "SourceURI": "{{ SourceURI }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "FileConfiguration": {
  "Folders": [
   "{{ Folders[0] }}"
  ],
  "Filters": {}
 },
 "ObjectConfiguration": {}
}
>>>
--all properties
INSERT INTO aws.appintegrations.data_integrations (
 Description,
 Name,
 KmsKey,
 ScheduleConfig,
 SourceURI,
 Tags,
 FileConfiguration,
 ObjectConfiguration,
 region
)
SELECT 
 {{ .Description }},
 {{ .Name }},
 {{ .KmsKey }},
 {{ .ScheduleConfig }},
 {{ .SourceURI }},
 {{ .Tags }},
 {{ .FileConfiguration }},
 {{ .ObjectConfiguration }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.appintegrations.data_integrations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_integrations</code> resource, the following permissions are required:

### Create
```json
app-integrations:CreateDataIntegration,
app-integrations:TagResource,
appflow:DescribeConnectorProfiles,
appflow:CreateFlow,
appflow:DeleteFlow,
appflow:DescribeConnectorEntity,
appflow:UseConnectorProfile,
appflow:TagResource,
appflow:UntagResource,
kms:CreateGrant,
kms:DescribeKey,
kms:ListAliases,
kms:ListGrants,
kms:ListKeys,
s3:GetBucketNotification,
s3:PutBucketNotification,
s3:GetEncryptionConfiguration
```

### List
```json
app-integrations:ListDataIntegrations
```

### Delete
```json
app-integrations:DeleteDataIntegration,
app-integrations:UntagResource,
appflow:CreateFlow,
appflow:DeleteFlow,
appflow:DescribeConnectorEntity,
appflow:UseConnectorProfile,
appflow:TagResource,
appflow:UntagResource,
kms:CreateGrant,
kms:DescribeKey,
kms:ListAliases,
kms:ListGrants,
kms:ListKeys
```

