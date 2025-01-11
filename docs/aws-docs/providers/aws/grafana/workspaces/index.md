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

Creates, updates, deletes or gets a <code>workspace</code> resource or lists <code>workspaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Grafana::Workspace Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.grafana.workspaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="authentication_providers" /></td><td><code>array</code></td><td>List of authentication providers to enable.</td></tr>
<tr><td><CopyableCode code="sso_client_id" /></td><td><code>string</code></td><td>The client ID of the AWS SSO Managed Application.</td></tr>
<tr><td><CopyableCode code="saml_configuration" /></td><td><code>object</code></td><td>SAML configuration data associated with an AMG workspace.</td></tr>
<tr><td><CopyableCode code="network_access_control" /></td><td><code>object</code></td><td>The configuration settings for Network Access Control.</td></tr>
<tr><td><CopyableCode code="vpc_configuration" /></td><td><code>object</code></td><td>The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.</td></tr>
<tr><td><CopyableCode code="saml_configuration_status" /></td><td><code>string</code></td><td>Valid SAML configuration statuses.</td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td>A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>These enums represent the status of a workspace.</td></tr>
<tr><td><CopyableCode code="creation_timestamp" /></td><td><code>string</code></td><td>Timestamp when the workspace was created.</td></tr>
<tr><td><CopyableCode code="modification_timestamp" /></td><td><code>string</code></td><td>Timestamp when the workspace was last modified</td></tr>
<tr><td><CopyableCode code="grafana_version" /></td><td><code>string</code></td><td>The version of Grafana to support in your workspace.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>Endpoint for the Grafana workspace.</td></tr>
<tr><td><CopyableCode code="account_access_type" /></td><td><code>string</code></td><td>These enums represent valid account access types. Specifically these enums determine whether the workspace can access AWS resources in the AWS account only, or whether it can also access resources in other accounts in the same organization. If the value CURRENT_ACCOUNT is used, a workspace role ARN must be provided. If the value is ORGANIZATION, a list of organizational units must be provided.</td></tr>
<tr><td><CopyableCode code="organization_role_name" /></td><td><code>string</code></td><td>The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.</td></tr>
<tr><td><CopyableCode code="permission_type" /></td><td><code>string</code></td><td>These enums represent valid permission types to use when creating or configuring a Grafana workspace. The SERVICE_MANAGED permission type means the Managed Grafana service will create a workspace IAM role on your behalf. The CUSTOMER_MANAGED permission type means that the customer is expected to provide an IAM role that the Grafana workspace can use to query data sources.</td></tr>
<tr><td><CopyableCode code="stack_set_name" /></td><td><code>string</code></td><td>The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.</td></tr>
<tr><td><CopyableCode code="data_sources" /></td><td><code>array</code></td><td>List of data sources on the service managed IAM role.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of a workspace.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The id that uniquely identifies a Grafana workspace.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The user friendly name of a workspace.</td></tr>
<tr><td><CopyableCode code="notification_destinations" /></td><td><code>array</code></td><td>List of notification destinations on the customers service managed IAM role that the Grafana workspace can query.</td></tr>
<tr><td><CopyableCode code="organizational_units" /></td><td><code>array</code></td><td>List of Organizational Units containing AWS accounts the Grafana workspace can pull data from.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources.</td></tr>
<tr><td><CopyableCode code="plugin_admin_enabled" /></td><td><code>boolean</code></td><td>Allow workspace admins to install plugins</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-grafana-workspace.html"><code>AWS::Grafana::Workspace</code></a>.

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
Gets all <code>workspaces</code> in a region.
```sql
SELECT
region,
authentication_providers,
sso_client_id,
saml_configuration,
network_access_control,
vpc_configuration,
saml_configuration_status,
client_token,
status,
creation_timestamp,
modification_timestamp,
grafana_version,
endpoint,
account_access_type,
organization_role_name,
permission_type,
stack_set_name,
data_sources,
description,
id,
name,
notification_destinations,
organizational_units,
role_arn,
plugin_admin_enabled
FROM aws.grafana.workspaces
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>workspace</code>.
```sql
SELECT
region,
authentication_providers,
sso_client_id,
saml_configuration,
network_access_control,
vpc_configuration,
saml_configuration_status,
client_token,
status,
creation_timestamp,
modification_timestamp,
grafana_version,
endpoint,
account_access_type,
organization_role_name,
permission_type,
stack_set_name,
data_sources,
description,
id,
name,
notification_destinations,
organizational_units,
role_arn,
plugin_admin_enabled
FROM aws.grafana.workspaces
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

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

## `DELETE` example

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

### Read
```json
grafana:DescribeWorkspace,
grafana:DescribeWorkspaceAuthentication,
grafana:DescribeWorkspaceConfiguration
```

### Update
```json
grafana:DescribeWorkspace,
grafana:DescribeWorkspaceAuthentication,
grafana:DescribeWorkspaceConfiguration,
grafana:UpdateWorkspace,
grafana:UpdateWorkspaceAuthentication,
grafana:UpdateWorkspaceConfiguration,
sso:DescribeRegisteredRegions,
sso:CreateManagedApplicationInstance,
ec2:GetManagedPrefixListEntries,
iam:PassRole,
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
