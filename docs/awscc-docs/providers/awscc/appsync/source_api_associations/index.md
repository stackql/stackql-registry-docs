---
title: source_api_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - source_api_associations
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
Retrieves a list of <code>source_api_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_api_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>source_api_associations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appsync.source_api_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>association_arn</code></td><td><code>string</code></td><td>ARN of the SourceApiAssociation.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>source_api_associations</code> resource, the following permissions are required:

### Create
```json
appsync:AssociateSourceGraphqlApi,
appsync:AssociateMergedGraphqlApi,
appsync:GetSourceApiAssociation
```

### List
```json
appsync:ListSourceApiAssociations
```


## Example
```sql
SELECT
region,
association_arn
FROM awscc.appsync.source_api_associations
WHERE region = 'us-east-1'
```
