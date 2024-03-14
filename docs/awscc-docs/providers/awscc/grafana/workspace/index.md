---
title: workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace
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
Gets an individual <code>workspace</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>workspace</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.grafana.workspace</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>authentication_providers</code></td><td><code>array</code></td><td>List of authentication providers to enable.</td></tr>
<tr><td><code>sso_client_id</code></td><td><code>string</code></td><td>The client ID of the AWS SSO Managed Application.</td></tr>
<tr><td><code>saml_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>network_access_control</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>vpc_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>saml_configuration_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>client_token</code></td><td><code>string</code></td><td>A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_timestamp</code></td><td><code>string</code></td><td>Timestamp when the workspace was created.</td></tr>
<tr><td><code>modification_timestamp</code></td><td><code>string</code></td><td>Timestamp when the workspace was last modified</td></tr>
<tr><td><code>grafana_version</code></td><td><code>string</code></td><td>The version of Grafana to support in your workspace.</td></tr>
<tr><td><code>endpoint</code></td><td><code>string</code></td><td>Endpoint for the Grafana workspace.</td></tr>
<tr><td><code>account_access_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>organization_role_name</code></td><td><code>string</code></td><td>The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.</td></tr>
<tr><td><code>permission_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stack_set_name</code></td><td><code>string</code></td><td>The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.</td></tr>
<tr><td><code>data_sources</code></td><td><code>array</code></td><td>List of data sources on the service managed IAM role.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of a workspace.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The id that uniquely identifies a Grafana workspace.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The user friendly name of a workspace.</td></tr>
<tr><td><code>notification_destinations</code></td><td><code>array</code></td><td>List of notification destinations on the customers service managed IAM role that the Grafana workspace can query.</td></tr>
<tr><td><code>organizational_units</code></td><td><code>array</code></td><td>List of Organizational Units containing AWS accounts the Grafana workspace can pull data from.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources.</td></tr>
<tr><td><code>plugin_admin_enabled</code></td><td><code>boolean</code></td><td>Allow workspace admins to install plugins</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.grafana.workspace
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>workspace</code> resource, the following permissions are required:

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

