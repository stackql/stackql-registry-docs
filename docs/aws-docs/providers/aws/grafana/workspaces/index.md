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
    <td><CopyableCode code="AuthenticationProviders, PermissionType, AccountAccessType, region" /></td>
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

Use the following StackQL query and manifest file to create a new <code>workspace</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.grafana.workspaces (
 AuthenticationProviders,
 AccountAccessType,
 PermissionType,
 region
)
SELECT 
'{{ AuthenticationProviders }}',
 '{{ AccountAccessType }}',
 '{{ PermissionType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ AuthenticationProviders }}',
 '{{ SamlConfiguration }}',
 '{{ NetworkAccessControl }}',
 '{{ VpcConfiguration }}',
 '{{ ClientToken }}',
 '{{ GrafanaVersion }}',
 '{{ AccountAccessType }}',
 '{{ OrganizationRoleName }}',
 '{{ PermissionType }}',
 '{{ StackSetName }}',
 '{{ DataSources }}',
 '{{ Description }}',
 '{{ Name }}',
 '{{ NotificationDestinations }}',
 '{{ OrganizationalUnits }}',
 '{{ RoleArn }}',
 '{{ PluginAdminEnabled }}',
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
  - name: workspace
    props:
      - name: AuthenticationProviders
        value:
          - '{{ AuthenticationProviders[0] }}'
      - name: SamlConfiguration
        value:
          IdpMetadata:
            Url: '{{ Url }}'
            Xml: '{{ Xml }}'
          AssertionAttributes:
            Name: '{{ Name }}'
            Login: '{{ Login }}'
            Email: '{{ Email }}'
            Groups: '{{ Groups }}'
            Role: '{{ Role }}'
            Org: '{{ Org }}'
          RoleValues:
            Editor:
              - '{{ Editor[0] }}'
            Admin:
              - '{{ Admin[0] }}'
          AllowedOrganizations:
            - '{{ AllowedOrganizations[0] }}'
          LoginValidityDuration: null
      - name: NetworkAccessControl
        value:
          PrefixListIds:
            - '{{ PrefixListIds[0] }}'
          VpceIds:
            - '{{ VpceIds[0] }}'
      - name: VpcConfiguration
        value:
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
          SubnetIds:
            - '{{ SubnetIds[0] }}'
      - name: ClientToken
        value: '{{ ClientToken }}'
      - name: GrafanaVersion
        value: '{{ GrafanaVersion }}'
      - name: AccountAccessType
        value: '{{ AccountAccessType }}'
      - name: OrganizationRoleName
        value: '{{ OrganizationRoleName }}'
      - name: PermissionType
        value: '{{ PermissionType }}'
      - name: StackSetName
        value: '{{ StackSetName }}'
      - name: DataSources
        value:
          - '{{ DataSources[0] }}'
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: NotificationDestinations
        value:
          - '{{ NotificationDestinations[0] }}'
      - name: OrganizationalUnits
        value:
          - '{{ OrganizationalUnits[0] }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: PluginAdminEnabled
        value: '{{ PluginAdminEnabled }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
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

