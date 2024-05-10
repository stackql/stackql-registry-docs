---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - systemsmanagersap
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


Used to retrieve a list of <code>applications</code> in a region or to create or delete a <code>applications</code> resource, use <code>application</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SystemsManagerSAP::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.systemsmanagersap.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the Helix application</td></tr>
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
arn
FROM aws.systemsmanagersap.applications
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
 "ApplicationId": "{{ ApplicationId }}",
 "ApplicationType": "{{ ApplicationType }}"
}
>>>
--required properties only
INSERT INTO aws.systemsmanagersap.applications (
 ApplicationId,
 ApplicationType,
 region
)
SELECT 
{{ .ApplicationId }},
 {{ .ApplicationType }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ApplicationId": "{{ ApplicationId }}",
 "ApplicationType": "{{ ApplicationType }}",
 "Credentials": [
  {
   "DatabaseName": "{{ DatabaseName }}",
   "CredentialType": "{{ CredentialType }}",
   "SecretId": "{{ SecretId }}"
  }
 ],
 "Instances": [
  "{{ Instances[0] }}"
 ],
 "SapInstanceNumber": "{{ SapInstanceNumber }}",
 "Sid": "{{ Sid }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.systemsmanagersap.applications (
 ApplicationId,
 ApplicationType,
 Credentials,
 Instances,
 SapInstanceNumber,
 Sid,
 Tags,
 region
)
SELECT 
 {{ .ApplicationId }},
 {{ .ApplicationType }},
 {{ .Credentials }},
 {{ .Instances }},
 {{ .SapInstanceNumber }},
 {{ .Sid }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.systemsmanagersap.applications
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
ssm-sap:RegisterApplication,
ssm-sap:GetApplication,
ssm-sap:TagResource,
ssm-sap:ListTagsForResource
```

### Delete
```json
ssm-sap:DeregisterApplication,
ssm-sap:GetApplication
```

### List
```json
ssm-sap:ListApplications
```

