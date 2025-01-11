---
title: sync_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_configurations
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

Creates, updates, deletes or gets a <code>sync_configuration</code> resource or lists <code>sync_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for AWS::CodeStarConnections::SyncConfiguration resource which is used to enables an AWS resource to be synchronized from a source-provider.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codestarconnections.sync_configurations" /></td></tr>
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

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html"><code>AWS::CodeStarConnections::SyncConfiguration</code></a>.

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
    <td><CopyableCode code="Branch, ConfigFile, RepositoryLinkId, ResourceName, SyncType, RoleArn, region" /></td>
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
Gets all <code>sync_configurations</code> in a region.
```sql
SELECT
region,
owner_id,
resource_name,
repository_name,
provider_type,
branch,
config_file,
sync_type,
role_arn,
publish_deployment_status,
trigger_resource_update_on,
repository_link_id
FROM aws.codestarconnections.sync_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>sync_configuration</code>.
```sql
SELECT
region,
owner_id,
resource_name,
repository_name,
provider_type,
branch,
config_file,
sync_type,
role_arn,
publish_deployment_status,
trigger_resource_update_on,
repository_link_id
FROM aws.codestarconnections.sync_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<ResourceName>|<SyncType>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sync_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.codestarconnections.sync_configurations (
 ResourceName,
 Branch,
 ConfigFile,
 SyncType,
 RoleArn,
 RepositoryLinkId,
 region
)
SELECT 
'{{ ResourceName }}',
 '{{ Branch }}',
 '{{ ConfigFile }}',
 '{{ SyncType }}',
 '{{ RoleArn }}',
 '{{ RepositoryLinkId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.codestarconnections.sync_configurations (
 ResourceName,
 Branch,
 ConfigFile,
 SyncType,
 RoleArn,
 PublishDeploymentStatus,
 TriggerResourceUpdateOn,
 RepositoryLinkId,
 region
)
SELECT 
 '{{ ResourceName }}',
 '{{ Branch }}',
 '{{ ConfigFile }}',
 '{{ SyncType }}',
 '{{ RoleArn }}',
 '{{ PublishDeploymentStatus }}',
 '{{ TriggerResourceUpdateOn }}',
 '{{ RepositoryLinkId }}',
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
  - name: sync_configuration
    props:
      - name: ResourceName
        value: '{{ ResourceName }}'
      - name: Branch
        value: '{{ Branch }}'
      - name: ConfigFile
        value: '{{ ConfigFile }}'
      - name: SyncType
        value: '{{ SyncType }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: PublishDeploymentStatus
        value: '{{ PublishDeploymentStatus }}'
      - name: TriggerResourceUpdateOn
        value: '{{ TriggerResourceUpdateOn }}'
      - name: RepositoryLinkId
        value: '{{ RepositoryLinkId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.codestarconnections.sync_configurations
WHERE data__Identifier = '<ResourceName|SyncType>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>sync_configurations</code> resource, the following permissions are required:

### Create
```json
codestar-connections:CreateSyncConfiguration,
codestar-connections:PassRepository,
iam:PassRole
```

### Read
```json
codestar-connections:GetSyncConfiguration
```

### Update
```json
codestar-connections:UpdateSyncConfiguration,
codestar-connections:PassRepository,
iam:PassRole
```

### Delete
```json
codestar-connections:DeleteSyncConfiguration,
codestar-connections:GetSyncConfiguration
```

### List
```json
codestar-connections:ListSyncConfigurations,
codestar-connections:ListRepositoryLinks
```
