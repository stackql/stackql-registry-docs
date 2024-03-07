---
title: sync_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_configuration
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
Gets an individual <code>sync_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>sync_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.codestarconnections.sync_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>owner_id</code></td><td><code>string</code></td><td>the ID of the entity that owns the repository.</td></tr>
<tr><td><code>resource_name</code></td><td><code>string</code></td><td>The name of the resource that is being synchronized to the repository.</td></tr>
<tr><td><code>repository_name</code></td><td><code>string</code></td><td>The name of the repository that is being synced to.</td></tr>
<tr><td><code>provider_type</code></td><td><code>string</code></td><td>The name of the external provider where your third-party code repository is configured.</td></tr>
<tr><td><code>branch</code></td><td><code>string</code></td><td>The name of the branch of the repository from which resources are to be synchronized,</td></tr>
<tr><td><code>config_file</code></td><td><code>string</code></td><td>The source provider repository path of the sync configuration file of the respective SyncType.</td></tr>
<tr><td><code>sync_type</code></td><td><code>string</code></td><td>The type of resource synchronization service that is to be configured, for example, CFN_STACK_SYNC.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The IAM Role that allows AWS to update CloudFormation stacks based on content in the specified repository.</td></tr>
<tr><td><code>repository_link_id</code></td><td><code>string</code></td><td>A UUID that uniquely identifies the RepositoryLink that the SyncConfig is associated with.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>sync_configuration</code> resource, the following permissions are required:

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


## Example
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
repository_link_id
FROM awscc.codestarconnections.sync_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ResourceName&gt;'
AND data__Identifier = '&lt;SyncType&gt;'
```
