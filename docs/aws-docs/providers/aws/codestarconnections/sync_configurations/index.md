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


Used to retrieve a list of <code>sync_configurations</code> in a region or to create or delete a <code>sync_configurations</code> resource, use <code>sync_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for AWS::CodeStarConnections::SyncConfiguration resource which is used to enables an AWS resource to be synchronized from a source-provider.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codestarconnections.sync_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resource_name" /></td><td><code>string</code></td><td>The name of the resource that is being synchronized to the repository.</td></tr>
<tr><td><CopyableCode code="sync_type" /></td><td><code>string</code></td><td>The type of resource synchronization service that is to be configured, for example, CFN_STACK_SYNC.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
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
resource_name,
sync_type
FROM aws.codestarconnections.sync_configurations
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "ResourceName": "{{ ResourceName }}",
 "Branch": "{{ Branch }}",
 "ConfigFile": "{{ ConfigFile }}",
 "SyncType": "{{ SyncType }}",
 "RoleArn": "{{ RoleArn }}",
 "RepositoryLinkId": "{{ RepositoryLinkId }}"
}
>>>
--required properties only
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
{{ ResourceName }},
 {{ Branch }},
 {{ ConfigFile }},
 {{ SyncType }},
 {{ RoleArn }},
 {{ RepositoryLinkId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ResourceName": "{{ ResourceName }}",
 "Branch": "{{ Branch }}",
 "ConfigFile": "{{ ConfigFile }}",
 "SyncType": "{{ SyncType }}",
 "RoleArn": "{{ RoleArn }}",
 "PublishDeploymentStatus": "{{ PublishDeploymentStatus }}",
 "TriggerResourceUpdateOn": "{{ TriggerResourceUpdateOn }}",
 "RepositoryLinkId": "{{ RepositoryLinkId }}"
}
>>>
--all properties
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
 {{ ResourceName }},
 {{ Branch }},
 {{ ConfigFile }},
 {{ SyncType }},
 {{ RoleArn }},
 {{ PublishDeploymentStatus }},
 {{ TriggerResourceUpdateOn }},
 {{ RepositoryLinkId }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

