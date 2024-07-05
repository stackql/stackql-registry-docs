---
title: sync_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_configurations_list_only
  - codestarconnections
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

Lists <code>sync_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/sync_configurations/"><code>sync_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for AWS::CodeStarConnections::SyncConfiguration resource which is used to enables an AWS resource to be synchronized from a source-provider.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codestarconnections.sync_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>the ID of the entity that owns the repository.</td></tr>
<tr><td><CopyableCode code="resource_name" /></td><td><code>string</code></td><td>The name of the resource that is being synchronized to the repository.</td></tr>
<tr><td><CopyableCode code="repository_name" /></td><td><code>string</code></td><td>The name of the repository that is being synced to.</td></tr>
<tr><td><CopyableCode code="provider_type" /></td><td><code>string</code></td><td>The name of the external provider where your third-party code repository is configured.</td></tr>
<tr><td><CopyableCode code="branch" /></td><td><code>string</code></td><td>The name of the branch of the repository from which resources are to be synchronized,</td></tr>
<tr><td><CopyableCode code="config_file" /></td><td><code>string</code></td><td>The source provider repository path of the sync configuration file of the respective SyncType.</td></tr>
<tr><td><CopyableCode code="sync_type" /></td><td><code>string</code></td><td>The type of resource synchronization service that is to be configured, for example, CFN_STACK_SYNC.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The IAM Role that allows AWS to update CloudFormation stacks based on content in the specified repository.</td></tr>
<tr><td><CopyableCode code="publish_deployment_status" /></td><td><code>string</code></td><td>Whether to enable or disable publishing of deployment status to source providers.</td></tr>
<tr><td><CopyableCode code="trigger_resource_update_on" /></td><td><code>string</code></td><td>When to trigger Git sync to begin the stack update.</td></tr>
<tr><td><CopyableCode code="repository_link_id" /></td><td><code>string</code></td><td>A UUID that uniquely identifies the RepositoryLink that the SyncConfig is associated with.</td></tr>
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
Lists all <code>sync_configurations</code> in a region.
```sql
SELECT
region,
resource_name,
sync_type
FROM aws.codestarconnections.sync_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>sync_configurations_list_only</code> resource, see <a href="/providers/aws/codestarconnections/sync_configurations/#permissions"><code>sync_configurations</code></a>


