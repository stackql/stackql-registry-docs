---
title: endpoint_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_tags
  - sagemaker
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

Expands all tag keys and values for <code>endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Endpoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.endpoint_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="deployment_config" /></td><td><code>object</code></td><td>Specifies deployment configuration for updating the SageMaker endpoint. Includes rollback and update policies.</td></tr>
<tr><td><CopyableCode code="endpoint_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the endpoint.</td></tr>
<tr><td><CopyableCode code="endpoint_config_name" /></td><td><code>string</code></td><td>The name of the endpoint configuration for the SageMaker endpoint. This is a required property.</td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td>The name of the SageMaker endpoint. This name must be unique within an AWS Region.</td></tr>
<tr><td><CopyableCode code="exclude_retained_variant_properties" /></td><td><code>array</code></td><td>Specifies a list of variant properties that you want to exclude when updating an endpoint.</td></tr>
<tr><td><CopyableCode code="retain_all_variant_properties" /></td><td><code>boolean</code></td><td>When set to true, retains all variant properties for an endpoint when it is updated.</td></tr>
<tr><td><CopyableCode code="retain_deployment_config" /></td><td><code>boolean</code></td><td>When set to true, retains the deployment configuration during endpoint updates.</td></tr>
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
Expands tags for all <code>endpoints</code> in a region.
```sql
SELECT
region,
deployment_config,
endpoint_arn,
endpoint_config_name,
endpoint_name,
exclude_retained_variant_properties,
retain_all_variant_properties,
retain_deployment_config,
tag_key,
tag_value
FROM aws.sagemaker.endpoint_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>endpoint_tags</code> resource, see <a href="/providers/aws/sagemaker/endpoints/#permissions"><code>endpoints</code></a>

