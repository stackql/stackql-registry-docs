---
title: attribute_group_association
hide_title: false
hide_table_of_contents: false
keywords:
  - attribute_group_association
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
Gets an individual <code>attribute_group_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attribute_group_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>attribute_group_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.servicecatalogappregistry.attribute_group_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application</code></td><td><code>string</code></td><td>The name or the Id of the Application.</td></tr>
<tr><td><code>attribute_group</code></td><td><code>string</code></td><td>The name or the Id of the AttributeGroup.</td></tr>
<tr><td><code>application_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>attribute_group_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
application,
attribute_group,
application_arn,
attribute_group_arn
FROM awscc.servicecatalogappregistry.attribute_group_association
WHERE region = 'us-east-1'
AND data__Identifier = '{ApplicationArn}';
AND data__Identifier = '{AttributeGroupArn}';
```

## Permissions

To operate on the <code>attribute_group_association</code> resource, the following permissions are required:

### Read
```json
servicecatalog:ListAttributeGroupsForApplication
```

### Delete
```json
servicecatalog:DisassociateAttributeGroup
```

