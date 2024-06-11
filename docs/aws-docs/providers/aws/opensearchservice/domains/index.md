---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - opensearchservice
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

Creates, updates, deletes or gets a <code>domain</code> resource or lists <code>domains</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchservice.domains" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_config" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="access_policies" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="ip_address_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="advanced_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="log_publishing_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="snapshot_options" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_options" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="node_to_node_encryption_options" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_endpoint_options" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="cognito_options" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="advanced_security_options" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_endpoint_v2" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_endpoints" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="ebs_options" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="encryption_at_rest_options" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this Domain.</td></tr>
<tr><td><CopyableCode code="service_software_options" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="off_peak_window_options" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="software_update_options" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from a <code>domain</code>.
```sql
SELECT
region,
cluster_config,
domain_name,
access_policies,
ip_address_type,
engine_version,
advanced_options,
log_publishing_options,
snapshot_options,
vpc_options,
node_to_node_encryption_options,
domain_endpoint_options,
cognito_options,
advanced_security_options,
domain_endpoint,
domain_endpoint_v2,
domain_endpoints,
ebs_options,
id,
arn,
domain_arn,
encryption_at_rest_options,
tags,
service_software_options,
off_peak_window_options,
software_update_options
FROM aws.opensearchservice.domains
WHERE region = 'us-east-1' AND data__Identifier = '<DomainName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domain</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.opensearchservice.domains (
 ClusterConfig,
 DomainName,
 AccessPolicies,
 IPAddressType,
 EngineVersion,
 AdvancedOptions,
 LogPublishingOptions,
 SnapshotOptions,
 VPCOptions,
 NodeToNodeEncryptionOptions,
 DomainEndpointOptions,
 CognitoOptions,
 AdvancedSecurityOptions,
 EBSOptions,
 EncryptionAtRestOptions,
 Tags,
 OffPeakWindowOptions,
 SoftwareUpdateOptions,
 region
)
SELECT 
'{{ ClusterConfig }}',
 '{{ DomainName }}',
 '{{ AccessPolicies }}',
 '{{ IPAddressType }}',
 '{{ EngineVersion }}',
 '{{ AdvancedOptions }}',
 '{{ LogPublishingOptions }}',
 '{{ SnapshotOptions }}',
 '{{ VPCOptions }}',
 '{{ NodeToNodeEncryptionOptions }}',
 '{{ DomainEndpointOptions }}',
 '{{ CognitoOptions }}',
 '{{ AdvancedSecurityOptions }}',
 '{{ EBSOptions }}',
 '{{ EncryptionAtRestOptions }}',
 '{{ Tags }}',
 '{{ OffPeakWindowOptions }}',
 '{{ SoftwareUpdateOptions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.opensearchservice.domains (
 ClusterConfig,
 DomainName,
 AccessPolicies,
 IPAddressType,
 EngineVersion,
 AdvancedOptions,
 LogPublishingOptions,
 SnapshotOptions,
 VPCOptions,
 NodeToNodeEncryptionOptions,
 DomainEndpointOptions,
 CognitoOptions,
 AdvancedSecurityOptions,
 EBSOptions,
 EncryptionAtRestOptions,
 Tags,
 OffPeakWindowOptions,
 SoftwareUpdateOptions,
 region
)
SELECT 
 '{{ ClusterConfig }}',
 '{{ DomainName }}',
 '{{ AccessPolicies }}',
 '{{ IPAddressType }}',
 '{{ EngineVersion }}',
 '{{ AdvancedOptions }}',
 '{{ LogPublishingOptions }}',
 '{{ SnapshotOptions }}',
 '{{ VPCOptions }}',
 '{{ NodeToNodeEncryptionOptions }}',
 '{{ DomainEndpointOptions }}',
 '{{ CognitoOptions }}',
 '{{ AdvancedSecurityOptions }}',
 '{{ EBSOptions }}',
 '{{ EncryptionAtRestOptions }}',
 '{{ Tags }}',
 '{{ OffPeakWindowOptions }}',
 '{{ SoftwareUpdateOptions }}',
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
  - name: domain
    props:
      - name: ClusterConfig
        value:
          InstanceCount: '{{ InstanceCount }}'
          WarmEnabled: '{{ WarmEnabled }}'
          WarmCount: '{{ WarmCount }}'
          DedicatedMasterEnabled: '{{ DedicatedMasterEnabled }}'
          ZoneAwarenessConfig:
            AvailabilityZoneCount: '{{ AvailabilityZoneCount }}'
          DedicatedMasterCount: '{{ DedicatedMasterCount }}'
          InstanceType: '{{ InstanceType }}'
          WarmType: '{{ WarmType }}'
          ZoneAwarenessEnabled: '{{ ZoneAwarenessEnabled }}'
          DedicatedMasterType: '{{ DedicatedMasterType }}'
          MultiAZWithStandbyEnabled: '{{ MultiAZWithStandbyEnabled }}'
          ColdStorageOptions:
            Enabled: '{{ Enabled }}'
      - name: DomainName
        value: '{{ DomainName }}'
      - name: AccessPolicies
        value: {}
      - name: IPAddressType
        value: '{{ IPAddressType }}'
      - name: EngineVersion
        value: '{{ EngineVersion }}'
      - name: AdvancedOptions
        value: {}
      - name: LogPublishingOptions
        value: {}
      - name: SnapshotOptions
        value:
          AutomatedSnapshotStartHour: '{{ AutomatedSnapshotStartHour }}'
      - name: VPCOptions
        value:
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
          SubnetIds:
            - '{{ SubnetIds[0] }}'
      - name: NodeToNodeEncryptionOptions
        value:
          Enabled: '{{ Enabled }}'
      - name: DomainEndpointOptions
        value:
          CustomEndpointCertificateArn: '{{ CustomEndpointCertificateArn }}'
          CustomEndpointEnabled: '{{ CustomEndpointEnabled }}'
          EnforceHTTPS: '{{ EnforceHTTPS }}'
          CustomEndpoint: '{{ CustomEndpoint }}'
          TLSSecurityPolicy: '{{ TLSSecurityPolicy }}'
      - name: CognitoOptions
        value:
          Enabled: '{{ Enabled }}'
          IdentityPoolId: '{{ IdentityPoolId }}'
          UserPoolId: '{{ UserPoolId }}'
          RoleArn: '{{ RoleArn }}'
      - name: AdvancedSecurityOptions
        value:
          Enabled: '{{ Enabled }}'
          MasterUserOptions:
            MasterUserPassword: '{{ MasterUserPassword }}'
            MasterUserName: '{{ MasterUserName }}'
            MasterUserARN: '{{ MasterUserARN }}'
          InternalUserDatabaseEnabled: '{{ InternalUserDatabaseEnabled }}'
          AnonymousAuthEnabled: '{{ AnonymousAuthEnabled }}'
          SAMLOptions:
            Enabled: '{{ Enabled }}'
            Idp:
              MetadataContent: '{{ MetadataContent }}'
              EntityId: '{{ EntityId }}'
            MasterUserName: '{{ MasterUserName }}'
            MasterBackendRole: '{{ MasterBackendRole }}'
            SubjectKey: '{{ SubjectKey }}'
            RolesKey: '{{ RolesKey }}'
            SessionTimeoutMinutes: '{{ SessionTimeoutMinutes }}'
          AnonymousAuthDisableDate: '{{ AnonymousAuthDisableDate }}'
      - name: EBSOptions
        value:
          EBSEnabled: '{{ EBSEnabled }}'
          VolumeType: '{{ VolumeType }}'
          Iops: '{{ Iops }}'
          VolumeSize: '{{ VolumeSize }}'
          Throughput: '{{ Throughput }}'
      - name: EncryptionAtRestOptions
        value:
          KmsKeyId: '{{ KmsKeyId }}'
          Enabled: '{{ Enabled }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: OffPeakWindowOptions
        value:
          Enabled: '{{ Enabled }}'
          OffPeakWindow:
            WindowStartTime:
              Hours: '{{ Hours }}'
              Minutes: '{{ Minutes }}'
      - name: SoftwareUpdateOptions
        value:
          AutoSoftwareUpdateEnabled: '{{ AutoSoftwareUpdateEnabled }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.opensearchservice.domains
WHERE data__Identifier = '<DomainName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>domains</code> resource, the following permissions are required:

### Create
```json
es:CreateDomain,
es:DescribeDomain,
es:AddTags,
es:ListTags
```

### Read
```json
es:DescribeDomain,
es:ListTags
```

### Update
```json
es:UpdateDomain,
es:UpgradeDomain,
es:DescribeDomain,
es:AddTags,
es:RemoveTags,
es:ListTags,
es:DescribeDomainChangeProgress
```

### Delete
```json
es:DeleteDomain,
es:DescribeDomain
```

