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
<tr><td><b>Id</b></td><td><code>aws.supportapp.slack_workspace_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>TeamId</code></td><td><code>string</code></td><td>The team ID in Slack, which uniquely identifies a workspace.</td></tr><tr><td><code>VersionId</code></td><td><code>string</code></td><td>An identifier used to update an existing Slack workspace configuration in AWS CloudFormation.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.supportapp.slack_workspace_configuration
WHERE region = 'us-east-1' AND data__Identifier = '{TeamId}'
```
