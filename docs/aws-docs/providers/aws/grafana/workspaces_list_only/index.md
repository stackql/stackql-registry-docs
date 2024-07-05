---
title: workspaces_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_list_only
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

Lists <code>workspaces</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/workspaces/"><code>workspaces</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Grafana::Workspace Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.grafana.workspaces_list_only" /></td></tr>
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

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>workspaces</code> in a region.
```sql
SELECT
region,
id
FROM aws.grafana.workspaces_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>workspaces_list_only</code> resource, see <a href="/providers/aws/grafana/workspaces/#permissions"><code>workspaces</code></a>


