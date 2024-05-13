---
title: integration_association
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_association
  - connect
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


Gets or updates an individual <code>integration_association</code> resource, use <code>integration_associations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::IntegrationAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.integration_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="integration_association_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="integration_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="integration_type" /></td><td><code>string</code></td><td></td></tr>
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
integration_association_id,
instance_id,
integration_arn,
integration_type
FROM aws.connect.integration_association
WHERE region = 'us-east-1' AND data__Identifier = '<InstanceId>|<IntegrationType>|<IntegrationArn>';
```


## Permissions

To operate on the <code>integration_association</code> resource, the following permissions are required:

### Read
```json
connect:ListBots,
connect:ListLambdaFunctions,
connect:ListIntegrationAssociations
```

