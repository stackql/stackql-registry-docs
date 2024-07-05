---
title: calculated_attribute_definitions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - calculated_attribute_definitions_list_only
  - customerprofiles
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

Lists <code>calculated_attribute_definitions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/calculated_attribute_definitions/"><code>calculated_attribute_definitions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>calculated_attribute_definitions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A calculated attribute definition for Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.calculated_attribute_definitions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="calculated_attribute_name" /></td><td><code>string</code></td><td>The unique name of the calculated attribute.</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>The display name of the calculated attribute.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the calculated attribute.</td></tr>
<tr><td><CopyableCode code="attribute_details" /></td><td><code>object</code></td><td>Mathematical expression and a list of attribute items specified in that expression.</td></tr>
<tr><td><CopyableCode code="conditions" /></td><td><code>object</code></td><td>The conditions including range, object count, and threshold for the calculated attribute.</td></tr>
<tr><td><CopyableCode code="statistic" /></td><td><code>string</code></td><td>The aggregation operation to perform for the calculated attribute.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the calculated attribute definition was created.</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The timestamp of when the calculated attribute definition was most recently edited.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
Lists all <code>calculated_attribute_definitions</code> in a region.
```sql
SELECT
region,
domain_name,
calculated_attribute_name
FROM aws.customerprofiles.calculated_attribute_definitions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>calculated_attribute_definitions_list_only</code> resource, see <a href="/providers/aws/customerprofiles/calculated_attribute_definitions/#permissions"><code>calculated_attribute_definitions</code></a>


