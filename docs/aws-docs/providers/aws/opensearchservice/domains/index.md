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


Used to retrieve a list of <code>domains</code> in a region or to create or delete a <code>domains</code> resource, use <code>domain</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchservice.domains" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
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
domain_name
FROM aws.opensearchservice.domains
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
 "ClusterConfig": {
  "InstanceCount": "{{ InstanceCount }}",
  "WarmEnabled": "{{ WarmEnabled }}",
  "WarmCount": "{{ WarmCount }}",
  "DedicatedMasterEnabled": "{{ DedicatedMasterEnabled }}",
  "ZoneAwarenessConfig": {
   "AvailabilityZoneCount": "{{ AvailabilityZoneCount }}"
  },
  "DedicatedMasterCount": "{{ DedicatedMasterCount }}",
  "InstanceType": "{{ InstanceType }}",
  "WarmType": "{{ WarmType }}",
  "ZoneAwarenessEnabled": "{{ ZoneAwarenessEnabled }}",
  "DedicatedMasterType": "{{ DedicatedMasterType }}",
  "MultiAZWithStandbyEnabled": "{{ MultiAZWithStandbyEnabled }}",
  "ColdStorageOptions": {
   "Enabled": "{{ Enabled }}"
  }
 },
 "DomainName": "{{ DomainName }}",
 "AccessPolicies": {},
 "IPAddressType": "{{ IPAddressType }}",
 "EngineVersion": "{{ EngineVersion }}",
 "AdvancedOptions": {},
 "LogPublishingOptions": {},
 "SnapshotOptions": {
  "AutomatedSnapshotStartHour": "{{ AutomatedSnapshotStartHour }}"
 },
 "VPCOptions": {
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ],
  "SubnetIds": [
   "{{ SubnetIds[0] }}"
  ]
 },
 "NodeToNodeEncryptionOptions": {
  "Enabled": "{{ Enabled }}"
 },
 "DomainEndpointOptions": {
  "CustomEndpointCertificateArn": "{{ CustomEndpointCertificateArn }}",
  "CustomEndpointEnabled": "{{ CustomEndpointEnabled }}",
  "EnforceHTTPS": "{{ EnforceHTTPS }}",
  "CustomEndpoint": "{{ CustomEndpoint }}",
  "TLSSecurityPolicy": "{{ TLSSecurityPolicy }}"
 },
 "CognitoOptions": {
  "Enabled": "{{ Enabled }}",
  "IdentityPoolId": "{{ IdentityPoolId }}",
  "UserPoolId": "{{ UserPoolId }}",
  "RoleArn": "{{ RoleArn }}"
 },
 "AdvancedSecurityOptions": {
  "Enabled": "{{ Enabled }}",
  "MasterUserOptions": {
   "MasterUserPassword": "{{ MasterUserPassword }}",
   "MasterUserName": "{{ MasterUserName }}",
   "MasterUserARN": "{{ MasterUserARN }}"
  },
  "InternalUserDatabaseEnabled": "{{ InternalUserDatabaseEnabled }}",
  "AnonymousAuthEnabled": "{{ AnonymousAuthEnabled }}",
  "SAMLOptions": {
   "Enabled": "{{ Enabled }}",
   "Idp": {
    "MetadataContent": "{{ MetadataContent }}",
    "EntityId": "{{ EntityId }}"
   },
   "MasterUserName": "{{ MasterUserName }}",
   "MasterBackendRole": "{{ MasterBackendRole }}",
   "SubjectKey": "{{ SubjectKey }}",
   "RolesKey": "{{ RolesKey }}",
   "SessionTimeoutMinutes": "{{ SessionTimeoutMinutes }}"
  },
  "AnonymousAuthDisableDate": "{{ AnonymousAuthDisableDate }}"
 },
 "EBSOptions": {
  "EBSEnabled": "{{ EBSEnabled }}",
  "VolumeType": "{{ VolumeType }}",
  "Iops": "{{ Iops }}",
  "VolumeSize": "{{ VolumeSize }}",
  "Throughput": "{{ Throughput }}"
 },
 "EncryptionAtRestOptions": {
  "KmsKeyId": "{{ KmsKeyId }}",
  "Enabled": "{{ Enabled }}"
 },
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "OffPeakWindowOptions": {
  "Enabled": "{{ Enabled }}",
  "OffPeakWindow": {
   "WindowStartTime": {
    "Hours": "{{ Hours }}",
    "Minutes": "{{ Minutes }}"
   }
  }
 },
 "SoftwareUpdateOptions": {
  "AutoSoftwareUpdateEnabled": "{{ AutoSoftwareUpdateEnabled }}"
 }
}
>>>
--required properties only
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
{{ .ClusterConfig }},
 {{ .DomainName }},
 {{ .AccessPolicies }},
 {{ .IPAddressType }},
 {{ .EngineVersion }},
 {{ .AdvancedOptions }},
 {{ .LogPublishingOptions }},
 {{ .SnapshotOptions }},
 {{ .VPCOptions }},
 {{ .NodeToNodeEncryptionOptions }},
 {{ .DomainEndpointOptions }},
 {{ .CognitoOptions }},
 {{ .AdvancedSecurityOptions }},
 {{ .EBSOptions }},
 {{ .EncryptionAtRestOptions }},
 {{ .Tags }},
 {{ .OffPeakWindowOptions }},
 {{ .SoftwareUpdateOptions }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ClusterConfig": {
  "InstanceCount": "{{ InstanceCount }}",
  "WarmEnabled": "{{ WarmEnabled }}",
  "WarmCount": "{{ WarmCount }}",
  "DedicatedMasterEnabled": "{{ DedicatedMasterEnabled }}",
  "ZoneAwarenessConfig": {
   "AvailabilityZoneCount": "{{ AvailabilityZoneCount }}"
  },
  "DedicatedMasterCount": "{{ DedicatedMasterCount }}",
  "InstanceType": "{{ InstanceType }}",
  "WarmType": "{{ WarmType }}",
  "ZoneAwarenessEnabled": "{{ ZoneAwarenessEnabled }}",
  "DedicatedMasterType": "{{ DedicatedMasterType }}",
  "MultiAZWithStandbyEnabled": "{{ MultiAZWithStandbyEnabled }}",
  "ColdStorageOptions": {
   "Enabled": "{{ Enabled }}"
  }
 },
 "DomainName": "{{ DomainName }}",
 "AccessPolicies": {},
 "IPAddressType": "{{ IPAddressType }}",
 "EngineVersion": "{{ EngineVersion }}",
 "AdvancedOptions": {},
 "LogPublishingOptions": {},
 "SnapshotOptions": {
  "AutomatedSnapshotStartHour": "{{ AutomatedSnapshotStartHour }}"
 },
 "VPCOptions": {
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ],
  "SubnetIds": [
   "{{ SubnetIds[0] }}"
  ]
 },
 "NodeToNodeEncryptionOptions": {
  "Enabled": "{{ Enabled }}"
 },
 "DomainEndpointOptions": {
  "CustomEndpointCertificateArn": "{{ CustomEndpointCertificateArn }}",
  "CustomEndpointEnabled": "{{ CustomEndpointEnabled }}",
  "EnforceHTTPS": "{{ EnforceHTTPS }}",
  "CustomEndpoint": "{{ CustomEndpoint }}",
  "TLSSecurityPolicy": "{{ TLSSecurityPolicy }}"
 },
 "CognitoOptions": {
  "Enabled": "{{ Enabled }}",
  "IdentityPoolId": "{{ IdentityPoolId }}",
  "UserPoolId": "{{ UserPoolId }}",
  "RoleArn": "{{ RoleArn }}"
 },
 "AdvancedSecurityOptions": {
  "Enabled": "{{ Enabled }}",
  "MasterUserOptions": {
   "MasterUserPassword": "{{ MasterUserPassword }}",
   "MasterUserName": "{{ MasterUserName }}",
   "MasterUserARN": "{{ MasterUserARN }}"
  },
  "InternalUserDatabaseEnabled": "{{ InternalUserDatabaseEnabled }}",
  "AnonymousAuthEnabled": "{{ AnonymousAuthEnabled }}",
  "SAMLOptions": {
   "Enabled": "{{ Enabled }}",
   "Idp": {
    "MetadataContent": "{{ MetadataContent }}",
    "EntityId": "{{ EntityId }}"
   },
   "MasterUserName": "{{ MasterUserName }}",
   "MasterBackendRole": "{{ MasterBackendRole }}",
   "SubjectKey": "{{ SubjectKey }}",
   "RolesKey": "{{ RolesKey }}",
   "SessionTimeoutMinutes": "{{ SessionTimeoutMinutes }}"
  },
  "AnonymousAuthDisableDate": "{{ AnonymousAuthDisableDate }}"
 },
 "EBSOptions": {
  "EBSEnabled": "{{ EBSEnabled }}",
  "VolumeType": "{{ VolumeType }}",
  "Iops": "{{ Iops }}",
  "VolumeSize": "{{ VolumeSize }}",
  "Throughput": "{{ Throughput }}"
 },
 "EncryptionAtRestOptions": {
  "KmsKeyId": "{{ KmsKeyId }}",
  "Enabled": "{{ Enabled }}"
 },
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "OffPeakWindowOptions": {
  "Enabled": "{{ Enabled }}",
  "OffPeakWindow": {
   "WindowStartTime": {
    "Hours": "{{ Hours }}",
    "Minutes": "{{ Minutes }}"
   }
  }
 },
 "SoftwareUpdateOptions": {
  "AutoSoftwareUpdateEnabled": "{{ AutoSoftwareUpdateEnabled }}"
 }
}
>>>
--all properties
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
 {{ .ClusterConfig }},
 {{ .DomainName }},
 {{ .AccessPolicies }},
 {{ .IPAddressType }},
 {{ .EngineVersion }},
 {{ .AdvancedOptions }},
 {{ .LogPublishingOptions }},
 {{ .SnapshotOptions }},
 {{ .VPCOptions }},
 {{ .NodeToNodeEncryptionOptions }},
 {{ .DomainEndpointOptions }},
 {{ .CognitoOptions }},
 {{ .AdvancedSecurityOptions }},
 {{ .EBSOptions }},
 {{ .EncryptionAtRestOptions }},
 {{ .Tags }},
 {{ .OffPeakWindowOptions }},
 {{ .SoftwareUpdateOptions }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
es:DeleteDomain,
es:DescribeDomain
```

