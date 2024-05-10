---
title: account_audit_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - account_audit_configurations
  - iot
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


Used to retrieve a list of <code>account_audit_configurations</code> in a region or to create or delete a <code>account_audit_configurations</code> resource, use <code>account_audit_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_audit_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Configures the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.account_audit_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).</td></tr>
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
account_id
FROM aws.iot.account_audit_configurations
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
 "AccountId": "{{ AccountId }}",
 "AuditCheckConfigurations": {
  "AuthenticatedCognitoRoleOverlyPermissiveCheck": {
   "Enabled": "{{ Enabled }}"
  },
  "CaCertificateExpiringCheck": null,
  "CaCertificateKeyQualityCheck": null,
  "ConflictingClientIdsCheck": null,
  "DeviceCertificateExpiringCheck": null,
  "DeviceCertificateKeyQualityCheck": null,
  "DeviceCertificateSharedCheck": null,
  "IotPolicyOverlyPermissiveCheck": null,
  "IotRoleAliasAllowsAccessToUnusedServicesCheck": null,
  "IotRoleAliasOverlyPermissiveCheck": null,
  "LoggingDisabledCheck": null,
  "RevokedCaCertificateStillActiveCheck": null,
  "RevokedDeviceCertificateStillActiveCheck": null,
  "UnauthenticatedCognitoRoleOverlyPermissiveCheck": null,
  "IntermediateCaRevokedForActiveDeviceCertificatesCheck": null,
  "IoTPolicyPotentialMisConfigurationCheck": null
 },
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.iot.account_audit_configurations (
 AccountId,
 AuditCheckConfigurations,
 RoleArn,
 region
)
SELECT 
{{ AccountId }},
 {{ AuditCheckConfigurations }},
 {{ RoleArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AccountId": "{{ AccountId }}",
 "AuditCheckConfigurations": {
  "AuthenticatedCognitoRoleOverlyPermissiveCheck": {
   "Enabled": "{{ Enabled }}"
  },
  "CaCertificateExpiringCheck": null,
  "CaCertificateKeyQualityCheck": null,
  "ConflictingClientIdsCheck": null,
  "DeviceCertificateExpiringCheck": null,
  "DeviceCertificateKeyQualityCheck": null,
  "DeviceCertificateSharedCheck": null,
  "IotPolicyOverlyPermissiveCheck": null,
  "IotRoleAliasAllowsAccessToUnusedServicesCheck": null,
  "IotRoleAliasOverlyPermissiveCheck": null,
  "LoggingDisabledCheck": null,
  "RevokedCaCertificateStillActiveCheck": null,
  "RevokedDeviceCertificateStillActiveCheck": null,
  "UnauthenticatedCognitoRoleOverlyPermissiveCheck": null,
  "IntermediateCaRevokedForActiveDeviceCertificatesCheck": null,
  "IoTPolicyPotentialMisConfigurationCheck": null
 },
 "AuditNotificationTargetConfigurations": {
  "Sns": {
   "TargetArn": "{{ TargetArn }}",
   "RoleArn": "{{ RoleArn }}",
   "Enabled": "{{ Enabled }}"
  }
 },
 "RoleArn": "{{ RoleArn }}"
}
>>>
--all properties
INSERT INTO aws.iot.account_audit_configurations (
 AccountId,
 AuditCheckConfigurations,
 AuditNotificationTargetConfigurations,
 RoleArn,
 region
)
SELECT 
 {{ AccountId }},
 {{ AuditCheckConfigurations }},
 {{ AuditNotificationTargetConfigurations }},
 {{ RoleArn }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iot.account_audit_configurations
WHERE data__Identifier = '<AccountId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>account_audit_configurations</code> resource, the following permissions are required:

### Create
```json
iot:UpdateAccountAuditConfiguration,
iot:DescribeAccountAuditConfiguration,
iam:PassRole
```

### Delete
```json
iot:DescribeAccountAuditConfiguration,
iot:DeleteAccountAuditConfiguration
```

### List
```json
iot:DescribeAccountAuditConfiguration
```

