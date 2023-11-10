---
title: microsoft_teams_channel_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - microsoft_teams_channel_configurations
  - chatbot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>microsoft_teams_channel_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>microsoft_teams_channel_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>microsoft_teams_channel_configurations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.chatbot.microsoft_teams_channel_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the configuration</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn
FROM aws.chatbot.microsoft_teams_channel_configurations
WHERE region = 'us-east-1'
```
