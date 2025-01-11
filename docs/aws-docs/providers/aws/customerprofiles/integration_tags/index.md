---
title: integration_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_tags
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

Expands all tag keys and values for <code>integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The resource schema for creating an Amazon Connect Customer Profiles Integration.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.integration_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="uri" /></td><td><code>string</code></td><td>The URI of the S3 bucket or any other type of data source.</td></tr>
<tr><td><CopyableCode code="flow_definition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="object_type_name" /></td><td><code>string</code></td><td>The name of the ObjectType defined for the 3rd party data in Profile Service</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this integration got created</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The time of this integration got last updated at</td></tr>
<tr><td><CopyableCode code="object_type_names" /></td><td><code>array</code></td><td>The mapping between 3rd party event types and ObjectType names</td></tr>
<tr><td><CopyableCode code="event_trigger_names" /></td><td><code>array</code></td><td>A list of unique names for active event triggers associated with the integration.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>integrations</code> in a region.
```sql
SELECT
region,
domain_name,
uri,
flow_definition,
object_type_name,
created_at,
last_updated_at,
object_type_names,
event_trigger_names,
tag_key,
tag_value
FROM aws.customerprofiles.integration_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>integration_tags</code> resource, see <a href="/providers/aws/customerprofiles/integrations/#permissions"><code>integrations</code></a>

