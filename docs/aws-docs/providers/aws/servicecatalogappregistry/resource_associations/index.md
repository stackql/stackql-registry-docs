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
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalogAppRegistry::ResourceAssociation</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicecatalogappregistry.resource_associations</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
application_arn,
resource_arn,
resource_type
FROM aws.servicecatalogappregistry.resource_associations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>resource_associations</code> resource, the following permissions are required:

### Create
```json
servicecatalog:AssociateResource,
cloudformation:DescribeStacks
```

### List
```json
servicecatalog:ListAssociatedResources
```

