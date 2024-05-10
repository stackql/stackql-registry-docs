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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>resource_associations</code> in a region or to create or delete a <code>resource_associations</code> resource, use <code>resource_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalogAppRegistry::ResourceAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.servicecatalogappregistry.resource_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>The type of the CFN Resource for now it's enum CFN_STACK.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
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
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Application": "{{ Application }}",
 "Resource": "{{ Resource }}",
 "ResourceType": "{{ ResourceType }}"
}
>>>
--required properties only
INSERT INTO aws.servicecatalogappregistry.resource_associations (
 Application,
 Resource,
 ResourceType,
 region
)
SELECT 
{{ Application }},
 {{ Resource }},
 {{ ResourceType }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Application": "{{ Application }}",
 "Resource": "{{ Resource }}",
 "ResourceType": "{{ ResourceType }}"
}
>>>
--all properties
INSERT INTO aws.servicecatalogappregistry.resource_associations (
 Application,
 Resource,
 ResourceType,
 region
)
SELECT 
 {{ Application }},
 {{ Resource }},
 {{ ResourceType }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.servicecatalogappregistry.resource_associations
WHERE data__Identifier = '<ApplicationArn|ResourceArn|ResourceType>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_associations</code> resource, the following permissions are required:

### Create
```json
servicecatalog:AssociateResource,
cloudformation:DescribeStacks
```

### Delete
```json
servicecatalog:DisassociateResource
```

### List
```json
servicecatalog:ListAssociatedResources
```

