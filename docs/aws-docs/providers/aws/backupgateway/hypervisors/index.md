---
title: hypervisors
hide_title: false
hide_table_of_contents: false
keywords:
  - hypervisors
  - backupgateway
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


Used to retrieve a list of <code>hypervisors</code> in a region or to create or delete a <code>hypervisors</code> resource, use <code>hypervisor</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hypervisors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::BackupGateway::Hypervisor Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backupgateway.hypervisors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="hypervisor_arn" /></td><td><code>string</code></td><td></td></tr>
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
hypervisor_arn
FROM aws.backupgateway.hypervisors
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
 "Host": "{{ Host }}",
 "KmsKeyArn": "{{ KmsKeyArn }}",
 "LogGroupArn": "{{ LogGroupArn }}",
 "Name": "{{ Name }}",
 "Password": "{{ Password }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "Username": "{{ Username }}"
}
>>>
--required properties only
INSERT INTO aws.backupgateway.hypervisors (
 Host,
 KmsKeyArn,
 LogGroupArn,
 Name,
 Password,
 Tags,
 Username,
 region
)
SELECT 
{{ Host }},
 {{ KmsKeyArn }},
 {{ LogGroupArn }},
 {{ Name }},
 {{ Password }},
 {{ Tags }},
 {{ Username }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Host": "{{ Host }}",
 "KmsKeyArn": "{{ KmsKeyArn }}",
 "LogGroupArn": "{{ LogGroupArn }}",
 "Name": "{{ Name }}",
 "Password": "{{ Password }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "Username": "{{ Username }}"
}
>>>
--all properties
INSERT INTO aws.backupgateway.hypervisors (
 Host,
 KmsKeyArn,
 LogGroupArn,
 Name,
 Password,
 Tags,
 Username,
 region
)
SELECT 
 {{ Host }},
 {{ KmsKeyArn }},
 {{ LogGroupArn }},
 {{ Name }},
 {{ Password }},
 {{ Tags }},
 {{ Username }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.backupgateway.hypervisors
WHERE data__Identifier = '<HypervisorArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>hypervisors</code> resource, the following permissions are required:

### Create
```json
backup-gateway:ImportHypervisorConfiguration,
backup-gateway:GetHypervisor,
backup-gateway:ListHypervisors,
backup-gateway:TagResource,
kms:CreateGrant,
kms:Encrypt,
kms:Decrypt
```

### Delete
```json
backup-gateway:DeleteHypervisor,
backup-gateway:GetHypervisor,
backup-gateway:ListHypervisors
```

### List
```json
backup-gateway:ListHypervisors
```

