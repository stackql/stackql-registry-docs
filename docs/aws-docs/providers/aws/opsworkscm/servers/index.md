---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - opsworkscm
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


Used to retrieve a list of <code>servers</code> in a region or to create or delete a <code>servers</code> resource, use <code>server</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::OpsWorksCM::Server</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opsworkscm.servers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="server_name" /></td><td><code>string</code></td><td></td></tr>
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
server_name
FROM aws.opsworkscm.servers
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
 "ServiceRoleArn": "{{ ServiceRoleArn }}",
 "InstanceProfileArn": "{{ InstanceProfileArn }}",
 "InstanceType": "{{ InstanceType }}"
}
>>>
--required properties only
INSERT INTO aws.opsworkscm.servers (
 ServiceRoleArn,
 InstanceProfileArn,
 InstanceType,
 region
)
SELECT 
{{ .ServiceRoleArn }},
 {{ .InstanceProfileArn }},
 {{ .InstanceType }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "KeyPair": "{{ KeyPair }}",
 "EngineVersion": "{{ EngineVersion }}",
 "ServiceRoleArn": "{{ ServiceRoleArn }}",
 "DisableAutomatedBackup": "{{ DisableAutomatedBackup }}",
 "BackupId": "{{ BackupId }}",
 "EngineModel": "{{ EngineModel }}",
 "PreferredMaintenanceWindow": "{{ PreferredMaintenanceWindow }}",
 "AssociatePublicIpAddress": "{{ AssociatePublicIpAddress }}",
 "InstanceProfileArn": "{{ InstanceProfileArn }}",
 "CustomCertificate": "{{ CustomCertificate }}",
 "PreferredBackupWindow": "{{ PreferredBackupWindow }}",
 "SecurityGroupIds": [
  "{{ SecurityGroupIds[0] }}"
 ],
 "SubnetIds": [
  "{{ SubnetIds[0] }}"
 ],
 "CustomDomain": "{{ CustomDomain }}",
 "CustomPrivateKey": "{{ CustomPrivateKey }}",
 "EngineAttributes": [
  {
   "Value": "{{ Value }}",
   "Name": "{{ Name }}"
  }
 ],
 "BackupRetentionCount": "{{ BackupRetentionCount }}",
 "InstanceType": "{{ InstanceType }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "Engine": "{{ Engine }}"
}
>>>
--all properties
INSERT INTO aws.opsworkscm.servers (
 KeyPair,
 EngineVersion,
 ServiceRoleArn,
 DisableAutomatedBackup,
 BackupId,
 EngineModel,
 PreferredMaintenanceWindow,
 AssociatePublicIpAddress,
 InstanceProfileArn,
 CustomCertificate,
 PreferredBackupWindow,
 SecurityGroupIds,
 SubnetIds,
 CustomDomain,
 CustomPrivateKey,
 EngineAttributes,
 BackupRetentionCount,
 InstanceType,
 Tags,
 Engine,
 region
)
SELECT 
 {{ .KeyPair }},
 {{ .EngineVersion }},
 {{ .ServiceRoleArn }},
 {{ .DisableAutomatedBackup }},
 {{ .BackupId }},
 {{ .EngineModel }},
 {{ .PreferredMaintenanceWindow }},
 {{ .AssociatePublicIpAddress }},
 {{ .InstanceProfileArn }},
 {{ .CustomCertificate }},
 {{ .PreferredBackupWindow }},
 {{ .SecurityGroupIds }},
 {{ .SubnetIds }},
 {{ .CustomDomain }},
 {{ .CustomPrivateKey }},
 {{ .EngineAttributes }},
 {{ .BackupRetentionCount }},
 {{ .InstanceType }},
 {{ .Tags }},
 {{ .Engine }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.opsworkscm.servers
WHERE data__Identifier = '<ServerName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>servers</code> resource, the following permissions are required:

### Create
```json
opsworks-cm:CreateServer,
opsworks-cm:DescribeServers,
iam:PassRole
```

### Delete
```json
opsworks-cm:DeleteServer,
opsworks-cm:DescribeServers
```

### List
```json
opsworks-cm:DescribeServers,
opsworks-cm:ListTagsForResource
```

