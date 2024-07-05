---
title: application_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - application_tags
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

Expands all tag keys and values for <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalogAppRegistry::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.servicecatalogappregistry.application_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the application.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the application.</td></tr>
<tr><td><CopyableCode code="application_tag_key" /></td><td><code>string</code></td><td>The key of the AWS application tag, which is awsApplication. Applications created before 11/13/2023 or applications without the AWS application tag resource group return no value.</td></tr>
<tr><td><CopyableCode code="application_tag_value" /></td><td><code>string</code></td><td>The value of the AWS application tag, which is the identifier of an associated resource. Applications created before 11/13/2023 or applications without the AWS application tag resource group return no value.</td></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the application.</td></tr>
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
Expands tags for all <code>applications</code> in a region.
```sql
SELECT
region,
id,
arn,
name,
description,
application_tag_key,
application_tag_value,
application_name,
tag_key,
tag_value
FROM aws.servicecatalogappregistry.application_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>application_tags</code> resource, see <a href="/providers/aws/servicecatalogappregistry/applications/#permissions"><code>applications</code></a>


