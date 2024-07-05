---
title: slack_workspace_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - slack_workspace_configurations
  - supportapp
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

Creates, updates, deletes or gets a <code>slack_workspace_configuration</code> resource or lists <code>slack_workspace_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>slack_workspace_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An AWS Support App resource that creates, updates, lists, and deletes Slack workspace configurations.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.supportapp.slack_workspace_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="team_id" /></td><td><code>string</code></td><td>The team ID in Slack, which uniquely identifies a workspace.</td></tr>
<tr><td><CopyableCode code="version_id" /></td><td><code>string</code></td><td>An identifier used to update an existing Slack workspace configuration in AWS CloudFormation.</td></tr>
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
    <td><CopyableCode code="TeamId, region" /></td>
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
Gets all <code>slack_workspace_configurations</code> in a region.
```sql
SELECT
region,
team_id,
version_id
FROM aws.supportapp.slack_workspace_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>slack_workspace_configuration</code>.
```sql
SELECT
region,
team_id,
version_id
FROM aws.supportapp.slack_workspace_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<TeamId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>slack_workspace_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.supportapp.slack_workspace_configurations (
 TeamId,
 region
)
SELECT 
'{{ TeamId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.supportapp.slack_workspace_configurations (
 TeamId,
 VersionId,
 region
)
SELECT 
 '{{ TeamId }}',
 '{{ VersionId }}',
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
  - name: slack_workspace_configuration
    props:
      - name: TeamId
        value: '{{ TeamId }}'
      - name: VersionId
        value: '{{ VersionId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.supportapp.slack_workspace_configurations
WHERE data__Identifier = '<TeamId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>slack_workspace_configurations</code> resource, the following permissions are required:

### Create
```json
supportapp:RegisterSlackWorkspaceForOrganization,
supportapp:ListSlackWorkspaceConfigurations
```

### Read
```json
supportapp:ListSlackWorkspaceConfigurations
```

### Update
```json
supportapp:RegisterSlackWorkspaceForOrganization,
supportapp:ListSlackWorkspaceConfigurations
```

### Delete
```json
supportapp:ListSlackWorkspaceConfigurations,
supportapp:DeleteSlackWorkspaceConfiguration
```

### List
```json
supportapp:ListSlackWorkspaceConfigurations
```

