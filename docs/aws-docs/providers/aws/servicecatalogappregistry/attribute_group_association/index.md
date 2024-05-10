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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>attribute_group_association</code> resource, use <code>attribute_group_associations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attribute_group_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.servicecatalogappregistry.attribute_group_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application" /></td><td><code>string</code></td><td>The name or the Id of the Application.</td></tr>
<tr><td><CopyableCode code="attribute_group" /></td><td><code>string</code></td><td>The name or the Id of the AttributeGroup.</td></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="attribute_group_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
application,
attribute_group,
application_arn,
attribute_group_arn
FROM aws.servicecatalogappregistry.attribute_group_association
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationArn>|<AttributeGroupArn>';
```


## Permissions

To operate on the <code>attribute_group_association</code> resource, the following permissions are required:

### Read
```json
servicecatalog:ListAttributeGroupsForApplication
```

