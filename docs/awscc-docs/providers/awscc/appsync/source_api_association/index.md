---
title: source_api_association
hide_title: false
hide_table_of_contents: false
keywords:
  - source_api_association
  - appsync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>source_api_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_api_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>source_api_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appsync.source_api_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>source_api_identifier</code></td><td><code>string</code></td><td>Identifier of the Source GraphQLApi to associate. It could be either GraphQLApi ApiId or ARN</td></tr>
<tr><td><code>merged_api_identifier</code></td><td><code>string</code></td><td>Identifier of the Merged GraphQLApi to associate. It could be either GraphQLApi ApiId or ARN</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of the SourceApiAssociation.</td></tr>
<tr><td><code>source_api_association_config</code></td><td><code>undefined</code></td><td>Customized configuration for SourceApiAssociation.</td></tr>
<tr><td><code>association_id</code></td><td><code>string</code></td><td>Id of the SourceApiAssociation.</td></tr>
<tr><td><code>association_arn</code></td><td><code>string</code></td><td>ARN of the SourceApiAssociation.</td></tr>
<tr><td><code>source_api_id</code></td><td><code>string</code></td><td>GraphQLApiId of the source API in the association.</td></tr>
<tr><td><code>source_api_arn</code></td><td><code>string</code></td><td>ARN of the source API in the association.</td></tr>
<tr><td><code>merged_api_id</code></td><td><code>string</code></td><td>GraphQLApiId of the Merged API in the association.</td></tr>
<tr><td><code>merged_api_arn</code></td><td><code>string</code></td><td>ARN of the Merged API in the association.</td></tr>
<tr><td><code>source_api_association_status</code></td><td><code>string</code></td><td>Current status of SourceApiAssociation.</td></tr>
<tr><td><code>source_api_association_status_detail</code></td><td><code>string</code></td><td>Current SourceApiAssociation status details.</td></tr>
<tr><td><code>last_successful_merge_date</code></td><td><code>string</code></td><td>Date of last schema successful merge.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
source_api_identifier,
merged_api_identifier,
description,
source_api_association_config,
association_id,
association_arn,
source_api_id,
source_api_arn,
merged_api_id,
merged_api_arn,
source_api_association_status,
source_api_association_status_detail,
last_successful_merge_date
FROM awscc.appsync.source_api_association
WHERE data__Identifier = '<AssociationArn>';
```

## Permissions

To operate on the <code>source_api_association</code> resource, the following permissions are required:

### Read
```json
appsync:GetSourceApiAssociation,
appsync:ListSourceApiAssociations
```

### Update
```json
appsync:GetSourceApiAssociation,
appsync:UpdateSourceApiAssociation,
appsync:GetSourceApiAssociation
```

### Delete
```json
appsync:GetSourceApiAssociation,
appsync:DisassociateSourceGraphqlApi,
appsync:DisassociateMergedGraphqlApi,
appsync:ListSourceApiAssociations
```

