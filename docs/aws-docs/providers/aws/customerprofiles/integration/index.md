---
title: integration
hide_title: false
hide_table_of_contents: false
keywords:
  - integration
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


Gets or updates an individual <code>integration</code> resource, use <code>integrations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The resource schema for creating an Amazon Connect Customer Profiles Integration.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.integration" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="uri" /></td><td><code>string</code></td><td>The URI of the S3 bucket or any other type of data source.</td></tr>
<tr><td><CopyableCode code="flow_definition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="object_type_name" /></td><td><code>string</code></td><td>The name of the ObjectType defined for the 3rd party data in Profile Service</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this integration got created</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The time of this integration got last updated at</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags (keys and values) associated with the integration</td></tr>
<tr><td><CopyableCode code="object_type_names" /></td><td><code>array</code></td><td>The mapping between 3rd party event types and ObjectType names</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
domain_name,
uri,
flow_definition,
object_type_name,
created_at,
last_updated_at,
tags,
object_type_names
FROM aws.customerprofiles.integration
WHERE region = 'us-east-1' AND data__Identifier = '<DomainName>|<Uri>';
```


## Permissions

To operate on the <code>integration</code> resource, the following permissions are required:

### Read
```json
profile:GetIntegration
```

### Update
```json
profile:PutIntegration,
profile:GetIntegration,
appflow:CreateFlow,
app-integrations:GetEventIntegration,
app-integrations:CreateEventIntegrationAssociation,
app-integrations:ListEventIntegrationAssociations,
app-integrations:DeleteEventIntegrationAssociation,
events:ListTargetsByRule,
events:RemoveTargets,
events:DeleteRule,
events:PutRule,
events:PutTargets,
events:PutEvents,
profile:UntagResource,
profile:TagResource
```

