---
title: resource_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_associations
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
Retrieves a list of <code>resource_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_associations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.servicecatalogappregistry.resource_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_type</code></td><td><code>string</code></td><td>The type of the CFN Resource for now it's enum CFN_STACK.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resource_associations</code> resource, the following permissions are required:

### Create
<pre>
servicecatalog:AssociateResource,
cloudformation:DescribeStacks</pre>

### List
<pre>
servicecatalog:ListAssociatedResources</pre>


## Example
```sql
SELECT
region,
application_arn,
resource_arn,
resource_type
FROM awscc.servicecatalogappregistry.resource_associations
WHERE region = 'us-east-1'
```
