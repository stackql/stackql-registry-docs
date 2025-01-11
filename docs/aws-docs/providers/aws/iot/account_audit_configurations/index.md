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

Creates, updates, deletes or gets an <code>account_audit_configuration</code> resource or lists <code>account_audit_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_audit_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Configures the Device Defender audit settings for this account. Settings include how audit notifications are sent and which audit checks are enabled or disabled.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.account_audit_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).</td></tr>
<tr><td><CopyableCode code="audit_check_configurations" /></td><td><code>object</code></td><td>Specifies which audit checks are enabled and disabled for this account.</td></tr>
<tr><td><CopyableCode code="audit_notification_target_configurations" /></td><td><code>object</code></td><td>Information about the targets to which audit notifications are sent.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates and other items as required when performing an audit.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-accountauditconfiguration.html"><code>AWS::IoT::AccountAuditConfiguration</code></a>.

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
    <td><CopyableCode code="AccountId, AuditCheckConfigurations, RoleArn, region" /></td>
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
Gets all <code>account_audit_configurations</code> in a region.
```sql
SELECT
region,
account_id,
audit_check_configurations,
audit_notification_target_configurations,
role_arn
FROM aws.iot.account_audit_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>account_audit_configuration</code>.
```sql
SELECT
region,
account_id,
audit_check_configurations,
audit_notification_target_configurations,
role_arn
FROM aws.iot.account_audit_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<AccountId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>account_audit_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.account_audit_configurations (
 AccountId,
 AuditCheckConfigurations,
 RoleArn,
 region
)
SELECT 
'{{ AccountId }}',
 '{{ AuditCheckConfigurations }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.account_audit_configurations (
 AccountId,
 AuditCheckConfigurations,
 AuditNotificationTargetConfigurations,
 RoleArn,
 region
)
SELECT 
 '{{ AccountId }}',
 '{{ AuditCheckConfigurations }}',
 '{{ AuditNotificationTargetConfigurations }}',
 '{{ RoleArn }}',
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
  - name: account_audit_configuration
    props:
      - name: AccountId
        value: '{{ AccountId }}'
      - name: AuditCheckConfigurations
        value:
          AuthenticatedCognitoRoleOverlyPermissiveCheck:
            Enabled: '{{ Enabled }}'
          CaCertificateExpiringCheck: null
          CaCertificateKeyQualityCheck: null
          ConflictingClientIdsCheck: null
          DeviceCertificateExpiringCheck: null
          DeviceCertificateKeyQualityCheck: null
          DeviceCertificateSharedCheck: null
          IotPolicyOverlyPermissiveCheck: null
          IotRoleAliasAllowsAccessToUnusedServicesCheck: null
          IotRoleAliasOverlyPermissiveCheck: null
          LoggingDisabledCheck: null
          RevokedCaCertificateStillActiveCheck: null
          RevokedDeviceCertificateStillActiveCheck: null
          UnauthenticatedCognitoRoleOverlyPermissiveCheck: null
          IntermediateCaRevokedForActiveDeviceCertificatesCheck: null
          IoTPolicyPotentialMisConfigurationCheck: null
      - name: AuditNotificationTargetConfigurations
        value:
          Sns:
            TargetArn: '{{ TargetArn }}'
            RoleArn: '{{ RoleArn }}'
            Enabled: '{{ Enabled }}'
      - name: RoleArn
        value: '{{ RoleArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
iot:DescribeAccountAuditConfiguration
```

### Update
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
