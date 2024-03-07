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
Retrieves a list of <code>sync_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>sync_configurations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.codestarconnections.sync_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource_name</code></td><td><code>string</code></td><td>The name of the resource that is being synchronized to the repository.</td></tr>
<tr><td><code>sync_type</code></td><td><code>string</code></td><td>The type of resource synchronization service that is to be configured, for example, CFN_STACK_SYNC.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>sync_configurations</code> resource, the following permissions are required:

### Create
```json
codestar-connections:CreateSyncConfiguration,
codestar-connections:PassRepository,
iam:PassRole
```

### List
```json
codestar-connections:ListSyncConfigurations,
codestar-connections:ListRepositoryLinks
```


## Example
```sql
SELECT
region,
resource_name,
sync_type
FROM awscc.codestarconnections.sync_configurations
WHERE region = 'us-east-1'
```
