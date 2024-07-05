---
title: applications_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - applications_list_only
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

Lists <code>applications</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/applications/"><code>applications</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalogAppRegistry::Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.servicecatalogappregistry.applications_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the application.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the application.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="application_tag_key" /></td><td><code>string</code></td><td>The key of the AWS application tag, which is awsApplication. Applications created before 11/13/2023 or applications without the AWS application tag resource group return no value.</td></tr>
<tr><td><CopyableCode code="application_tag_value" /></td><td><code>string</code></td><td>The value of the AWS application tag, which is the identifier of an associated resource. Applications created before 11/13/2023 or applications without the AWS application tag resource group return no value.</td></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the application.</td></tr>
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
Lists all <code>applications</code> in a region.
```sql
SELECT
region,
id
FROM aws.servicecatalogappregistry.applications_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>applications_list_only</code> resource, see <a href="/providers/aws/servicecatalogappregistry/applications/#permissions"><code>applications</code></a>


