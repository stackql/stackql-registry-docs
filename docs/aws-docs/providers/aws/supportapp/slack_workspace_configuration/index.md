---
title: slack_workspace_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - slack_workspace_configuration
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
Gets an individual <code>slack_workspace_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>slack_workspace_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An AWS Support App resource that creates, updates, lists, and deletes Slack workspace configurations.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.supportapp.slack_workspace_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>team_id</code></td><td><code>string</code></td><td>The team ID in Slack, which uniquely identifies a workspace.</td></tr>
<tr><td><code>version_id</code></td><td><code>string</code></td><td>An identifier used to update an existing Slack workspace configuration in AWS CloudFormation.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
team_id,
version_id
FROM aws.supportapp.slack_workspace_configuration
WHERE data__Identifier = '<TeamId>';
```

## Permissions

To operate on the <code>slack_workspace_configuration</code> resource, the following permissions are required:

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

