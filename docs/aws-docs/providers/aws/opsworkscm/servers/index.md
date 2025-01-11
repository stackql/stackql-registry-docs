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

Creates, updates, deletes or gets a <code>server</code> resource or lists <code>servers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::OpsWorksCM::Server</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opsworkscm.servers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="key_pair" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="disable_automated_backup" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="engine_model" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="preferred_maintenance_window" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="associate_public_ip_address" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_profile_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_certificate" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="preferred_backup_window" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_domain" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_private_key" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="server_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="engine_attributes" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_retention_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html"><code>AWS::OpsWorksCM::Server</code></a>.

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
    <td><CopyableCode code="ServiceRoleArn, InstanceProfileArn, InstanceType, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>servers</code> in a region.
```sql
SELECT
region,
key_pair,
engine_version,
service_role_arn,
disable_automated_backup,
backup_id,
engine_model,
preferred_maintenance_window,
associate_public_ip_address,
instance_profile_arn,
custom_certificate,
preferred_backup_window,
security_group_ids,
subnet_ids,
custom_domain,
endpoint,
custom_private_key,
server_name,
engine_attributes,
backup_retention_count,
arn,
instance_type,
tags,
engine
FROM aws.opsworkscm.servers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>server</code>.
```sql
SELECT
region,
key_pair,
engine_version,
service_role_arn,
disable_automated_backup,
backup_id,
engine_model,
preferred_maintenance_window,
associate_public_ip_address,
instance_profile_arn,
custom_certificate,
preferred_backup_window,
security_group_ids,
subnet_ids,
custom_domain,
endpoint,
custom_private_key,
server_name,
engine_attributes,
backup_retention_count,
arn,
instance_type,
tags,
engine
FROM aws.opsworkscm.servers
WHERE region = 'us-east-1' AND data__Identifier = '<ServerName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Update
```json
opsworks-cm:UpdateServer,
opsworks-cm:TagResource,
opsworks-cm:UntagResource,
opsworks-cm:DescribeServers
```

### List
```json
opsworks-cm:DescribeServers,
opsworks-cm:ListTagsForResource
```

### Read
```json
opsworks-cm:DescribeServers
```
