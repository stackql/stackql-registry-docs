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
Retrieves a list of <code>workspaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.grafana.workspaces</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AuthenticationProviders</code></td><td><code>array</code></td><td>List of authentication providers to enable.</td></tr><tr><td><code>SsoClientId</code></td><td><code>string</code></td><td>The client ID of the AWS SSO Managed Application.</td></tr><tr><td><code>SamlConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>NetworkAccessControl</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>VpcConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>SamlConfigurationStatus</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ClientToken</code></td><td><code>string</code></td><td>A unique, case-sensitive, user-provided identifier to ensure the idempotency of the request.</td></tr><tr><td><code>Status</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>CreationTimestamp</code></td><td><code>string</code></td><td>Timestamp when the workspace was created.</td></tr><tr><td><code>ModificationTimestamp</code></td><td><code>string</code></td><td>Timestamp when the workspace was last modified</td></tr><tr><td><code>GrafanaVersion</code></td><td><code>string</code></td><td>Version of Grafana the workspace is currently using.</td></tr><tr><td><code>Endpoint</code></td><td><code>string</code></td><td>Endpoint for the Grafana workspace.</td></tr><tr><td><code>AccountAccessType</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>OrganizationRoleName</code></td><td><code>string</code></td><td>The name of an IAM role that already exists to use with AWS Organizations to access AWS data sources and notification channels in other accounts in an organization.</td></tr><tr><td><code>PermissionType</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>StackSetName</code></td><td><code>string</code></td><td>The name of the AWS CloudFormation stack set to use to generate IAM roles to be used for this workspace.</td></tr><tr><td><code>DataSources</code></td><td><code>array</code></td><td>List of data sources on the service managed IAM role.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>Description of a workspace.</td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td>The id that uniquely identifies a Grafana workspace.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The user friendly name of a workspace.</td></tr><tr><td><code>NotificationDestinations</code></td><td><code>array</code></td><td>List of notification destinations on the customers service managed IAM role that the Grafana workspace can query.</td></tr><tr><td><code>OrganizationalUnits</code></td><td><code>array</code></td><td>List of Organizational Units containing AWS accounts the Grafana workspace can pull data from.</td></tr><tr><td><code>RoleArn</code></td><td><code>string</code></td><td>IAM Role that will be used to grant the Grafana workspace access to a customers AWS resources.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.grafana.workspaces
WHERE region = 'us-east-1'
```
