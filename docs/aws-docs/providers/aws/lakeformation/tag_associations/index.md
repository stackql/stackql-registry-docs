---
title: tag_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_associations
  - lakeformation
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


Used to retrieve a list of <code>tag_associations</code> in a region or to create or delete a <code>tag_associations</code> resource, use <code>tag_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema representing a Lake Formation Tag Association. While tag associations are not explicit Lake Formation resources, this CloudFormation resource can be used to associate tags with Lake Formation entities.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lakeformation.tag_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resource_identifier" /></td><td><code>string</code></td><td>Unique string identifying the resource. Used as primary identifier, which ideally should be a string</td></tr>
<tr><td><CopyableCode code="tags_identifier" /></td><td><code>string</code></td><td>Unique string identifying the resource's tags. Used as primary identifier, which ideally should be a string</td></tr>
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
resource_identifier,
tags_identifier
FROM aws.lakeformation.tag_associations
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
 "Resource": {
  "Catalog": {},
  "Database": {
   "CatalogId": "{{ CatalogId }}",
   "Name": "{{ Name }}"
  },
  "Table": {
   "CatalogId": null,
   "DatabaseName": null,
   "Name": null,
   "TableWildcard": {}
  },
  "TableWithColumns": {
   "CatalogId": null,
   "DatabaseName": null,
   "Name": null,
   "ColumnNames": [
    null
   ]
  }
 },
 "LFTags": [
  {
   "CatalogId": null,
   "TagKey": "{{ TagKey }}",
   "TagValues": [
    "{{ TagValues[0] }}"
   ]
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.lakeformation.tag_associations (
 Resource,
 LFTags,
 region
)
SELECT 
{{ Resource }},
 {{ LFTags }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Resource": {
  "Catalog": {},
  "Database": {
   "CatalogId": "{{ CatalogId }}",
   "Name": "{{ Name }}"
  },
  "Table": {
   "CatalogId": null,
   "DatabaseName": null,
   "Name": null,
   "TableWildcard": {}
  },
  "TableWithColumns": {
   "CatalogId": null,
   "DatabaseName": null,
   "Name": null,
   "ColumnNames": [
    null
   ]
  }
 },
 "LFTags": [
  {
   "CatalogId": null,
   "TagKey": "{{ TagKey }}",
   "TagValues": [
    "{{ TagValues[0] }}"
   ]
  }
 ]
}
>>>
--all properties
INSERT INTO aws.lakeformation.tag_associations (
 Resource,
 LFTags,
 region
)
SELECT 
 {{ Resource }},
 {{ LFTags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lakeformation.tag_associations
WHERE data__Identifier = '<ResourceIdentifier|TagsIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>tag_associations</code> resource, the following permissions are required:

### Create
```json
lakeformation:AddLFTagsToResource,
glue:GetDatabase,
glue:GetTable
```

### Delete
```json
lakeformation:RemoveLFTagsFromResource,
glue:GetDatabase,
glue:GetTable
```

