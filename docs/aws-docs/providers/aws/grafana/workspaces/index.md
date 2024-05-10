---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - grafana
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


Used to retrieve a list of <code>workspaces</code> in a region or to create or delete a <code>workspaces</code> resource, use <code>workspace</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Grafana::Workspace Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.grafana.workspaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The id that uniquely identifies a Grafana workspace.</td></tr>
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
FROM aws.grafana.workspaces
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
 "AuthenticationProviders": [
  "{{ AuthenticationProviders[0] }}"
 ],
 "AccountAccessType": "{{ AccountAccessType }}",
 "PermissionType": "{{ PermissionType }}"
}
>>>
--required properties only
INSERT INTO aws.grafana.workspaces (
 AuthenticationProviders,
 AccountAccessType,
 PermissionType,
 region
)
SELECT 
{{ AuthenticationProviders }},
 {{ AccountAccessType }},
 {{ PermissionType }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AuthenticationProviders": [
  "{{ AuthenticationProviders[0] }}"
 ],
 "SamlConfiguration": {
  "IdpMetadata": {
   "Url": "{{ Url }}",
   "Xml": "{{ Xml }}"
  },
  "AssertionAttributes": {
   "Name": "{{ Name }}",
   "Login": "{{ Login }}",
   "Email": "{{ Email }}",
   "Groups": "{{ Groups }}",
   "Role": "{{ Role }}",
   "Org": "{{ Org }}"
  },
  "RoleValues": {
   "Editor": [
    "{{ Editor[0] }}"
   ],
   "Admin": [
    "{{ Admin[0] }}"
   ]
  },
  "AllowedOrganizations": [
   "{{ AllowedOrganizations[0] }}"
  ],
  "LoginValidityDuration": null
 },
 "NetworkAccessControl": {
  "PrefixListIds": [
   "{{ PrefixListIds[0] }}"
  ],
  "VpceIds": [
   "{{ VpceIds[0] }}"
  ]
 },
 "VpcConfiguration": {
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ],
  "SubnetIds": [
   "{{ SubnetIds[0] }}"
  ]
 },
 "ClientToken": "{{ ClientToken }}",
 "GrafanaVersion": "{{ GrafanaVersion }}",
 "AccountAccessType": "{{ AccountAccessType }}",
 "OrganizationRoleName": "{{ OrganizationRoleName }}",
 "PermissionType": "{{ PermissionType }}",
 "StackSetName": "{{ StackSetName }}",
 "DataSources": [
  "{{ DataSources[0] }}"
 ],
 "Description": "{{ Description }}",
 "Name": "{{ Name }}",
 "NotificationDestinations": [
  "{{ NotificationDestinations[0] }}"
 ],
 "OrganizationalUnits": [
  "{{ OrganizationalUnits[0] }}"
 ],
 "RoleArn": "{{ RoleArn }}",
 "PluginAdminEnabled": "{{ PluginAdminEnabled }}"
}
>>>
--all properties
INSERT INTO aws.grafana.workspaces (
 AuthenticationProviders,
 SamlConfiguration,
 NetworkAccessControl,
 VpcConfiguration,
 ClientToken,
 GrafanaVersion,
 AccountAccessType,
 OrganizationRoleName,
 PermissionType,
 StackSetName,
 DataSources,
 Description,
 Name,
 NotificationDestinations,
 OrganizationalUnits,
 RoleArn,
 PluginAdminEnabled,
 region
)
SELECT 
 {{ AuthenticationProviders }},
 {{ SamlConfiguration }},
 {{ NetworkAccessControl }},
 {{ VpcConfiguration }},
 {{ ClientToken }},
 {{ GrafanaVersion }},
 {{ AccountAccessType }},
 {{ OrganizationRoleName }},
 {{ PermissionType }},
 {{ StackSetName }},
 {{ DataSources }},
 {{ Description }},
 {{ Name }},
 {{ NotificationDestinations }},
 {{ OrganizationalUnits }},
 {{ RoleArn }},
 {{ PluginAdminEnabled }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.grafana.workspaces
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>workspaces</code> resource, the following permissions are required:

### Create
```json
grafana:CreateWorkspace,
grafana:DescribeWorkspace,
grafana:DescribeWorkspaceAuthentication,
grafana:DescribeWorkspaceConfiguration,
grafana:UpdateWorkspaceAuthentication,
sso:DescribeRegisteredRegions,
sso:CreateManagedApplicationInstance,
organizations:DescribeOrganization,
sso:GetSharedSsoConfiguration,
iam:PassRole,
ec2:GetManagedPrefixListEntries,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
iam:CreateServiceLinkedRole,
sso:ListApplicationInstances,
sso:GetApplicationInstance
```

### Delete
```json
grafana:DeleteWorkspace,
grafana:DescribeWorkspace,
grafana:DescribeWorkspaceAuthentication,
grafana:DescribeWorkspaceConfiguration,
sso:DeleteManagedApplicationInstance,
sso:DescribeRegisteredRegions
```

### List
```json
grafana:ListWorkspaces,
grafana:DescribeWorkspaceAuthentication,
grafana:DescribeWorkspaceConfiguration
```

