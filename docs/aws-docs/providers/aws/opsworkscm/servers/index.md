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

Use the following StackQL query and manifest file to create a new <code>server</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- server.iql (required properties only)
INSERT INTO aws.opsworkscm.servers (
 ServiceRoleArn,
 InstanceProfileArn,
 InstanceType,
 region
)
SELECT 
'{{ ServiceRoleArn }}',
 '{{ InstanceProfileArn }}',
 '{{ InstanceType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- server.iql (all properties)
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
 '{{ KeyPair }}',
 '{{ EngineVersion }}',
 '{{ ServiceRoleArn }}',
 '{{ DisableAutomatedBackup }}',
 '{{ BackupId }}',
 '{{ EngineModel }}',
 '{{ PreferredMaintenanceWindow }}',
 '{{ AssociatePublicIpAddress }}',
 '{{ InstanceProfileArn }}',
 '{{ CustomCertificate }}',
 '{{ PreferredBackupWindow }}',
 '{{ SecurityGroupIds }}',
 '{{ SubnetIds }}',
 '{{ CustomDomain }}',
 '{{ CustomPrivateKey }}',
 '{{ EngineAttributes }}',
 '{{ BackupRetentionCount }}',
 '{{ InstanceType }}',
 '{{ Tags }}',
 '{{ Engine }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: server
    props:
      - name: KeyPair
        value: '{{ KeyPair }}'
      - name: EngineVersion
        value: '{{ EngineVersion }}'
      - name: ServiceRoleArn
        value: '{{ ServiceRoleArn }}'
      - name: DisableAutomatedBackup
        value: '{{ DisableAutomatedBackup }}'
      - name: BackupId
        value: '{{ BackupId }}'
      - name: EngineModel
        value: '{{ EngineModel }}'
      - name: PreferredMaintenanceWindow
        value: '{{ PreferredMaintenanceWindow }}'
      - name: AssociatePublicIpAddress
        value: '{{ AssociatePublicIpAddress }}'
      - name: InstanceProfileArn
        value: '{{ InstanceProfileArn }}'
      - name: CustomCertificate
        value: '{{ CustomCertificate }}'
      - name: PreferredBackupWindow
        value: '{{ PreferredBackupWindow }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: CustomDomain
        value: '{{ CustomDomain }}'
      - name: CustomPrivateKey
        value: '{{ CustomPrivateKey }}'
      - name: EngineAttributes
        value:
          - Value: '{{ Value }}'
            Name: '{{ Name }}'
      - name: BackupRetentionCount
        value: '{{ BackupRetentionCount }}'
      - name: InstanceType
        value: '{{ InstanceType }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: Engine
        value: '{{ Engine }}'

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

