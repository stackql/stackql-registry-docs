---
title: wal_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - wal_workspaces
  - emr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>wal_workspaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wal_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>wal_workspaces</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.emr.wal_workspaces</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>w_al_workspace_name</code></td><td><code>string</code></td><td>The name of the emrwal container</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>wal_workspaces</code> resource, the following permissions are required:

### Create
<pre>
emrwal:CreateWorkspace,
emrwal:TagResource,
iam:CreateServiceLinkedRole</pre>

### List
<pre>
emrwal:ListWorkspaces</pre>


## Example
```sql
SELECT
region,
w_al_workspace_name
FROM awscc.emr.wal_workspaces
WHERE region = 'us-east-1'
```
