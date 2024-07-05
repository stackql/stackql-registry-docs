---
title: projects_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - projects_list_only
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

Lists <code>projects</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/projects/"><code>projects</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Project</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.projects_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="project_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Project.</td></tr>
<tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td>Project Id.</td></tr>
<tr><td><CopyableCode code="project_name" /></td><td><code>string</code></td><td>The name of the project.</td></tr>
<tr><td><CopyableCode code="project_description" /></td><td><code>string</code></td><td>The description of the project.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the project was created.</td></tr>
<tr><td><CopyableCode code="service_catalog_provisioning_details" /></td><td><code>object</code></td><td>Input ServiceCatalog Provisioning Details</td></tr>
<tr><td><CopyableCode code="service_catalog_provisioned_product_details" /></td><td><code>object</code></td><td>Provisioned ServiceCatalog Details</td></tr>
<tr><td><CopyableCode code="project_status" /></td><td><code>string</code></td><td>The status of a project.</td></tr>
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
Lists all <code>projects</code> in a region.
```sql
SELECT
region,
project_arn
FROM aws.sagemaker.projects_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>projects_list_only</code> resource, see <a href="/providers/aws/sagemaker/projects/#permissions"><code>projects</code></a>


