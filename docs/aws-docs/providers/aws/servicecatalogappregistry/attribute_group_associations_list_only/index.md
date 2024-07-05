---
title: attribute_group_associations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - attribute_group_associations_list_only
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

Lists <code>attribute_group_associations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/attribute_group_associations/"><code>attribute_group_associations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attribute_group_associations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.servicecatalogappregistry.attribute_group_associations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application" /></td><td><code>string</code></td><td>The name or the Id of the Application.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>attribute_group_associations</code> in a region.
```sql
SELECT
region,
application_arn,
attribute_group_arn
FROM aws.servicecatalogappregistry.attribute_group_associations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>attribute_group_associations_list_only</code> resource, see <a href="/providers/aws/servicecatalogappregistry/attribute_group_associations/#permissions"><code>attribute_group_associations</code></a>


