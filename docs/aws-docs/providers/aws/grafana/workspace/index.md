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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>workspace</code> resource, use <code>workspaces</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Grafana::Workspace Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.grafana.workspace" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="authentication_providers" /></td><td><code>array</code></td><td>List of authentication providers to enable.</td></tr>
<tr><td><CopyableCode code="sso_client_id" /></td><td><code>string</code></td><td>The client ID of the AWS SSO Managed Application.</td></tr>
<tr><td><CopyableCode code="saml_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="network_access_control" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="saml_configuration_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td>A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_timestamp" /></td><td><code>string</code></td><td>Timestamp when the workspace was created.</td></tr>
<tr><td><CopyableCode code="modification_timestamp" /></td><td><code>string</code></td><td>Timestamp when the workspace was last modified</td></tr>
<tr><td><CopyableCode code="grafana_version" /></td><td><code>string</code></td><td>The version of Grafana to support in your workspace.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>Endpoint for the Grafana workspace.</td></tr>
<tr><td><CopyableCode code="account_access_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="organization_role_name" /></td><td><code>string</code></td><td>The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.</td></tr>
<tr><td><CopyableCode code="permission_type" /></td><td><code>string</code></td><td></td></tr>
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

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.grafana.workspace
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

