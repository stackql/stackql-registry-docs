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
<tr><td><b>Description</b></td><td>workspaces</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.grafana.workspaces</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The id that uniquely identifies a Grafana workspace.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id
FROM awscc.grafana.workspaces
WHERE region = 'us-east-1'
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

### List
```json
grafana:ListWorkspaces,
grafana:DescribeWorkspaceAuthentication,
grafana:DescribeWorkspaceConfiguration
```

