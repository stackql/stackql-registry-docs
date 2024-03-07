---
title: network_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - network_settings
  - workspacesweb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>network_settings</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>network_settings</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.workspacesweb.network_settings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>associated_portal_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>network_settings_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>network_settings</code> resource, the following permissions are required:

### Read
<pre>
workspaces-web:GetNetworkSettings,
workspaces-web:ListTagsForResource</pre>

### Update
<pre>
workspaces-web:UpdateNetworkSettings,
workspaces-web:UpdateResource,
workspaces-web:TagResource,
workspaces-web:UntagResource,
workspaces-web:GetNetworkSettings,
workspaces-web:ListTagsForResource</pre>

### Delete
<pre>
workspaces-web:GetNetworkSettings,
workspaces-web:DeleteNetworkSettings</pre>


## Example
```sql
SELECT
region,
associated_portal_arns,
network_settings_arn,
security_group_ids,
subnet_ids,
tags,
vpc_id
FROM awscc.workspacesweb.network_settings
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;NetworkSettingsArn&gt;'
```
