---
title: resource_association
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_association
  - servicecatalogappregistry
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>resource_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.servicecatalogappregistry.resource_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application</code></td><td><code>string</code></td><td>The name or the Id of the Application.</td></tr>
<tr><td><code>resource</code></td><td><code>string</code></td><td>The name or the Id of the Resource.</td></tr>
<tr><td><code>resource_type</code></td><td><code>string</code></td><td>The type of the CFN Resource for now it's enum CFN_STACK.</td></tr>
<tr><td><code>application_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
application,
resource,
resource_type,
application_arn,
resource_arn
FROM awscc.servicecatalogappregistry.resource_association
WHERE region = 'us-east-1'
AND data__Identifier = '{ApplicationArn}';
AND data__Identifier = '{ResourceArn}';
AND data__Identifier = '{ResourceType}';
```

## Permissions

To operate on the <code>resource_association</code> resource, the following permissions are required:

### Read
```json
servicecatalog:ListAssociatedResources
```

### Delete
```json
servicecatalog:DisassociateResource
```

