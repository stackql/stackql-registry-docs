---
title: workspaces_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_pools
  - workspaces
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

Creates, updates, deletes or gets a <code>workspaces_pool</code> resource or lists <code>workspaces_pools</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::WorkSpaces::WorkspacesPool</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.workspaces.workspaces_pools" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pool_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capacity" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="pool_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="bundle_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="directory_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="timeout_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspacespool.html"><code>AWS::WorkSpaces::WorkspacesPool</code></a>.

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
    <td><CopyableCode code="PoolName, BundleId, DirectoryId, Capacity, region" /></td>
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
Gets all <code>workspaces_pools</code> in a region.
```sql
SELECT
region,
pool_id,
pool_arn,
capacity,
pool_name,
description,
created_at,
bundle_id,
directory_id,
application_settings,
timeout_settings,
tags
FROM aws.workspaces.workspaces_pools
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>workspaces_pool</code>.
```sql
SELECT
region,
pool_id,
pool_arn,
capacity,
pool_name,
description,
created_at,
bundle_id,
directory_id,
application_settings,
timeout_settings,
tags
FROM aws.workspaces.workspaces_pools
WHERE region = 'us-east-1' AND data__Identifier = '<PoolId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspaces_pool</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.workspaces.workspaces_pools (
 Capacity,
 PoolName,
 BundleId,
 DirectoryId,
 region
)
SELECT 
'{{ Capacity }}',
 '{{ PoolName }}',
 '{{ BundleId }}',
 '{{ DirectoryId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.workspaces.workspaces_pools (
 Capacity,
 PoolName,
 Description,
 BundleId,
 DirectoryId,
 ApplicationSettings,
 TimeoutSettings,
 Tags,
 region
)
SELECT 
 '{{ Capacity }}',
 '{{ PoolName }}',
 '{{ Description }}',
 '{{ BundleId }}',
 '{{ DirectoryId }}',
 '{{ ApplicationSettings }}',
 '{{ TimeoutSettings }}',
 '{{ Tags }}',
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
  - name: workspaces_pool
    props:
      - name: Capacity
        value:
          DesiredUserSessions: '{{ DesiredUserSessions }}'
      - name: PoolName
        value: '{{ PoolName }}'
      - name: Description
        value: '{{ Description }}'
      - name: BundleId
        value: '{{ BundleId }}'
      - name: DirectoryId
        value: '{{ DirectoryId }}'
      - name: ApplicationSettings
        value:
          Status: '{{ Status }}'
          SettingsGroup: '{{ SettingsGroup }}'
      - name: TimeoutSettings
        value:
          DisconnectTimeoutInSeconds: '{{ DisconnectTimeoutInSeconds }}'
          IdleDisconnectTimeoutInSeconds: '{{ IdleDisconnectTimeoutInSeconds }}'
          MaxUserDurationInSeconds: '{{ MaxUserDurationInSeconds }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.workspaces.workspaces_pools
WHERE data__Identifier = '<PoolId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>workspaces_pools</code> resource, the following permissions are required:

### Create
```json
workspaces:CreateWorkspacesPool,
workspaces:DescribeWorkspacesPools
```

### Read
```json
workspaces:DescribeWorkspacesPools
```

### Update
```json
workspaces:UpdateWorkspacesPool
```

### Delete
```json
workspaces:DescribeWorkspacesPools,
workspaces:TerminateWorkspacesPool
```

### List
```json
workspaces:DescribeWorkspacesPools
```
