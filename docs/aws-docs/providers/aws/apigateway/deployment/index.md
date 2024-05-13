---
title: deployment
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment
  - apigateway
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


Gets or updates an individual <code>deployment</code> resource, use <code>deployments</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::Deployment</code> resource deploys an API Gateway <code>RestApi</code> resource to a stage so that clients can call the API over the internet. The stage acts as an environment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.deployment" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="deployment_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deployment_canary_settings" /></td><td><code>object</code></td><td>The input configuration for a canary deployment.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description for the Deployment resource to create.</td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><CopyableCode code="stage_description" /></td><td><code>object</code></td><td>The description of the Stage resource for the Deployment resource to create. To specify a stage description, you must also provide a stage name.</td></tr>
<tr><td><CopyableCode code="stage_name" /></td><td><code>string</code></td><td>The name of the Stage resource for the Deployment resource to create.</td></tr>
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
deployment_id,
deployment_canary_settings,
description,
rest_api_id,
stage_description,
stage_name
FROM aws.apigateway.deployment
WHERE region = 'us-east-1' AND data__Identifier = '<DeploymentId>|<RestApiId>';
```


## Permissions

To operate on the <code>deployment</code> resource, the following permissions are required:

### Read
```json
apigateway:GET
```

### Update
```json
apigateway:PATCH,
apigateway:GET,
apigateway:PUT,
apigateway:DELETE
```

